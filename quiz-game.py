
# ------ QUIZ GAME ------

quiz = {
    "What is the capital of India ?": "Delhi",
    "Which planet is known as the red planet ?": "Mars",
    "What is the largest mammal ?": "Blue Whale",
    "How many days are there in a leap year ?": "366",
    "Who wrote the Ramayana ?": "Valmiki",
}

def display_menu():
    print("\n=== Quiz Game Menu ===")
    print("1. Start Quiz")
    print("2. VIew All QUestions and Answers")
    print("3. Add a New Questions")
    print("4. Delete a Question")
    print("5. Exit")
    print("=" * 24)

def start_quiz():

    score = 0
    print("\n--- STarting Quiz ---")

    for question, answer in quiz.items():
        print("\nQuestion")
        print(question)
        user_answer = input("Enter Your Answer:").strip()

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct Answer:",answer)

        print("\n--- Quiz Complete ---")
        print(f"Your Score: {score} out of {len(quiz)}")
        print("-"*22)

while True:
    display_menu()

    choice  = input("Enter Your Choice (1-5): ").strip()

    match choice:
        case "1":
            pass
            start_quiz()
        case "2":
           pass
        case "3":
           pass
        case "4":
           pass
        case "5":
           print("Exiting")
           break
        case _:
            print("Invalid Choice. Please Try Again!")



