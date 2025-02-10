import time

class GameManager:
    def __init__(self):
        self.logged_in = False
        self.username = None
        self.friends = []

    def login(self):
        print("\nWelcome to Game Manager-Friend!")
	print("\nIn this software you add or delete your game friends,")
        print("Please log in to continue.\n")
        while not self.logged_in:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username and password:  # Simple login validation
                self.username = username
                self.logged_in = True
                print(f"\nLogin successful! Welcome, {self.username}.\n")
            else:
                print("Invalid credentials. Please try again.\n")

    def add_friend(self):
        friend_name = input("Enter your friend's username: ")
        if friend_name and friend_name not in self.friends:
            self.friends.append(friend_name)
            print(f"\n{friend_name} has been added to your friend list!\n")
        else:
            print("\nInvalid entry or friend already added.\n")

    def remove_friend(self):
        if not self.friends:
            print("\nYour friend list is empty. Add some friends first!\n")
            return

        while True:  # Keep asking until a valid number is entered
            print("\nYour Friends List:")
            for index, friend in enumerate(self.friends, start=1):
                print(f"  {index}. {friend}")

            choice = input("\nEnter the number of the friend you want to remove: ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.friends):
                    removed_friend = self.friends.pop(choice - 1)
                    print(f"\n{removed_friend} has been removed from your friend list!\n")
                    break  # Exit loop after successful removal
                else:
                    print("\nInvalid number. Please enter a valid number from the list.\n")
            else:
                print("\nInvalid input. Please enter a number.\n")

    def list_friends(self):
        print("\nFriends List:")
        if self.friends:
            for friend in self.friends:
                print(f"  - {friend}")
        else:
            print("  No friends added yet.")
        print()

    def help_page(self):
        print("\n----------------- HELP -----------------")
        print("COMMANDS:")
        print("  Enter  -> Show a welcome message")
        print("  friend -> Add a friend")
        print("  list   -> Show all added friends")
        print("  remove -> Remove a friend from the list")
        print("  help   -> Show this help menu")
        print("  quit   -> Exit the program")
        print("----------------------------------------\n")

    def run(self):
        self.login()
        print("\nGame Manager CLI - Type 'help' to see available commands.\n")

        while True:
            command = input("[Enter/friend/list/remove/help/quit]: ").strip().lower()

            if command == "":
                print(f"\nWelcome, {self.username}! Enjoy your gaming time.\n")
		print("\nThe version you are using now only supports the friend system and does not have a game management system.")
            elif command == "friend":
                self.add_friend()
            elif command == "list":
                self.list_friends()
            elif command == "remove":
                self.remove_friend()
            elif command == "help":
                self.help_page()
            elif command in ["q", "quit"]:
                print("\nGoodbye! Have a great day.\n")
                break
            else:
                print("\nInvalid command. Type 'help' for a list of commands.\n")

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()
