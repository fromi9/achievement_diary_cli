import os
from datetime import datetime
from colorama import init, Fore, Style
import csv
import shutil

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

def export_to_csv():
    entries = read_entries()
    if not entries:
        print(Fore.YELLOW + "No entries to export.")
        return

    with open("achievement.csv", "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Achievement"])

        for entry in entries:
            lines = entry.strip().split("\n")
            if not lines:
                continue
            date = lines[0].strip("[]")
            text = " ".join(lines[1:])
            writer.writerow([date, text])
    print(Fore.GREEN + "Achievements exported to achievements.csv")


def backup_file():
    if os.path.exists(file_ach):
        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        shutil.copy(file_ach, backup_name)
        print(Fore.YELLOW + f"Backup created: {backup_name}")

def sorted_achievement():
    entries = read_entries()

    if not entries:
        print(Fore.YELLOW + "There are no entries yet.")
        return

    def extract_date(entry):
        lines = entry.strip().split("\n")
        if lines:
            date_str = lines[0].strip("[]")
            try:
                return datetime.strptime(date_str, "%d.%m.%Y")
            except ValueError:
                return datetime.min
        return datetime.min

    entries.sort(key=extract_date)

    print(Style.BRIGHT + "\n***SORTED ENTRIES***\n")

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

def search_achievements():
    print(Style.BRIGHT + "\n***SEARCH***")
    keyword = input("Enter a word to search: ").strip()

    if keyword:
        entries = read_entries()
        matches = [entry for entry in entries if keyword.lower() in entry.lower()]
        
        if matches:
            print("\n--- Search Results ---\n")
            for match in matches:
                print(match)
                print("-" * 30)
        else:
            print(Fore.YELLOW + "No entries found.")
            print()
    else:
        print(Fore.RED + "Empty input. Try again")

def delete_entries():
    entries = read_entries()

    if not entries:
        print(Fore.YELLOW + "No entries to delete.")
        return
    
    for idx, entry in enumerate(entries):
        print(f"{idx}:")
        print(entry)
        print("-" * 30)

    try:
        entry_numbers = input("Enter the numbers of the entries to delete, separated by commas: ").strip()
        entry_numbers = [int(num.strip()) for num in entry_numbers.split(",")]
    except ValueError:
        print(Fore.RED + "Invalid input. Must be numbers separated by commas.")
        return
    
    valid_entries = [entry for idx, entry in enumerate(entries) if idx not in entry_numbers]
    removed_entries = [entries[idx] for idx in entry_numbers if 0 <= idx < len(entries)]

    if removed_entries:
        with open(file_ach, "w", encoding="utf-8") as file:
            file.write("\n\n".join(valid_entries) + "\n")
        print()
        print(Fore.RED + "Entries DELETED:")
        for removed in removed_entries:
            print(Fore.CYAN + removed)
    else:
        print(Fore.RED + "Invalid entry numbers.")

    
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
        print(Style.BRIGHT + "***ACHIEVEMENT DIARY***")
        print("1 - Add achievement")
        print("2 - View achievements")
        print("3 - Search achievements")
        print("4 - Delete entry")
        print("5 - Sorted achievements")
        print("6 - Export to CSV")
        print("7 - Exit")

        choice = input(Style.BRIGHT + "Enter choice: ")

        if choice == "1":
            add_achievement()
            
        elif choice == "2":
            view_achievements()

        elif choice == "3":
            search_achievements()
        
        elif choice == "4":
            delete_entries()

        elif choice == "5":
            sorted_achievement()

        elif choice == "6":
            export_to_csv()

        elif choice == "7":
            print("BYE")
            break
        else:
            print(Fore.RED + "Wrong input.")



if __name__ == "__main__":
    main()    