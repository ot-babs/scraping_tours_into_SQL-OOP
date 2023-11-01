

class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        age = current_year - self.birth_year
        return age
        pass


if __name__ == "__main__":
    user = User("John", 1999)
    age = user.age(2023)

    print(age)
    print(user.get_name())
