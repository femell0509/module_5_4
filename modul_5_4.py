class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        #cls.houses_history.append(args)
        cls.houses_history += args
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название:{self.name} , количество этажей {self.number_of_floors}  '

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else: print(f'{new_floor} этажа не существует!')

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors >= other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        return self + other
    def __del__(self):
        print(f'{self.name} снесен, но останентся в истории')

h1 = House('ЖК Эльбрус', number_of_floors = 10)
print(House.houses_history)
h2 = House('ЖК Акация', number_of_floors = 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', number_of_floors = 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
