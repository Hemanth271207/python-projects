def quiz():
    score = 0

    print("Question 1: What is the capital of India?")
    ans = input("Your answer: ")
    if ans.lower() == "delhi":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer is Delhi.")

    print("Question 2: What is 5 x 6?")
    ans = input("Your answer: ")
    if ans == "30":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer is 30.")

    print("Question 3: Which language are we learning?")
    ans = input("Your answer: ")
    if ans.lower() == "python":
        print("Correct!")
        score += 1
    else:
        print("Wrong! It's Python.")

    print("\nYou scored", score, "out of 3!")

quiz()
