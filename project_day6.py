# ================= Welcome Message =================
print("============ Welcome to the QUIZ Game! ===========")
score = 0

# ================= Quiz Questions =================
quiz = [
    {"question": "What is the capital of India?",
     "options": ["a) Mumbai", "b) Delhi", "c) Kolkata", "d) Chennai"],
     "answer": "b"},

    {"question": "Which planet is known as the 'Red Planet'?",
     "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
     "answer": "b"},

    {"question": "Who wrote the national anthem of India, 'Jana Gana Mana'?",
     "options": ["a) Bankim Chandra Chatterjee", "b) Swami Vivekananda", "c) Rabindranath Tagore", "d) Sarojini Naidu"],
     "answer": "c"},

    {"question": "What is the largest ocean on Earth?",
     "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"],
     "answer": "d"},

    {"question": "Which element has the chemical symbol 'O'?",
     "options": ["a) Gold", "b) Silver", "c) Oxygen", "d) Iron"],
     "answer": "c"},

    {"question": "In which year did India gain independence from British rule?",
     "options": ["a) 1942", "b) 1945", "c) 1947", "d) 1950"],
     "answer": "c"},

    {"question": "Which is the tallest mountain in the world?",
     "options": ["a) K2", "b) Mount Everest", "c) Kangchenjunga", "d) Lhotse"],
     "answer": "b"},

    {"question": "What is the currency of Japan?",
     "options": ["a) Yuan", "b) Won", "c) Yen", "d) Ringgit"],
     "answer": "c"},

    {"question": "Which organ in the human body is responsible for pumping blood?",
     "options": ["a) Lungs", "b) Brain", "c) Liver", "d) Heart"],
     "answer": "d"},

    {"question": "Who is known as the 'Father of the Nation' in India?",
     "options": ["a) Jawaharlal Nehru", "b) Subhas Chandra Bose", "c) Mahatma Gandhi", "d) B.R. Ambedkar"],
     "answer": "c"},

    {"question": "Which is the smallest continent by land area?",
     "options": ["a) Europe", "b) Australia", "c) Antarctica", "d) South America"],
     "answer": "b"}
]

# ================= Quiz Loop =================
for index, q in enumerate(quiz, start=1):
    print(f"\nQ{index}: {q['question']}")
    for opt in q["options"]:
        print(opt)
    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    if user_answer == q["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer was: {q['answer'].upper()}")

# ================= Final Score =================
print("\n============ Quiz Completed! ===========")
print(f"Your final score is: {score} / {len(quiz)} 💯")
