class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player = {"name": name, "position": position, "number": number, "age": age, "nationality": nationality}
        self.players.append(player)

    def remove_player(self, number):
        self.players = [p for p in self.players if p.get("number") != number]

    def update_player(self, number, key, value):
        for p in self.players:
            if p.get("number") == number:
                p[key] = value
                break

    def display_team_info(self):
        print("Team:", self.team_name)
        print("Coach:", self.coach)
        print("Players:")
        if not self.players:
            print("No players yet, add some!")
        else:
            for p in self.players:
                print(f"#{p['number']} - {p['name']} | {p['position']} | Age: {p['age']} | {p['nationality']}")

    def display_player_info(self, number):
        for p in self.players:
            if p.get("number") == number:
                print("Player info:")
                for k, v in p.items():
                    print(f"{k.capitalize()}: {v}")
                return
        print("Player not found :(")


if __name__ == "__main__":
    team = FootballTeam("Loko FC", "Vakhtang Vardi")
    team.add_player("George", "Defense", 1, 24, "Georgian")
    team.add_player("Manuchar", "Midfield", 10, 27, "Georgian")
    team.display_team_info()
    team.update_player(10, "goals", 1)
    team.display_player_info(10)
    team.remove_player(1)
    print("\nUpdated team info:")
    team.display_team_info()
