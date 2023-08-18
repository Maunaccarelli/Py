import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=15)
        self.inventory = []
        self.skills = [
            Skill("Fireball", 20, 10),
            Skill("Heal", 0, -30)
        ]

class Enemy(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)

class Item:
    def __init__(self, name, healing):
        self.name = name
        self.healing = healing

class Skill:
    def __init__(self, name, damage, healing):
        self.name = name
        self.damage = damage
        self.healing = healing

class RPGGame:
    def __init__(self):
        self.player = Player(input("Enter your character's name: "))
        self.enemies = [
            Enemy("Goblin", 30, 5),
            Enemy("Orc", 50, 8)
        ]
        self.items = [
            Item("Health Potion", 20),
            Item("Super Health Potion", 50)
        ]

    def battle(self):
        print(f"Welcome, {self.player.name}! Get ready for an epic adventure!")
        while self.player.is_alive():
            enemy = random.choice(self.enemies)
            print(f"A wild {enemy.name} appears!")
            while enemy.is_alive() and self.player.is_alive():
                action = input("Do you want to (a)ttack, (u)se skill, (i)tem, or (f)lee? ").lower()
                if action == "a":
                    self.attack(enemy)
                elif action == "u":
                    self.use_skill(enemy)
                elif action == "i":
                    self.use_item()
                elif action == "f":
                    if self.try_flee():
                        print(f"{self.player.name} fled from battle!")
                        break
                self.enemy_turn(enemy)
                if not enemy.is_alive():
                    self.player.inventory.append(random.choice(self.items))
                    break

    def attack(self, enemy):
        player_damage = random.randint(self.player.attack - 3, self.player.attack + 3)
        enemy.take_damage(player_damage)
        print(f"You dealt {player_damage} damage to {enemy.name}.")

    def use_skill(self, enemy):
        print("Skills:")
        for i, skill in enumerate(self.player.skills, start=1):
            print(f"{i}. {skill.name}")
        choice = int(input("Select a skill to use (1, 2, ...): ")) - 1
        if 0 <= choice < len(self.player.skills):
            skill = self.player.skills[choice]
            if skill.damage > 0:
                enemy.take_damage(skill.damage)
                print(f"You used {skill.name} and dealt {skill.damage} damage to {enemy.name}.")
            if skill.healing < 0:
                self.player.take_damage(skill.healing)
                print(f"You used {skill.name} and healed for {-skill.healing} HP.")
        else:
            print("Invalid choice.")

    def use_item(self):
        if not self.player.inventory:
            print("Your inventory is empty.")
            return
        print("Inventory:")
        for i, item in enumerate(self.player.inventory, start=1):
            print(f"{i}. {item.name} (+{item.healing} HP)")
        choice = int(input("Select an item to use (1, 2, ...): ")) - 1
        if 0 <= choice < len(self.player.inventory):
            self.player.use_item(self.player.inventory[choice])
        else:
            print("Invalid choice.")

    def try_flee(self):
        flee_chance = random.random()
        if flee_chance < 0.5:
            return True
        return False

    def enemy_turn(self, enemy):
        enemy_damage = random.randint(enemy.attack - 2, enemy.attack + 2)
        self.player.take_damage(enemy_damage)
        print(f"{enemy.name} dealt {enemy_damage} damage to you.")

if __name__ == "__main__":
    game = RPGGame()
    game.battle()