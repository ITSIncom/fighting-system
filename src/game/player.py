from random import randint


class Player:
    name: str
    life: int
    damage: int
    defense: int

    @property
    def is_alive(self) -> bool:
        return self.life > 0

    def __init__(self, name: str, life = 100, damage = 10, defense = None):
        self.name = name
        self.life = life
        self.damage = damage
        self.defense = randint(0, 25) if defense is None else defense

    def take_damage(self, damage: int) -> int:
        damage -= (damage * self.defense) / 100
        damage = int(damage)

        self.life -= damage

        return damage

    def __str__(self) -> str:
        return f"Giocatore: {self.name} (Life: {self.life}%)"
