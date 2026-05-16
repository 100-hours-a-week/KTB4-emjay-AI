import argparse
import json
import random

KEYWORDS= None

FORTUNE_DATA = None
ROUTINE_DATA = None
QUOTE_DATA = None
DEFAULT_DATA = None

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def load_files():
    global KEYWORDS, FORTUNE_DATA, ROUTINE_DATA, QUOTE_DATA, DEFAULT_DATA

    KEYWORDS = load_json("data/keywords.json")

    FORTUNE_DATA = load_json("data/fortune_data.json")
    ROUTINE_DATA = load_json("data/routine_data.json")
    QUOTE_DATA = load_json("data/quote_data.json")
    DEFAULT_DATA = load_json("data/default_data.json")
    return

def extract_keywords(sentence):
    user_keywords = []

    for keyword in KEYWORDS["keywords"]:
        if keyword in sentence:
            user_keywords.append(keyword)

    return user_keywords


def recommend_by_keywords(user_keywords, data, default_data):
    candidates = []

    for item in data:
        keywords = item["keywords"]
        messages = item["messages"]

        for keyword in user_keywords:
            if keyword in keywords:
                candidates.extend(messages)
        
    if not candidates:
        candidates = default_data
    
    return random.choice(candidates)


def show_menu():
    print("\nBot: 무엇을 도와드릴까요?")

    print("=" * 25)
    print(f"| {'번호':^6} | {'항목':^8} |")
    print("=" * 25)

    for i, menu in enumerate(KEYWORDS["menus"], start=1):
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
            result = recommend_by_keywords(user_keywords, FORTUNE_DATA, DEFAULT_DATA["fortune"])
            print(f"\nBot: {result}")

        elif choice == "루틴":
            print("You: 오늘의 루틴을 추천해줘")
            result = recommend_by_keywords(user_keywords, ROUTINE_DATA, DEFAULT_DATA["routine"])
            print(f"\nBot: {result}")

        elif choice == "글귀":
            print("You: 오늘의 한 문장을 말해줘")
            result = recommend_by_keywords(user_keywords, QUOTE_DATA, DEFAULT_DATA["quote"])
            print(f"\nBot: {result}")

        else:
            print("Bot: 운세, 루틴, 글귀 중에서 입력해주세요.")
            continue


        print("\nBot: 더 확인하고 싶은 것이 있나요?\n")

        while True:
            answer = input("You: ")

            if answer in KEYWORDS["end_keywords"]:
                print("\nBot: 종료하겠습니다.")
                return

            elif answer in KEYWORDS["repeat_keywords"]:
                break

            else:
                print("\nBot: 응답을 이해하지 못했어요. 더 확인하고 싶다면 (응, 예) 등을, 종료하고 싶다면 (종료, 끝, 아니) 등을 입력해 주세요.\n")


def main():
    load_files()

    parser = argparse.ArgumentParser(description="계획 기반 '오늘의 문장' 추천 CLI 프로그램")
    parser.add_argument("--name", default="사용자", help="사용자 이름 입력")

    args = parser.parse_args()
    run_program(args.name)


if __name__ == "__main__":
    main()
