
import random

while True:

    print(f"======================================")
    print(f"          PYTHON TREASURE HUNT")
    print(f"======================================")

    name = input("Enter your name: ")

    print(f"\nWelcome, {name}!")
    print(f"Your adventure begins now!")
    print(f"\nCollect gold coins by answering Python questions.")
    print(f"You will explore three different worlds.")
    print(f"Each correct answer gives you 10 gold coins.")
    print(f"Answer only T for True or F for False.")

    input(f"\nPress Enter to start your adventure...")

    # QUESTIONS

    prelim = [
        ["Python is a programming language.", "T", "Python is used to create programs."],
        ["The print() function displays output.", "T", "print() displays information on the screen."],
        ["Comments start with the # symbol.", "T", "The # symbol is used for comments."],
        ["A variable stores data.", "T", "Variables are used to store information."],
        ["Python uses the word 'integer' as a data type.", "F", "The correct data type is int."],
        ["The input() function gets information from the user.", "T", "input() allows users to enter information."],
        ["A string stores text.", "T", "Strings contain letters, words, or symbols."],
        ["The + operator can add numbers.", "T", "The + operator performs addition."],
        ["Python is only used for games.", "F", "Python can be used for websites, apps, and more."],
        ["A constant is a value that should not change.", "T", "Constants are intended to remain unchanged."]
    ]

    midterm = [
        ["An if statement is used for decision-making.", "T", "if checks whether a condition is true."],
        ["The else statement runs when the if condition is false.", "T", "else handles the other condition."],
        ["The == operator checks equality.", "T", "== compares two values."],
        ["The > operator means less than.", "F", "> means greater than."],
        ["The and operator requires both conditions to be true.", "T", "and is true when both conditions are true."],
        ["The or operator requires both conditions to be true.", "F", "or needs at least one true condition."],
        ["An elif statement checks another condition.", "T", "elif means else if."],
        ["The != operator means not equal.", "T", "!= checks if values are different."],
        ["An if statement cannot be used with else.", "F", "if and else can be used together."],
        ["Logical operators help combine conditions.", "T", "and, or, and not are logical operators."]
    ]

    finals = [
        ["A loop repeats a set of instructions.", "T", "Loops are used to repeat code."],
        ["A for loop can repeat code a certain number of times.", "T", "for loops can go through a sequence."],
        ["A while loop repeats while its condition is true.", "T", "while checks its condition before repeating."],
        ["The range(5) function produces numbers from 0 to 4.", "T", "range(5) produces 0, 1, 2, 3, 4."],
        ["A loop can never stop.", "F", "A loop stops when its condition becomes false or it finishes."],
        ["The break statement can stop a loop.", "T", "break immediately ends the loop."],
        ["The continue statement skips the current iteration.", "T", "continue moves to the next iteration."],
        ["A for loop is always an infinite loop.", "F", "A for loop usually stops after its sequence ends."],
        ["A while loop can become infinite if its condition never becomes false.", "T", "The condition must eventually become false to stop normally."],
        ["Loops help avoid writing the same code many times.", "T", "Loops make repeated tasks easier."]
    ]

    worlds = [prelim, midterm, finals]

    world_names = ["PRELIM WORLD", "MIDTERM WORLD", "FINALS WORLD"]

    rewards = ["PYTHON EXPLORER", "PYTHON ADVENTURER", "PYTHON MASTER"]

    total_score = 0
    gold_coins = 0
    total_correct = 0
    inventory = []

    # THREE WORLDS

    for w in range(3):

        print(f"\n======================================")
        print(f"          {world_names[w]}")
        print(f"======================================")

        print(f"Get ready, {name}!")

        random.shuffle(worlds[w])

        world_score = 0

        for q in range(10):

            question = worlds[w][q]

            print(f"\nQuestion {q + 1} of 10")
            print(f"{question[0]}")

            answer = input(f"Your answer (T/F): ").upper()

            while answer != "T" and answer != "F":
                print(f"Invalid answer! Please enter T or F.")
                answer = input(f"Your answer (T/F): ").upper()

            if answer == question[1]:

                print(f"\nCorrect answer!")
                world_score += 1
                total_correct += 1
                gold_coins += 10

            else:

                print(f"\nWrong answer!")
                print(f"Correct answer: {question[1]}")

            print(f"Explanation: {question[2]}")
            print(f"Gold Coins: {gold_coins}")

        # WORLD SUMMARY

        total_score += world_score

        print(f"\n======================================")
        print(f"          WORLD COMPLETED!")
        print(f"======================================")

        print(f"Correct Answers: {world_score} / 10")
        print(f"Total Score: {total_score} / 30")

        print(f"\nTREASURE CHEST UNLOCKED!")
        print(f"You are now: {rewards[w]}")

        print(f"Gold Coins: {gold_coins}")

        input(f"\nPress Enter to continue to the next world...")


    print(f"\n======================================")
    print(f"       ALL WORLDS COMPLETED!")
    print(f"======================================")

    print(f"Congratulations, {name}!")
    print(f"You have unlocked the TREASURE SHOP!")

    print(f"\n======================================")
    print(f"            TREASURE SHOP")
    print(f"======================================")

    print(f"AVAILABLE ITEMS:")
    print(f"1. Maxx - 100 coins")
    print(f"2. Snowbear 100 coins")
    print(f"3. Vfresh - 100 coins")
    print(f"4. Exit Shop")

    shop = ""

    while shop != "4":

        print(f"\nYour Gold Coins: {gold_coins}")
        shop = input(f"Choose an item (1-4): ")

        if shop == "1":

            if gold_coins >= 100:
                gold_coins -= 100
                inventory.append("Maxx")
                print(f"You bought a Maxx!")

            else:
                print(f"Not enough gold coins!")

        elif shop == "2":

            if gold_coins >= 100:
                gold_coins -= 100
                inventory.append("Snow bear")
                print(f"You bought a Snowbear!")

            else:
                print(f"Not enough gold coins!")

        elif shop == "3":

            if gold_coins >= 100:
                gold_coins -= 100
                inventory.append("Vfresh")
                print(f"You bought a Vfresh!")

            else:
                print(f"Not enough gold coins!")

        elif shop == "4":

            print(f"\nThank you for visiting the Treasure Shop!")

        else:

            print(f"Invalid choice! Please choose from 1 to 4.")


    print(f"\n======================================")
    print(f"         YOUR INVENTORY")
    print(f"======================================")

    if len(inventory) == 0:
        print(f"No items purchased.")

    else:
        for item in inventory:
            print(f"- {item}")

    # FINAL SCORE REPORT

    percentage = (total_correct / 30) * 100

    print(f"\n======================================")
    print(f"          FINAL SCORE REPORT")
    print(f"======================================")

    print(f"Player Name: {name}")
    print(f"Correct Answers: {total_correct} / 30")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Remaining Gold Coins: {gold_coins}")

    if total_correct >= 27:
        achievement = "PYTHON LEGEND"

    elif total_correct >= 20:
        achievement = "PYTHON ADVENTURER"

    elif total_correct >= 10:
        achievement = "PYTHON EXPLORER"

    else:
        achievement = "CODE BEGINNER"

    print(f"\nFINAL ACHIEVEMENT: {achievement}")

    print(f"\nThank you for playing Python Treasure Hunt!")

    # PLAY AGAIN

    print(f"\n======================================")

    replay = input(f"Do you want to play again? (Y/N): ").upper()

    while replay != "Y" and replay != "N":
        print(f"Invalid choice!")
        replay = input(f"Please enter Y or N: ").upper()

    if replay == "N":
        print(f"\nThank you for playing!")
        print(f"Goodbye, {name}!")
        break
