import time


def countdown_timer():
    while True:
        try:
            start_num = int(input("Enter a starting number: "))
            if start_num <= 0:
                print("Please enter a number greater than 0.")
                return

            final_message = input("Enter your final message: ")

            for count in range(start_num, 0, -1):
                print(count)
                time.sleep(1)

            print(final_message)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask the user if they want to run again
        repeat = input("Do you want to run the time again? (yes/no): ").strip()
        if repeat not in ['yes', 'y']:
            print("Goodbye!")
            break


if __name__ == "__main__":
    countdown_timer()
