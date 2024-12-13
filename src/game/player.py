from random import randint

class Player:
    name: str
    life: int = 100
    damage: int = 10
    defense: int

    @property
    def is_alive(self) -> bool:
        return self.life > 0

    def __init__(self, name: str):
        self.name = name
        self.defense = randint(0, 25)

    def take_damage(self, damage: int) -> int:
        damage -= (damage * self.defense) / 100
        damage = int(damage)

        self.life -= damage

        return damage

    def __str__(self) -> str:
        return f"Giocatore: {self.name} (Life: {self.life}%)"
