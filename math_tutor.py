import random
import time

def start_math_quiz():
    # Input: number of questions
    while True:
        try:
            no_of_questions = int(input("Enter number of questions: "))
            if no_of_questions <= 0:
                print("Enter at least 1 question.")
                continue
            break
        except:
            print("Invalid input. Enter a number.")

    # Input: max number
    while True:
        try:
            max_num = int(input("How high should numbers go? "))
            if max_num <= 0:
                print("Enter a positive number.")
                continue
            break
        except:
            print("Invalid input. Enter a number.")

    score = 0
    answers_list = []

    start = time.time()

    for i in range(1, no_of_questions + 1):
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)

        correct_answer = num1 * num2

        # User input with validation
        while True:
            try:
                user_answer = int(input(f"Q{i}: {num1} x {num2} = "))
                break
            except:
                print("Invalid input. Enter a number.")

        if user_answer == correct_answer:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong ❌ (Correct: {correct_answer})")

        answers_list.append(
            f"{num1} x {num2} = {correct_answer} | You: {user_answer}"
        )

    end = time.time()

    total_time = round(end - start, 2)
    avg_time = round(total_time / no_of_questions, 2)
    percentage = round((score / no_of_questions) * 100, 2)

    print("\n----- Thanks for playing -----\n")

    print(f"Score: {score}/{no_of_questions}")
    print(f"Percentage: {percentage}%")
    print(f"Total time: {total_time} seconds")
    print(f"Average time per question: {avg_time} seconds")

    print("\n----- ANSWERS REVIEW -----\n")
    for ans in answers_list:
        print(ans)