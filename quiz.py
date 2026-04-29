import random

# ============================================
#           ONLINE QUIZ SYSTEM
# ============================================

question_bank = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum",
                    "C. James Gosling", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Processing Unit",
                    "C. Central Program Unit", "D. Control Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "What is the output of 10 // 3?",
        "options": ["A. 3", "B. 3.33", "C. 4", "D. 1"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. **", "C. //", "D. %"],
        "answer": "B"
    },
    {
        "question": "Which function is used to take user input?",
        "options": ["A. print()", "B. scan()", "C. input()", "D. get()"],
        "answer": "C"
    },
    {
        "question": "Which company developed Java?",
        "options": ["A. Microsoft", "B. Oracle",
                    "C. Sun Microsystems", "D. IBM"],
        "answer": "C"
    }
]


def run_quiz():
    print("=" * 60)
    print("          WELCOME TO ONLINE QUIZ SYSTEM")
    print("=" * 60)

    while True:
        # Shuffle questions for each new game
        questions = random.sample(question_bank, len(question_bank))

        score = 0

        for i, q in enumerate(questions, start=1):
            print("\n" + "=" * 60)
            print(f"Question {i}: {q['question']}")
            print("=" * 60)

            for option in q["options"]:
                print(option)

            while True:
                answer = input(
                    "Enter your answer (A/B/C/D): "
                ).strip().upper()

                if answer in ["A", "B", "C", "D"]:
                    break

                print("Invalid input! Please enter A, B, C, or D.")

            if answer == q["answer"]:
                print("Correct Answer!")
                score += 1
            else:
                print(
                    f"Wrong Answer! "
                    f"Correct answer is {q['answer']}"
                )

        # Display Result
        percentage = (score / len(questions)) * 100

        print("\n" + "=" * 60)
        print("                 QUIZ COMPLETED")
        print("=" * 60)
        print(f"Your Score : {score}/{len(questions)}")
        print(f"Percentage : {percentage:.2f}%")

        if percentage == 100:
            print("Outstanding! Perfect Score!")
        elif percentage >= 75:
            print("Excellent Performance!")
        elif percentage >= 50:
            print("Good Job!")
        else:
            print("Keep Practicing!")

        # Ask only after completing all questions
        retry = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if retry != "yes":
            print("\nThank you for playing the Quiz!")
            break


if __name__ == "__main__":
    run_quiz()