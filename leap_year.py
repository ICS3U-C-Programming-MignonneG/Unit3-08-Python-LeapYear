#!/usr/bin/env python3
# Created by: Mignonne
# Created on Oct 30 2026
# This program checks if user_input is a leap year or not


def main():
    # Asks the user to enter a year
    user_input_as_string = input("Enter a year: ")

    try:
        user_input = int(user_input_as_string)

        # Nested if statements to check leap year conditions
        if user_input % 4 == 0:
            if user_input % 100 == 0:
                if user_input % 400 == 0:
                    print(f"{user_input} is a leap year.")
                else:
                    print(f"{user_input} is not a leap year.")
            else:
                print(f"{user_input} is a leap year.")
        else:
            print(f"{user_input} is not a leap year.")

    except ValueError:
        print(f"'{user_input_as_string}' is not a valid integer.")


if __name__ == "__main__":
    main()
