from random import randint

from .player import Player


class Game:
    current_index: int

    @property
    def current_player(self) -> Player:
        return self.players[self.current_index]

    is_running: bool = True

    players: list[Player]

    def __init__(self, player_names: list[str]):
        total_players = len(player_names)

        self.current_index = randint(0 , total_players - 1)
        self.players = []

        for name in player_names:
            player = Player(name)

            self.players.append(player)

    def are_players_alive(self) -> bool:
        players_alive = 0
        for player in self.players:
            if player.is_alive:
                players_alive += 1
        
        return players_alive > 1

    def attack_player(self, target_index: int) -> int:
        randomness = randint(0, 10) - 5
        damage = self.current_player.damage + randomness

        target_player = self.players[target_index]
        taken_damage = target_player.take_damage(damage)

        return taken_damage

    def next_turn(self) -> bool:
        while True:
            self.current_index = (self.current_index + 1) % len(self.players)
            if self.current_player.is_alive:
                self.is_running = self.are_players_alive()

                return self.is_running

    def __str__(self) -> str:
        value = "Stato partita:"

        for player in self.players:
            value += f"\n - {player}"

        return value
