class Game_bot:
    def __init__(self, character, health, gender): #bonus, bust, strength
        self._character = character
        self.health = health
        self.gender = gender

    def shoot(self):
            return "I can shoot"

    def get_character(self):
            return f"Hello! My class is {self._character}"



class Shooter(Game_bot):
    def __init__(self, character, health, gender, style): # инкапсулировались атрибуты
        super().__init__(character, health, gender)  # ссылка на суперкласс
        self.style = style  # расширяем на одно значение


    def role(self):
        return "To support allies and weaken rivals."

    # Переиспользование метода из родительского класса
    def shoot(self):
            return "I can shoot a bow"



class Sniper(Shooter):
    def __init__(self, character, health, gender, style, specializations): # инкапсулировались атрибуты
        super().__init__(character, health, gender, style)  # ссылка на суперкласс
        self.specializations = specializations  # расширяем на одно значение


    def role(self):
        return "To support allies and weaken rivals."

    # Переиспользование метода из родительского класса
    def shoot(self):
            return "I can shoot a bow"

    def skill(self):
            return "I can change position and just wait for the perfect moment to strike, avoiding damage"

    def set_character(self, new_character):
        self._character = new_character #Protected (добавила подчеркивание)

# bot1 = Game_bot("Shooter", 100, "Shoot")
# print(bot1._character)
# print(bot1.get_character())
# print(bot1.health)
# print(bot1.shoot())
#
# bot2 = Shooter("Shooter", 99, "Male", "targets_from_a_distance")
# print(bot2.shoot())
# print(bot2.get_character())
bot3 = Sniper("Shooter", 99, "Female", "Targets_from_a_distance", "Change the mount and avoiding damage.")
print(bot3.get_character())
print(bot3.set_character("Centaur 3"))
print(bot3.get_character())
