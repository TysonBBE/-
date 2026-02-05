
Кейс задача - 1 
Сумма отрицательных элементов между максимальным и минимальным.  
(test1.py)
n = int(input("Введите количество элементов массива 'A': "))
arr = []

print("Введите элементы массива:")
for i in range(n):
 arr.append(float(input()))

min_i = arr.index(min(arr))
max_i = arr.index(max(arr))

start = min(min_i, max_i) + 1
end = max(min_i, max_i)

result = sum(x for x in arr[start:end] if x < 0)

print("Сумма отрицательных элементов между min и max =", result)


Кейс задача - 2 
Демонстрация работы методов базового и производного класса.  
(tesstcase2.py)

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def info(self):
        print(f"Сотрудник: {self.name}")
        print(f"Базовая зарплата: {self.base_salary} евро.")

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, languages):
        super().__init__(name, base_salary)
        self.languages = languages

    def info(self):
        super().info()
        print(f"Языки программирования: {', '.join(self.languages)}")

    def calculate_salary(self):
        bonus = 500 * len(self.languages)
        return self.base_salary + bonus

    def write_code(self):
        print(f"{self.name} Разрабатывает ПО")


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def info(self):
        super().info()
        print(f"Размер команды: {self.team_size} человек")

    def calculate_salary(self):
        bonus = self.team_size * 300
        return self.base_salary + bonus

    def hold_meeting(self):
        print(f"{self.name} Контролирует работу команды разработчиков")


def main():
    print("\nВведите данные программиста")
    dev_name = input("Имя: ")
    dev_salary = int(input("Базовая зарплата: "))
    langs = input("Введите языки через запятую: ").split(",")
    langs = [l.strip() for l in langs]

    dev = Developer(dev_name, dev_salary, langs)

    print("\nВведите данные управляющего")
    mgr_name = input("Имя: ")
    mgr_salary = int(input("Базовая зарплата: "))
    team_size = int(input("Размер команды: "))

    mgr = Manager(mgr_name, mgr_salary, team_size)

    print("\nПрограммист")
    dev.info()
    print("Итоговая зарплата:", dev.calculate_salary(), "евро.")
    dev.write_code()

    print("\nУправляющий")
    mgr.info()
    print("Итоговая зарплата:", mgr.calculate_salary(), "евро.")
    mgr.hold_meeting()


if __name__ == "__main__":
    main()

Кейс задача - 3
База данных «Туризм»  
(туризм2.sql)


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def info(self):
        print(f"Сотрудник: {self.name}")
        print(f"Базовая зарплата: {self.base_salary} евро.")

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, languages):
        super().__init__(name, base_salary)
        self.languages = languages

    def info(self):
        super().info()
        print(f"Языки программирования: {', '.join(self.languages)}")

    def calculate_salary(self):
        bonus = 500 * len(self.languages)
        return self.base_salary + bonus

    def write_code(self):
        print(f"{self.name} Разрабатывает ПО")


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def info(self):
        super().info()
        print(f"Размер команды: {self.team_size} человек")

    def calculate_salary(self):
        bonus = self.team_size * 300
        return self.base_salary + bonus

    def hold_meeting(self):
        print(f"{self.name} Контролирует работу команды разработчиков")


def main():
    print("\nВведите данные программиста")
    dev_name = input("Имя: ")
    dev_salary = int(input("Базовая зарплата: "))
    langs = input("Введите языки через запятую: ").split(",")
    langs = [l.strip() for l in langs]

    dev = Developer(dev_name, dev_salary, langs)

    print("\nВведите данные управляющего")
    mgr_name = input("Имя: ")
    mgr_salary = int(input("Базовая зарплата: "))
    team_size = int(input("Размер команды: "))

    mgr = Manager(mgr_name, mgr_salary, team_size)

    print("\nПрограммист")
    dev.info()
    print("Итоговая зарплата:", dev.calculate_salary(), "евро.")
    dev.write_code()

    print("\nУправляющий")
    mgr.info()
    print("Итоговая зарплата:", mgr.calculate_salary(), "евро.")
    mgr.hold_meeting()


if __name__ == "__main__":
    main()
