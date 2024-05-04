class Player:
    def __init__(self, name, health, strength, agility):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility

    def attack(self, enemy):
        # Логика атаки персонажа
        pass

    def take_damage(self, damage):
        # Логика получения урона
        pass

    def use_item(self, item):
        # Логика использования предмета
        pass
