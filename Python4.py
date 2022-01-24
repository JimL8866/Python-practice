def menu():
    user_choice = input("Please choose 1 for addition, 2 for subtraction, 3 for termination\n")
    try:
        if int(user_choice) == 1:
            num1 = int(input("please put a number\n"))
            num2 = int(input("please put another number\n"))
            add(num1, num2)
        elif int(user_choice) == 2:
            num1 = int(input("please put a number\n"))
            num2 = int(input("please put another number\n"))
            sub(num1, num2)
        elif int(user_choice) == 3:
            print("Program Terminated.Goodbye")
            exit()
        else:
            print("You've chosen wrong numer. Please try again.")
    except ValueError:
        print("Please put number only. Please try again.")


def add(num1, num2):
    print(f"Addition result is {num1 + num2}")


def sub(num1, num2):
    print(f"subtraction result is {num1 - num2}")


while True:
    menu()