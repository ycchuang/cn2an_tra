import re

from .cn2an import Cn2An
from .an2cn import An2Cn
from .conf import UNIT_CN2AN, WORD_TO_SIM, WORD_TO_TRA


class Transform(object):
    def __init__(self) -> None:
        self.all_num_ezero = "一二两三四五六七八九"
        self.all_num = "零一二两三四五六七八九"
        self.all_unit = "".join(list(UNIT_CN2AN.keys()))
        self.cn2an = Cn2An().cn2an
        self.an2cn = An2Cn().an2cn
        self.WORD_TO_SIM = WORD_TO_SIM
        self.WORD_TO_TRA = WORD_TO_TRA
        self.cn_zeropattern = f"负?([零{self.all_num}]+点)?[{self.all_num}]+|负?零[{self.all_num}]+|零[{self.all_num}]+"
        self.zeroheading = f"负?零+[{self.all_num_ezero}]"
        self.cn_pattern = f"负?([{self.all_num}{self.all_unit}]+点)?[{self.all_num}{self.all_unit}]+"
        self.cn_pattern_added = f"负?([{self.all_num}{self.all_unit}]+点)?[{self.all_num}{self.all_unit}]+|\
            负?([{self.all_num}{self.all_unit}{self.all_num}]+点)?[{self.all_num}{self.all_unit}{self.all_num}]+|\
            负?([{self.all_num}{self.all_unit}{self.all_num}{self.all_unit}]+点)?[{self.all_num}{self.all_unit}{self.all_num}{self.all_unit}]+"
        self.smart_cn_pattern = f"-?([0-9]+.)?[0-9]+[{self.all_unit}]+"

    def transform(self, inputs: str, method: str = "cn2an") -> str:
        #To Sim Chinese
        for nor_num in self.WORD_TO_SIM.keys():
            inputs = inputs.replace(nor_num, self.WORD_TO_SIM[nor_num])
        
        if method == "cn2an":
            inputs = inputs.replace("廿", "二十").replace("半", "0.5").replace("两", "2")
            # date
            inputs = re.sub(
                fr"((({self.smart_cn_pattern})|({self.cn_pattern}))年)?([{self.all_num}十]+月)?([{self.all_num}十]+日)?",
                lambda x: self.__sub_util(x.group(), "cn2an", "date"), inputs)
            # fraction
            inputs = re.sub(fr"{self.cn_pattern}分之{self.cn_pattern}",
                            lambda x: self.__sub_util(x.group(), "cn2an", "fraction"), inputs)
            # percent
            inputs = re.sub(fr"百分之{self.cn_pattern}",
                            lambda x: self.__sub_util(x.group(), "cn2an", "percent"), inputs)
            # celsius
            inputs = re.sub(fr"{self.cn_pattern}摄氏度",
                            lambda x: self.__sub_util(x.group(), "cn2an", "celsius"), inputs)
            # number
            inputs = re.sub(self.cn_pattern_added,
                            lambda x: self.__sub_util(x.group(), "cn2an", "number"), inputs)
            # zeronumber
            output = re.sub(self.cn_zeropattern,
                            lambda x: self.__sub_util(x.group(), "cn2an", "zeronumber"), inputs)


        elif method == "an2cn":
            # date
            inputs = re.sub(r"(\d{2,4}年)?(\d{1,2}月)?(\d{1,2}日)?",
                            lambda x: self.__sub_util(x.group(), "an2cn", "date"), inputs)
            # fraction
            inputs = re.sub(r"\d+/\d+",
                            lambda x: self.__sub_util(x.group(), "an2cn", "fraction"), inputs)
            # percent
            inputs = re.sub(r"-?(\d+\.)?\d+%",
                            lambda x: self.__sub_util(x.group(), "an2cn", "percent"), inputs)
            # celsius
            inputs = re.sub(r"\d+℃",
                            lambda x: self.__sub_util(x.group(), "an2cn", "celsius"), inputs)
            # number
            output = re.sub(r"-?(\d+\.)?\d+",
                            lambda x: self.__sub_util(x.group(), "an2cn", "number"), inputs)
        else:
            raise ValueError(f"error method: {method}, only support 'cn2an' and 'an2cn'!")

        #Back to Tra Chinese
        for nor_num in self.WORD_TO_TRA.keys():
            output = output.replace(nor_num, self.WORD_TO_TRA[nor_num])
        print (str(input))
        return output

    def __sub_util(self, inputs, method: str = "cn2an", sub_mode: str = "number") -> str:
        try:
            if inputs:
                if method == "cn2an":
                    if sub_mode == "date":
                        return re.sub(fr"(({self.smart_cn_pattern})|({self.cn_pattern}))",
                                      lambda x: str(self.cn2an(x.group(), "smart")), inputs)
                    elif sub_mode == "fraction":
                        if inputs[0] != "百":
                            frac_result = re.sub(self.cn_pattern,
                                                 lambda x: str(self.cn2an(x.group(), "smart")), inputs)
                            numerator, denominator = frac_result.split("分之")
                            return f"{denominator}/{numerator}"
                        else:
                            return inputs
                    elif sub_mode == "percent":
                        return re.sub(f"(?<=百分之){self.cn_pattern}",
                                      lambda x: str(self.cn2an(x.group(), "smart")), inputs).replace("百分之", "") + "%"
                    elif sub_mode == "celsius":
                        return re.sub(f"{self.cn_pattern}(?=摄氏度)",
                                      lambda x: str(self.cn2an(x.group(), "smart")), inputs).replace("摄氏度", "℃")
                    elif sub_mode == "number":
                        if inputs[0] != "零" and inputs[:2] != "负零":
                            return str(self.cn2an(inputs, "smart"))
                        else:
                            return inputs
                    elif sub_mode == "zeronumber":
                        try:
                            rpl_str = re.match(f"{self.zeroheading}", inputs).group(0)[:-1]
                        except:
                            rpl_str = ""
                        inputs = inputs.replace("负","")
                        return str(rpl_str.replace("负","-").replace("零","0"))+str(self.cn2an(inputs, "smart"))
                    else:
                        raise Exception(f"error sub_mode: {sub_mode} !")
                else:
                    if sub_mode == "date":
                        inputs = re.sub(r"\d+(?=年)",
                                        lambda x: self.an2cn(x.group(), "direct"), inputs)
                        return re.sub(r"\d+",
                                      lambda x: self.an2cn(x.group(), "low"), inputs)
                    elif sub_mode == "fraction":
                        frac_result = re.sub(r"\d+", lambda x: self.an2cn(x.group(), "low"), inputs)
                        numerator, denominator = frac_result.split("/")
                        return f"{denominator}分之{numerator}"
                    elif sub_mode == "celsius":
                        return self.an2cn(inputs[:-1], "low") + "摄氏度"
                    elif sub_mode == "percent":
                        return "百分之" + self.an2cn(inputs[:-1], "low")
                    elif sub_mode == "number":
                        return self.an2cn(inputs, "low")
                    else:
                        raise Exception(f"error sub_mode: {sub_mode} !")
        except Exception as e:
            print(f"WARN: {e}")
            return inputs
