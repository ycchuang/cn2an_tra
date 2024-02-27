NUMBER_CN2AN = {
    "零": 0,
    "〇": 0,
    "一": 1,
    "壹": 1,
    "幺": 1,
    "二": 2,
    "贰": 2,
    "两": 2,
    "三": 3,
    "叁": 3,
    "四": 4,
    "肆": 4,
    "五": 5,
    "伍": 5,
    "六": 6,
    "陆": 6,
    "七": 7,
    "柒": 7,
    "八": 8,
    "捌": 8,
    "九": 9,
    "玖": 9,
}
UNIT_CN2AN = {
    "十": 10,
    "拾": 10,
    "百": 100,
    "佰": 100,
    "千": 1000,
    "仟": 1000,
    "万": 10000,
    "亿": 100000000,
}
UNIT_LOW_AN2CN = {
    10: "十",
    100: "百",
    1000: "千",
    10000: "万",
    100000000: "亿",
}
NUMBER_LOW_AN2CN = {
    0: "零",
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
}
NUMBER_UP_AN2CN = {
    0: "零",
    1: "壹",
    2: "贰",
    3: "叁",
    4: "肆",
    5: "伍",
    6: "陆",
    7: "柒",
    8: "捌",
    9: "玖",
}
UNIT_LOW_ORDER_AN2CN = [
    "",
    "十",
    "百",
    "千",
    "万",
    "十",
    "百",
    "千",
    "亿",
    "十",
    "百",
    "千",
    "万",
    "十",
    "百",
    "千",
]
UNIT_UP_ORDER_AN2CN = [
    "",
    "拾",
    "佰",
    "仟",
    "万",
    "拾",
    "佰",
    "仟",
    "亿",
    "拾",
    "佰",
    "仟",
    "万",
    "拾",
    "佰",
    "仟",
]
STRICT_CN_NUMBER = {
    "零": "零",
    "一": "一壹",
    "二": "二贰",
    "三": "三叁",
    "四": "四肆",
    "五": "五伍",
    "六": "六陆",
    "七": "七柒",
    "八": "八捌",
    "九": "九玖",
    "十": "十拾",
    "百": "百佰",
    "千": "千仟",
    "万": "万",
    "亿": "亿",
}
NORMAL_CN_NUMBER = {
    "零": "零〇",
    "一": "一壹幺",
    "二": "二贰两",
    "三": "三叁仨",
    "四": "四肆",
    "五": "五伍",
    "六": "六陆",
    "七": "七柒",
    "八": "八捌",
    "九": "九玖",
    "十": "十拾",
    "百": "百佰",
    "千": "千仟",
    "万": "万",
    "亿": "亿",
}
WORD_TO_SIM = {
    "兩兆": "二兆",
    "兩億": "二億",
    "兩萬": "二萬",
    "兩千": "二千",
    "兩百": "二百",
    "兩佰": "二佰",
    #單位量詞
    "兩公斤": "二公斤",
    "兩克": "二克",
    "兩公克": "二公克",
    "兩斤": "二斤",
    "兩台斤": "二台斤",
    "兩厘": "二厘",
    "兩毫": "二毫",
    "兩微": "二微",
    "兩奈": "二奈",
    "兩公里": "二公里",
    "兩米": "二米",
    "兩尺": "二尺",
    "兩公尺": "二公尺",
    "兩台尺": "二台尺",
    "兩平方": "二平方",
    "兩立方": "二立方",
    "兩升": "二升",
    "兩公升": "二公升",
    "兩分": "二分",
    "兩英吋": "二英吋",
    "兩英呎": "二英呎",
    "兩英哩": "二英哩",
    "兩英寸": "二英寸",
    "兩英尺": "二英尺",
    "兩英里": "二英里",
    "兩碼": "二碼",
    "兩磅": "二磅",
    "兩英磅": "二英磅",
    "兩盎司": "二盎司",
    "兩夸特": "二夸特",
    "兩英噸": "二英噸",
    "兩品脫": "二品脫",
    "兩加侖": "二加侖",
    #量詞
    "兩串": "二串",
    "兩件": "二件",
    "兩份": "二份",
    "兩刀": "二刀",
    "兩列": "二列",
    "兩則": "二則",
    "兩副": "二副",
    "兩口": "二口",
    "兩只": "二只",
    "兩地": "二地",
    "兩場": "二場",
    "兩堵": "二堵",
    "兩套": "二套",
    "兩封": "二封",
    "兩尊": "二尊",
    "兩對": "二對",
    "兩帖": "二帖",
    "兩席": "二席",
    "兩幀": "二幀",
    "兩幢": "二幢",
    "兩床": "二床",
    "兩座": "二座",
    "兩張": "二張",
    "兩所": "二所",
    "兩手": "二手",
    "兩把": "二把",
    "兩抔": "二抔",
    "兩方": "二方",
    "兩本": "二本",
    "兩架": "二架",
    "兩根": "二根",
    "兩棟": "二棟",
    "兩棵": "二棵",
    "兩派": "二派",
    "兩炷": "二炷",
    "兩瓣": "二瓣",
    "兩番": "二番",
    "兩發": "二發",
    "兩盤": "二盤",
    "兩窩": "二窩",
    "兩筆": "二筆",
    "兩節": "二節",
    "兩縷": "二縷",
    "兩群": "二群",
    "兩艘": "二艘",
    "兩記": "二記",
    "兩趟": "二趟",
    "兩通": "二通",
    "兩道": "二道",
    "兩部": "二部",
    "兩門": "二門",
    "兩陣": "二陣",
    "兩面": "二面",
    "兩頂": "二頂",
    "兩味": "二味",
    "兩輛": "二輛",
    "兩大": "二大",
    "兩小": "二小",
    "負": "负",
    #"點": "点",
    "圓": "圆",
    "萬": "万",
}
WORD_TO_TRA = {
    "负": "負",
    #"点": "點",
    "圆": "圓",
    "万": "萬",
}