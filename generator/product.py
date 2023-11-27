from random import choice
from utils.itertools import infinitify_with_args

colors = [
    '빨간색', '주황색', '노란색', '녹색', '파란색', '남색', '보라색', '아이보리색', '검정색', '회색'
]
clothing_categories = [
    "티셔츠", "바지", "드레스", "셔츠", "스웨터", "자켓", "코트", "청바지", "치마", "후드"
    ]
sizes = ["S", "M", "L", "XL", "XXL", "XXXL"]
materials = ["면", "울", "가죽", "나일론", "폴리에스터"]

@infinitify_with_args
def generator():
    return f"{choice(colors)} {choice(materials)} 재질 {choice(clothing_categories)} {choice(sizes)}"