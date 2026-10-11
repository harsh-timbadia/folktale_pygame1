import random
room = 'starting'
points = 0
inventory = []
game_running = True

while game_running:
    if room == 'starting' :
        print("\n--- MAIN HALL---")
        print("you are in the main hall. to the left is the arcade room")
        print("Enter '1' to go to the arcade room, or '2' to quit the game.")

        answer = input("> ")

        if answer == "1":
            room = 'arcade'
        elif answer == "2":
            print("Thanks for playing!")
            game_running = False
        else:
            print("Invalid input. Please enter '1' or '2'.")
    elif room == 'arcade':
        print("\n---ARCADE ROOM---")
        print(f"Tokens: {points} | Inventory: {inventory}")
        print("1: play a maths quiz (win 10 pints)")
        print("2: visit the prize shop")
        print("3: go back to the main hall")

        answer = input("> ")

        if answer == "1":
            room = 'maths_quiz'
        elif answer == "2":
            room = 'prize_shop'
        elif answer == "3":
            room = 'starting'
        else:
            print("Invalid input. Please enter '1', '2', or '3'.")

    elif room == "maths_quiz":
        print("\n---MATHS QUIZ---")
        num1 = random.randint(1,15)
        num2 = random.randint(1,15)
        operator = random.choice(['+', '-', '*'])

        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2

        print(f"What is {num1} {operator} {num2}?")
        answer = input("your answer: ")

        if answer == str(correct_answer):
            print("Correct! You win 10 points.")
            points += 10
        else:
            print("Incorrect answer. The correct answer was", correct_answer)

        room = 'arcade'

    elif room == "prize_shop":
        print("\n---PRIZE SHOP---")
        print(f"you have {points} points.")
        print("1: buy a magic sword (20 points)")
        print("2: buy a healing potion (10 points)")
        print("3: leave shop")

        choice = input("> ")

        if choice == "1":
            if "magic sword" in inventory:
                print("You already own a magic sword.")
            elif points >= 20:
                points -= 20
                inventory.append("magic sword")
                print("You bought a magic sword! ⚔")
            else:
                print("You don't have enough points to buy a magic sword.")

        elif choice == "2":
            if "healing potion" in inventory:
                print("You already own a healing potion.")
            elif points >= 10:
                points -= 10
                inventory.append("healing potion")
                print("You bought a healing potion! 🧪")
            else:
                print("You don't have enough points to buy a healing potion.")
        elif choice == "3":
            room = 'leaving the shop'
        else:
            print("invalid choice")

        room = "arcade"
        
