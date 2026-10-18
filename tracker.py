
import json

def save_matches(matches):
    with open("matches.json", "w") as f:
        json.dump(matches, f, indent=4)


def load_matches():
    try:
        with open("matches.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_match(matches):
    hero = input("Enter hero played: ")
    result = input("Enter result (Win or Loss): ").strip().capitalize()

    if result not in ("Win", "Loss"):
        print("Invalid result.")
        return False

    try:
        kills = int(input("Enter number of kills: "))
        deaths = int(input("Enter number of deaths: "))
        assists = int(input("Enter number of assists: "))
    except ValueError:
        print("Please enter valid numbers.")
        return False

    if kills < 0 or deaths < 0 or assists < 0:
        print("Statistics cannot be negative.")
        return False

    match = {
        "Hero": hero,
        "Result": result,
        "Kills": kills,
        "Deaths": deaths,
        "Assists": assists
    }

    matches.append(match)
    print("Match added successfully!")
    return True


def view_matches(matches):
    if len(matches) == 0:
        print("No matches recorded")
    else:
        for i in range(len(matches)):
            match = matches[i]
            print(
                f"Match {i + 1}: {match['Hero']} | {match['Result']} | "
                f"{match['Kills']}/{match['Deaths']}/{match['Assists']}"
            )


def view_statistics(matches):
    total_kills = 0
    total_deaths = 0
    total_assists = 0
    total_wins = 0
    total_losses = 0

    if len(matches) == 0:
        print("No matches recorded")
        return

    for i in range(len(matches)):
        total_kills += matches[i]["Kills"]
        total_deaths += matches[i]["Deaths"]
        total_assists += matches[i]["Assists"]

        if matches[i]["Result"] == "Win":
            total_wins += 1
        elif matches[i]["Result"] == "Loss":
            total_losses += 1

    print("Total kills =", total_kills)
    print("Total deaths =", total_deaths)
    print("Total assists =", total_assists)

    if total_deaths == 0:
        print("KDA = N/A (zero deaths)")
    else:
        print("KDA =", (total_kills + total_assists) / total_deaths)

    print("Total wins =", total_wins)
    print("Total losses =", total_losses)

    total_games = total_wins + total_losses
    if total_games > 0:
        print(f"Win % = {total_wins / total_games * 100:.2f}%")
    else:
        print("Win % = N/A")


matches = load_matches()

while True:
    print("\n===== DEADLOCK TRACKER =====")
    print("1. Add a match")
    print("2. View matches")
    print("3. View statistics")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a match...")
        if add_match(matches):
            save_matches(matches)

    elif choice == "2":
        print("Viewing matches...")
        view_matches(matches)

    elif choice == "3":
        print("Viewing statistics...")
        view_statistics(matches)

    elif choice == "4":
        print("Exiting...")
        save_matches(matches)
        break

    else:
        print("Invalid option.")
