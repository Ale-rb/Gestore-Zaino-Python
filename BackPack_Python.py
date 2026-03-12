import os

class Backpack:

    def __init__(self):
        # Set up the file path correctly
        self.current_folder = os.path.dirname(__file__)
        self.file_path = os.path.join(self.current_folder, "backpack_data.txt")
        self.backpack_list = []
        
        # Load existing data
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    self.backpack_list.append(line.strip())
        except FileNotFoundError:
            print("No saved data found. A new file will be created upon saving.")
            
    def save_to_disk(self):
        """Saves the entire list to the text file."""
        with open(self.file_path, "w") as file:
            for item in self.backpack_list:
                file.write(item + "\n")
        print("Data successfully saved to disk.")
        
    def add_subject(self, subject):
        self.backpack_list.append(subject)
        # Immediate append to file for safety
        with open(self.file_path, "a") as file:
            file.write(subject + "\n")
    
    def remove_subject(self, subject):
        if subject in self.backpack_list:
            self.backpack_list.remove(subject)
            self.save_to_disk() # Refresh the file
            print(f"Subject: {subject} removed.")
            print("Updated list:")
            self.show_backpack()
        else:
            print("Subject not found in backpack.")
            
    def show_backpack(self):
        if not self.backpack_list:
            print("The backpack is empty.")
        else:
            for item in self.backpack_list:
                print(f"- {item}")

def main():
    my_backpack = Backpack()
    while True:
        print("\n----- MAIN MENU -----")
        print("1. Add Subject")
        print("2. Show Backpack")
        print("3. Remove Subject")
        print("4. Save and Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            subject = input("Enter the subject to add: ")
            my_backpack.add_subject(subject)
            print(f"Added: {subject}")
            
        elif choice == "2":
            print("\nYour Subjects:")
            my_backpack.show_backpack()
            
        elif choice == "3":
            subject = input("Which subject do you want to remove?: ")
            my_backpack.remove_subject(subject)
            
        elif choice == "4":
            my_backpack.save_to_disk()
            print("Exiting system...")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    main()
