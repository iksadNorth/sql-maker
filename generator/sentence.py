from random import sample
from utils.itertools import infinitify_with_args

korean_sentences = [
    "안녕하세요, 반갑습니다.",
    "오늘 날씨가 정말 좋네요.",
    "한국 음식은 정말 맛있어요.",
    "공부를 열심히 해야겠어요.",
    "친구들과 함께 시간을 보내는 건 즐겁습니다.",
    "여름에 바다로 가는 게 좋아요.",
    "돈을 많이 벌고 싶어요.",
    "커피 한 잔 어떠세요?",
    "가족과 함께 있는 시간이 소중해요.",
    "운동을 해서 건강을 챙겨야 해요.",
    "책을 읽는 것이 취미입니다.",
    "영화를 보면 스트레스가 풀려요.",
    "나의 꿈은 세계 여행을 하는 것이에요.",
    "미래에 대한 계획을 세워봐야겠어요.",
    "음악을 듣는 건 마음을 편하게 해줘요.",
    "여행 가방을 싸는 건 항상 설레여요.",
    "우리 나라의 역사는 풍부하고 아름답습니다.",
    "새로운 경험을 쌓는 것이 중요하다고 생각해요.",
    "친구들과 미소 짓는 순간이 행복해요.",
    "미래에 대한 두려움을 극복해야 해요.",
    "맛있는 음식을 먹으면 기분이 좋아져요.",
    "새로운 언어를 배우는 건 어렵지만 재미있어요.",
    "건강하게 살기 위해 운동을 해야죠.",
    "모든 일에는 노력이 필요해요.",
    "가족들과 모여 식사하는 건 소중한 순간이에요.",
    "좋은 책을 읽으면 지식이 풍부해집니다.",
    "평화로운 곳에서 힐링하고 싶어요.",
    "항상 긍정적인 마인드를 가지려 노력하고 있어요.",
    "오늘 하루도 행복한 날이었으면 좋겠어요.",
    "자연을 즐기며 산책하는 건 좋은 생각이에요.",
    "공부는 평생의 일이에요.",
    "노래를 부르면 마음이 가벼워져요.",
    "친구들과 함께하는 여행은 최고에요.",
    "꿈을 이루기 위해 노력해야 해요.",
    "바쁜 일상에서 휴식이 필요해요.",
    "가족과의 대화는 소중하다고 생각해요.",
    "언젠가는 세계 일주를 꼭 해보고 싶어요.",
    "예술은 감동을 주는 힘이 있어요.",
    "자기 개발을 위해 노력하는 것이 중요하다고 생각해요.",
    "여름 휴가 계획을 세우는 게 재미있어요.",
    "음악은 마음의 위안이에요.",
    "배우고 성장하는 과정이 소중하다고 믿어요.",
    "좋은 사람들과 만나는 건 행운이에요.",
    "미소 지으면 세상이 더 밝아져요.",
    "도전은 성장의 기회이자 즐거움이에요.",
    "감사하며 살면 더 행복해져요.",
    "책을 읽는 것은 마음의 여행이에요.",
    "자연 속에서 에너지를 얻고 싶어요.",
    "모든 일에는 의미가 있다고 믿어요.",
    "평화로운 마음으로 살고 싶어요.",
    "무엇이든 시도해 보는 것이 중요하다고 생각해요.",
    "가족은 언제나 편안한 곳이에요.",
    "세상을 둘러보며 배우는 것이 즐거워요.",
    "꿈을 향해 끊임없이 나아가려 노력해야 해요.",
    "언젠가는 꿈을 이룰 거에요.",
    "자신을 믿고 도전하는 것이 중요하다고 생각해요.",
    "행복은 작은 것에서 찾을 수 있어요.",
    "건강한 식사를 하는 것은 중요하다고 생각해요.",
    "새로운 경험을 쌓는 것은 인생을 풍요롭게 만들어줘요.",
    "매일 웃음짓는 습관을 가지려 노력하고 있어요.",
    "친구와 함께 즐겁게 놀면 스트레스가 풀려요.",
    "열심히 일하면 보람을 느낄 수 있어요.",
    "사랑과 관심을 나누는 것이 중요하다고 생각해요.",
    "지금 이 순간을 즐겨야 해요.",
    "자연의 아름다움을 느끼며 산책하고 싶어요.",
    "도전을 통해 더 나은 사람이 되고 싶어요.",
    "열심히 노력하면 꼭 성취할 수 있어요.",
    "가족과 함께하는 시간은 특별하다고 느껴져요.",
    "새로운 사람들과 친구가 되는 건 흥미로워요.",
    "미소 짓는 것은 마음을 따뜻하게 만들어줘요.",
    "노력하면 언젠가는 성과가 나타날 거에요.",
    "자기 자신을 사랑하고 받아들이는 것이 중요하다고 생각해요.",
    "좋은 친구들을 사귀는 건 행운이에요.",
    "목표를 향해 끈질기게 나아가는 것이 중요하다고 믿어요.",
    "매일 감사하는 마음을 가지려 노력하고 있어요.",
    "밝은 마음으로 살면 모든 게 행복해 보여요.",
    "여행은 새로운 경험을 만들어줘요.",
    "흥미 있는 일을 하면 즐겁게 시간을 보낼 수 있어요.",
    "자연을 사랑하며 보호하는 것이 중요하다고 생각해요.",
    "새로운 도전을 두려워하지 않고 받아들이려 노력하고 있어요.",
    "무엇이든 열심히 하는 것이 성공의 비결이에요.",
    "미소 짓는 것은 주변 사람들에게도 긍정적인 영향을 미칠 거예요.",
    "자신의 열정을 추구하는 것이 중요하다고 생각해요.",
    "좋은 책을 읽으면 지식이 풍부해질 뿐만 아니라 영감도 받아요.",
    "힘들 때도 포기하지 않고 노력하면 언젠가는 성공할 거에요.",
    "예술과 문화를 즐기며 삶을 더 풍요롭게 만들어요.",
    "자기 자신을 믿고 자신감을 갖는 것이 중요하다고 생각해요.",
    "성장과 배움을 소중히 여기려 노력하고 있어요.",
    "사랑과 배려가 있는 삶은 풍요로워요.",
    "언젠가는 꿈을 이룰 수 있을 거에요.",
    "행복은 마음의 상태에 달려 있어요.",
    "매일 새로운 것을 배우는 것은 즐거워요.",
    "친구와 함께 있으면 행복해져요.",
    "모든 일에 최선을 다하는 것이 중요하다고 생각해요.",
    "자연을 사랑하고 보호하는 것은 지구의 미래를 위해 중요하다고 생각해요.",
    "세상을 더 넓게 볼 수 있는 여행은 특별해요.",
    "꾸준한 노력이 성과를 가져다 줄 거에요.",
    "자신의 가치를 인정하고 사랑하는 것이 중요하다고 생각해요.",
    "좋은 친구들과 함께 있으면 즐겁고 행복해요.",
    "힘들 때도 긍정적으로 생각하려 노력하고 있어요.",
    "목표를 향해 달려가는 것은 흥미로워요.",
    "일상 속에서 작은 행복을 찾아보세요.",
    "자연을 존중하고 보호하는 것이 지구의 미래에 도움이 됩니다.",
]

@infinitify_with_args
def generator(n : int = 1, delimiter : str = '\n'):
    list_sentence_selected = sample(korean_sentences, n)
    return delimiter.join(list_sentence_selected)