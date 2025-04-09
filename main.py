import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

file_ach = "achievement.txt"

def save_entry(data, text):
    with open(file_ach, "a", encoding="utf-8") as file:
        file.write(f"[{data}]\n{text}\n\n")

def read_entries():
    if not os.path.exists(file_ach):
        return []

    with open(file_ach, "r", encoding="utf-8") as file:
        raw = file.read().strip()
        entries = raw.split("\n\n")
        return entries

def add_achievement():
    date = input("Enter a date (or press ENTER for today): ").strip()
    if not date:
        date = datetime.now().strftime("%d.%m.%Y")  # Без цвета
        print(Fore.CYAN + f"[{date}]" + Style.RESET_ALL)
    print("Write what you did today (press ENTER twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)

    save_entry(date, text)
    print(Fore.GREEN + "Saved")
    
def view_achievements():
    entries = read_entries()

    if not entries:
        print(Fore.YELLOW + "There are no entries yet.")
        return

    print(Style.BRIGHT + "\n***ALL ENTRIES***\n")

    for entry in entries:
        lines = entry.strip().split("\n")
        if not lines:
            continue
        date_line = lines[0]
        content_lines = lines[1:]
        print(Fore.CYAN + date_line)
        for line in content_lines:
            print(Fore.WHITE + line)
        print()

    
def main():
    while True:
        print(Style.BRIGHT + "*** ACHIEVEMENT DIARY ***")
        print("1 - Add achievement")
        print("2 - View achievements")
        print("3 - Exit")

        choice = input(Style.BRIGHT + "Enter choice: ")

        if choice == "1":
            add_achievement()
            
        elif choice == "2":
            view_achievements()

        elif choice == "3":
            print("BYE")
            break
        else:
            print(Fore.RED + "Wrong input.")


if __name__ == "__main__":
    main()    