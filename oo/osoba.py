from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date

    def introduce_yourself(self):
        print(f"I am {self.get_full_name()}. I was born {self.__birth_date.date()}.")

    def get_full_name(self):
        return self.__last_name + " " + self.__first_name

    #Zwraca różnicę wieku w dniach pomiędzy dwoma osobami
    def compare_age(self, person):
        return self.__birth_date - person.__birth_date

    def is_older(self, person):
        diff = self.compare_age(person).days
        if diff > 0:
            print(f"Ja, {self.get_full_name()} jestem starszy od {person.get_full_name()} o {diff} dni")
        elif diff < 0:
            print(f"Ja, {self.get_full_name()} jestem młodszy od {person.get_full_name()} o {diff} dni")
        else:
            print(f"Ja, {self.get_full_name()} mam dokładnie taki sam wiek jak {person.get_full_name()}")


def main():
    # tworzymy dwa obiekty klasy Osoba
    jan = Person("Jan", "Skywalker", datetime(2005, 5, 5))
    leya = Person("Leya", "Organa", datetime(2005, 5, 6))
    luke = Person("Luke", "Skywalker", datetime(1985, 4, 24))

    luke.introduce_yourself()
    jan.introduce_yourself()
    jan.is_older(luke)
    jan.is_older(leya)



if __name__ == "__main__":
    main()
## Jestem Jan Nowak. Mam 48 lat.
## Jestem Adam Mickiewicz. Mam 220 lat.
## Jestem Adam Mickiewicz. Mam 221 lat.
## Wiek Adama sprzed urodzin: 220
## Jestem Stanisław Witkiewicz. Mam 133 lat.
