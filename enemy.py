class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        # Логика атаки врага
        pass

    def take_damage(self, damage):
        # Логика получения урона
        pass
