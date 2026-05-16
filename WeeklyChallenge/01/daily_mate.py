import argparse
import random

MENUS = ["운세", "루틴", "글귀"]
KEYWORDS = ["야구", "버스", "경기", "공연", "축제", "음악", "친구", "지하철"]
END_KEYWORDS = ["종료", "끝", "아니", "없어", "아니요", "ㄴㄴ"]
REPEAT_KEYWORDS = ["응", "있어", "네", "예", "ㅇㅇ"]

FORTUNE_DATA = {
    "야구": [
        "오늘은 응원하는 마음이 좋은 기운을 불러올 거예요.",
        "경기장에서 뜻밖의 즐거운 순간을 만날 수 있어요."
    ],
    "버스": [
        "이동 중에 좋은 생각이 떠오를 수 있는 하루예요.",
        "가는 길이 조금 길어도 기분 좋은 일이 생길 수 있어요."
    ],
    "경기": [
        "오늘은 결과보다 과정을 즐기면 더 좋은 하루가 될 거예요.",
        "승리의 기운이 가까이에 있어요."
    ]
}

ROUTINE_DATA = {
    "야구": [
        "출발 전 응원 도구와 티켓을 확인하세요.",
        "경기 시작 1시간 전에는 도착할 수 있게 준비해보세요."
    ],
    "버스": [
        "버스 도착 시간을 미리 확인하고 10분 일찍 출발해보세요.",
        "이동 중 들을 음악이나 플레이리스트를 준비해보세요."
    ],
    "경기": [
        "경기 전 간단히 식사하고 물을 챙겨보세요.",
        "오늘의 경기 포인트를 미리 찾아보고 가면 더 재미있어요."
    ]
}

QUOTE_DATA = {
    "야구": [
        "좋아하는 것을 보러 가는 하루는 이미 특별한 하루다.",
        "응원의 순간은 오래 남는 추억이 된다."
    ],
    "버스": [
        "가는 길마저 오늘의 이야기가 된다.",
        "천천히 가도 즐거운 목적지가 있다면 괜찮다."
    ],
    "경기": [
        "결과를 기다리는 설렘도 하나의 추억이다.",
        "최선을 다한 순간은 언제나 빛난다."
    ]
}

DEFAULT_FORTUNE = [
    "오늘은 작은 기대가 좋은 결과로 이어질 수 있어요.",
    "평소보다 긍정적인 마음이 행운을 불러올 거예요."
]

DEFAULT_ROUTINE = [
    "오늘 해야 할 일을 하나씩 정리해보세요.",
    "가장 중요한 일부터 천천히 시작해보세요."
]

DEFAULT_QUOTE = [
    "오늘의 작은 한 걸음이 내일의 큰 변화를 만든다.",
    "천천히 가도 멈추지만 않으면 괜찮다."
]


def extract_keywords(sentence):
    user_keywords = []

    for keyword in KEYWORDS:
        if keyword in sentence:
            user_keywords.append(keyword)

    return user_keywords


def recommend_by_keywords(user_keywords, data, default_data):
    candidates = []

    for keyword in user_keywords:
        if keyword in data:
            candidates.extend(data[keyword])

    if not candidates:
        candidates = default_data

    return random.choice(candidates)


def show_menu():
    print("\nBot: 무엇을 도와드릴까요?")

    print("=" * 25)
    print(f"| {'번호':^6} | {'항목':^8} |")
    print("=" * 25)

    for i, menu in enumerate(MENUS, start=1):
        print(f"| {i:^8} | {menu:^8} |")

    print("=" * 25)

def run_program(username):
    print(f"Bot: 안녕하세요, {username}님!")
    print("Bot: 오늘. 당신의 계획을 말해주세요.\n")

    sentence = input("You: ")
    user_keywords = extract_keywords(sentence)


    while True:
        show_menu()
        choice = input("\nYou: ")

        if choice == "운세":
            print("You: 오늘의 운세를 알려줘")
            result = recommend_by_keywords(user_keywords, FORTUNE_DATA, DEFAULT_FORTUNE)
            print(f"\nBot: {result}")

        elif choice == "루틴":
            print("You: 오늘의 루틴을 추천해줘")
            result = recommend_by_keywords(user_keywords, ROUTINE_DATA, DEFAULT_ROUTINE)
            print(f"\nBot: {result}")

        elif choice == "글귀":
            print("You: 오늘의 한 문장을 말해줘")
            result = recommend_by_keywords(user_keywords, QUOTE_DATA, DEFAULT_QUOTE)
            print(f"\nBot: {result}")

        else:
            print("Bot: 운세, 루틴, 글귀 중에서 입력해주세요.")
            continue


        print("\nBot: 더 확인하고 싶은 것이 있나요?\n")

        while True:
            answer = input("You: ")

            if answer in END_KEYWORDS:
                print("\nBot: 종료하겠습니다.")
                return

            elif answer in REPEAT_KEYWORDS:
                break

            else:
                print("\nBot: 응답을 이해하지 못했어요. 더 확인하고 싶다면 (응, 예) 등을, 종료하고 싶다면 (종료, 끝, 아니) 등을 입력해 주세요.\n")


def main():
    parser = argparse.ArgumentParser(description="계획 기반 '오늘의 문장' 추천 CLI 프로그램")
    parser.add_argument("--name", default="사용자", help="사용자 이름 입력")

    args = parser.parse_args()
    run_program(args.name)


if __name__ == "__main__":
    main()
