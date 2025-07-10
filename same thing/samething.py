class Player:
    id_counter = 1

    def __init__(self, name, position, jersey_number, age, nationality):
        self.id = Player.id_counter
        Player.id_counter += 1
        self.name = name
        self.position = position
        self.__jersey_number = jersey_number
        self.__age = age
        self.nationality = nationality
        self.matches_played = 0
        self.goals_scored = 0

    def __str__(self):
        return f"Player {self.id}: {self.name}, {self.position}, Jersey: {self.__jersey_number}, Age: {self.__age}, {self.nationality}, Matches: {self.matches_played}, Goals: {self.goals_scored}"

    def display_info(self):
        return self.__str__()

    def update_info(self, key, value):
        if key == "name":
            self.name = value
        elif key == "position":
            self.position = value
        elif key == "jersey_number":
            self.__jersey_number = value
        elif key == "age":
            self.__age = value
        elif key == "nationality":
            self.nationality = value
        elif key == "matches_played":
            self.matches_played = value
        elif key == "goals_scored":
            self.goals_scored = value


class Coach:
    def __init__(self, name, experience):
        self.name = name
        self.__experience = experience

    def __str__(self):
        return f"Coach: {self.name}, Experience: {self.__experience} years"

    def display_info(self):
        return self.__str__()

    def update_experience(self, new_experience):
        self.__experience = new_experience


class Team:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        if len(self.players) >= 25:
            print("Team is full. Can't add more than 25 players.")
        else:
            self.players.append(player)

    def search_player(self, player_id):
        for p in self.players:
            if p.id == player_id:
                return p
        return None

    def update_player(self, player_id, key, value):
        player = self.search_player(player_id)
        if player:
            player.update_info(key, value)
        else:
            print("Player not found.")

    def remove_player(self, player_id):
        self.players = [p for p in self.players if p.id != player_id]

    def __str__(self):
        players_str = "\n".join([str(p) for p in self.players])
        return f"Team: {self.name}\n{str(self.coach)}\nPlayers:\n{players_str}"

    def display_team_info(self):
        print(self.__str__())


if __name__ == "__main__":
    coach = Coach("John Doe", 5)
    team = Team("Loko FC", coach)
    p1 = Player("George", "Defense", 1, 24, "Georgian")
    p2 = Player("Manuchar", "Midfield", 10, 27, "Georgian")
    team.add_player(p1)
    team.add_player(p2)
    team.display_team_info()
    team.update_player(2, "goals_scored", 1)
    print("\nAfter updating player 2 stats:")
    player = team.search_player(2)
    if player:
        print(player)
    team.remove_player(1)
    print("\nAfter removing player 1:")
    team.display_team_info()
sq