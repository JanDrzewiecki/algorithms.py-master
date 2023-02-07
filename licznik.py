class Licznik:
    ile = 0  # pole statyczne

    def __init__(self):  # konstruktor
        Licznik.ile += 1  # odwołanie do pola statycznego
        self.ktory = Licznik.ile
        print(f"To jest obiekt nr {Licznik.ile}")

    def __del__(self):  # destruktor, czyli kod, który wykonuje się
        # podczas niszczenia obiektu
        Licznik.ile -= 1
        print(f"Niszczę obiekt nr {self.ktory}, pozostało jeszcze {Licznik.ile}.")

    @staticmethod
    def policz():
        return Licznik.ile


def main():
    a = Licznik()
    b = Licznik()
    c = Licznik()
    print(f"a to obiekt nr {a.ktory}")
    print(f"b to obiekt nr {b.ktory}")
    print(f"c to obiekt nr {c.ktory}")
    print(f"Liczba obiektow to: {Licznik.policz()}")
    a = None
    b = None
    print(f"Liczba obiektow to: {Licznik.policz()}")


if __name__ == "__main__":
    main()
## To jest obiekt nr 1
## To jest obiekt nr 2
## To jest obiekt nr 3
## a to obiekt nr 1
## b to obiekt nr 2
## c to obiekt nr 3
## Liczba obiektow to: 3
## Niszczę obiekt nr 1, pozostało jeszcze 2.
## Niszczę obiekt nr 2, pozostało jeszcze 1.
## Liczba obiektow to: 1
## Niszczę obiekt nr 3, pozostało jeszcze 0.