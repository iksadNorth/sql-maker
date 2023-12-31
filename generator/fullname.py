from random import choice
from utils.itertools import infinitify_with_args

first_names = [
    '김', '이', '박', '최', '정', '강', '조', '윤', '장', '임'
]
last_names = [
    "민준", "서연", "지우", "지훈", "서현", "하준", "예진", "재원", "지민", "영준",
    "다은", "윤서", "지윤", "민서", "예준", "준서", "현우", "지영", "준영", "수빈",
    "지호", "서영", "도현", "예나", "은우", "승민", "세진", "윤호", "지안", "현서",
    "예슬", "준혁", "서아", "시우", "민지", "은서", "민재", "하윤", "성민", "유진",
    "세연", "민송", "지우", "시윤", "승현", "서하", "은영", "혜원", "윤아", "재민",
    "서은", "서진", "승우", "서윤", "예지", "재윤", "승찬", "하람", "은혜", "서하",
    "준희", "재은", "민영", "지원", "서우", "하연", "준호", "지하", "민규", "지선",
    "다현", "은채", "시현", "도영", "성호", "태영", "준석", "재하", "세영", "시은",
    "서희", "현지", "주영", "지영", "은주", "은미", "예빈", "승준", "영호", "성우",
    "다인", "채원", "현민", "성훈", "민호", "태진", "진영", "승원", "예린", "정우"
]

@infinitify_with_args
def generator():
    return choice(first_names) + choice(last_names)