wrong = 0
right = 0
total = 0


print("-----General Knowledge Quiz-----")
answer1 = input("1. What fruit is linked to Sir Isaac Newton's discory of gravity?")
if answer1 == "apple" or answer1 == "Apple":
    right += 1
    total += 1
else:
    wrong += 1
    total += 1

answer2 = input("2. What is the rarest blood type in humans?")
if answer2 == "AB negative":
    right += 1
    total += 1
else:
    wrong += 1
    total += 1

answer3 = int(input("3. In what year was the first Star Wars film released?"))
if answer3 == 1977:
    right += 1
    total += 1
else:
    wrong += 1
    total += 1

answer4 = input("4. Who was the last Tudor monarch?")
if answer4 == "Elizabeth I":
    right += 1
    total += 1
else:
    wrong += 1
    total += 1

answer5 = input("5. Which country has won the most FIFA world cups?")
if answer5 == "Brazil" or answer5 == "brazil":
    right += 1
    total += 1
else: 
    wrong += 1
    total += 1

print("-----End of Quiz-----")
print("You got: " + str(right) + " correct answers")
print("You got: " + str(wrong) + " wrong answers")
print(str(right) + "/" + str(total))

