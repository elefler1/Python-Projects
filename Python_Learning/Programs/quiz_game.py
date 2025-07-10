# Python Quiz Game:

questions = ("How many elements are there in the periodic table?: ", 
             "Which animal lays the largest eggs?: ", 
             "What is the most abundant gas in the Earth's atmosphere?: ", 
             "How many bones are there in the adult human body?: ", 
             "Which planet in the solar system is the hottest?: ")

options = (("A. 118", "B. 120", "C. 119", "D. 121"), 
           ("A. Blue Whale", "B. Elephant", "C. Ostrich", "D. Crocodile"), 
           ("A. Hydrogen", "B. Nitrogen", "C. Carbon Dioxide", "D. Oxygen"), 
           ("A. 206", "B. 201", "C. 205", "D. 210"), 
           ("A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"))

answers = ("A", "C", "D", "A", "A")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"The correct answer is: {answers[question_number]}")
    question_number += 1

print("----------------------------")
print("         RESULTS            ")
print("----------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Your final score is: {int(score / len(questions) * 100)}%")
