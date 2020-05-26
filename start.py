from random import randrange

player2points = []
player1points = []


def Josh_function2():
    print(sum(player2points))
    Josh_function2()


def Josh_function1():
    print(sum(player1points))
    Josh_function1()


print("In order to determine who goes first type a number either 0 or 1")
print("This program will randomly generate either 0 or 1")
print("If you guess correctly, you will be player 1 and go first")
print("If you get it wrong, you will be Player 2 and the other person will be player 1 and get to go first")
print("Player 1 will always go first")
userguessednum = int(input())
random = randrange(2)

if userguessednum == random:
    print("you guessed the same number as the computer")
    print("your number is:" + str(userguessednum))
    print("computer number is:" + str(random))
    print("You are player 1")
    print("You will be going first")
else:
    print("your number did NOT match with the computer's number")
    print("your number is:" + str(userguessednum))
    print("computer number is:" + str(random))
    print("You are player 2")
    print("you will be going second")

print("================================")

########### QUESTION LIST START##############

q1 = "Here is the first question \n"
q1 = q1 + "Question1 - About how many Americans die per year because they can’t afford health care? \n"
q1 = q1 + "possible answers \n"
q1 = q1 + "1 - 678,000 \n"
q1 = q1 + "2 - 198,000 \n"
q1 = q1 + "3 - 45,000 \n"
q1 = q1 + "4 - 354,000 \n"
q1 = q1 + "write down your number below \n"

q2 = "Here is the second question \n"
q2 = q2 + "Question2 - About what percent of the American population does not have health insurance?\n"
q2 = q2 + "Possible answers \n"
q2 = q2 + "1 - 10.7% \n"
q2 = q2 + "2 - 20.5% \n"
q2 = q2 + "3 - 50.3% \n"
q2 = q2 + "4 - 8.5% \n"
q2 = q2 + "write down your number below \n"

q3 = "Here is the third question \n"
q3 = q3 + "Question 3 - What is the monthly average cost for health care in the United States?  \n"
q3 = q3 + "Possible answers \n"
q3 = q3 + "1 - $511 \n"
q3 = q3 + "2 - $200.35 \n"
q3 = q3 + "3 - $700 \n"
q3 = q3 + "4 - $143 \n"
q3 = q3 + "write down your number below \n"

q4 = "Here is the fourth question \n"
q4 = q4 + "Question 4 - About how much money does the U.S. spend on healthcare per year? \n"
q4 = q4 + "Possible answers \n"
q4 = q4 + "1 - $3.8 billion dollars \n"
q4 = q4 + "2 - $3.5 trillion dollars \n"
q4 = q4 + "3 - $12.3 billion dollars \n"
q4 = q4 + "4 - $32.2 million dollars \n"

q5 = "Here is the fifth question"
q5 = q5 + "Question 5 - What percentage of Americans have health problems but can’t go to the doctors because of health insurance? \n"
q5 = q5 + "Possible answers \n"
q5 = q5 + "1 - 23.4% \n"
q5 = q5 + "2 - 39.6% \n"
q5 = q5 + "3 - 76.8% \n"
q5 = q5 + "4 - 50.45 \n"
q5 = q5 + "write down your number below \n"

q6 = "Here is the sixth question"
q6 = q6 + "Question 6 - About what percentage of healthcare does American tax make up? \n"
q6 = q6 + "Possible answers \n"
q6 = q6 + "1 - 50% \n"
q6 = q6 + "2 - 14% \n"
q6 = q6 + "3 - 64% \n"
q6 = q6 + "4 - 78% \n"
q6 = q6 + "write down your number below \n"

q7 = "Here is the seventh question \n"
q7 = q7 + "Question 7 - What is the average amount of visits Americans make to the doctors per year? \n"
q7 = q7 + "Possible answers \n"
q7 = q7 + "1 - 120 \n"
q7 = q7 + "2 - 200 \n"
q7 = q7 + "3 - 57 \n"
q7 = q7 + "4 - 4 \n"
q7 = q7 + "write down your number below \n"

q8 = "Here is the eighth question"
q8 = q8 + "Question 8 - What is the percentage of the health insurance that makes up the U.S economy? \n"
q8 = q8 + "Possible answers \n"
q8 = q8 + "1 - 35% \n"
q8 = q8 + "2 - 5% \n"
q8 = q8 + "3 - 57% \n"
q8 = q8 + "4 - 85% \n"
q8 = q8 + "write down your number below \n"

q9 = "Here is the ninth question \n"
q9 = q9 + "Question 9 - The healthcare sector employs what percentage of American workers? \n"
q9 = q9 + "Possible answers \n"
q9 = q9 + "1 - 11% \n"
q9 = q9 + "2 - 20% \n"
q9 = q9 + "3 - 75% \n"
q9 = q9 + "4 - 44% \n"
q9 = q9 + "write down your number below \n"

q10 = "Here is the tenth question \n"
q10 = q10 + "Question 10 - What percentage of Americans have their health insurance covered by their employer  \n"
q10 = q10 + "Possible answers \n"
q10 = q10 + "1 - 97% \n"
q10 = q10 + "2 - 49% \n"
q10 = q10 + "3 - 34% \n"
q10 = q10 + "4 - 4% \n"
q10 = q10 + "write down your number below \n"
########### QUESTION LIST END ##############

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
answers = [3, 4, 1, 2, 2, 3, 4, 2, 1, 2]

switchTurn = 0


def Josh_function2():
    print(sum(player2points))


def Josh_function1():
    print(sum(player1points))


count = 1
for index in range(len(questions)):
    print(questions[index])

    answerInput = int(input())

    if answerInput == answers[index]:
        print("You got the question right")
        print("You earned 100 points")

        if count % 2 == 1:
            player1points.append(100)

        else:
            player2points.append(100)


    else:
        print("You got the question wrong")
        print("You earned 0 points")

        if count % 2 == 1:
            player1points.append(0)
        else:
            player2points.append(0)

    count = count + 1

finalscore1 = (sum(player1points))
finalscore2 = (sum(player2points))

print("Player 1 has " + str(finalscore1) + " points")
print("Player 2 has " + str(finalscore2) + " points")
Josh_function2()
Josh_function1()


if finalscore1 > finalscore2:
    print("Player1 won")

elif finalscore2 > finalscore1:
    print("Player2 won")

elif finalscore1 == finalscore2:
    print("Tie game")


