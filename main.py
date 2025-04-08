import os
from datetime import datetime

file_ach = "achievement.txt"

def save_entry(data, text):
    with open(file_ach, "a", encoding="utf-8") as file:
        file.write(f"[{data}]\n{text}\n\n")

def read_entries():
    if not os.path.exists(file_ach):
        return "There are no entries yet"
    with open(file_ach, "r", encoding="utf-8") as file:
        return file.read()

def add_achievement():
    date = input("Enter a date (or press ENTER for today): ").strip()
    if not date:
        date = datetime.now().strftime("%d.%m.%Y")
    print("Write what you did today (press ENTER twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)

    save_entry(date, text)
    print("Saved")

def view_achievements():
    entries = read_entries()
    print("\n***ALL ENTRIES***")
    print(entries)
    
def main():
    while True:
        print("*** ACHIEVEMENT DIARY ***")
        print("1 - Add achievement")
        print("2 - View achievements")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_achievement()
            
        elif choice == "2":
            view_achievements()

        elif choice == "3":
            print("BYE")
            break
        else:
            print("Wrong input.")


if __name__ == "__main__":
    main()    