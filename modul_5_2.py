class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.nFloors:
            print('Такого этажа не существует!')
        else:
            if new_floor < 1:
                for f in range(1, new_floor-1, -1):
                    print('Спускаемся:', f)
            for f in range(1, new_floor+1):
                print('Поднимаемся:', f)

    def __len__(self):
        return self.nFloors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.nFloors}.'

def main():

    print('вариант 1 modul_5_1')
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(0)
    h2.go_to(25)
    h1.go_to(5)
    h2.go_to(1)

    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    print(f'вариант 2 modul_5_1:\n{h1}\n{h2}')
    print(len(h1), len(h2))

if __name__ == '__main__':
    main()



