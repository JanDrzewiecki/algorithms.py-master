class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def multiple(self, fraction):
        result = Fraction(self.numerator * fraction.numerator, self.denominator * fraction.denominator)
        return result

    @staticmethod
    def nwd(a, b):
        if b > 0:
            return Fraction.nwd(b, a % b)
        return a

    @staticmethod
    def nww(a, b):
        return a * b // Fraction.nwd(a, b)

    def add(self, fraction):
        common_denominator = self.denominator * fraction.denominator
        sum = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        result = Fraction(sum, common_denominator)
        return result

    def subtract(self, fraction):
        common_denominator = self.denominator * fraction.denominator
        sum = self.numerator * fraction.denominator - fraction.numerator * self.denominator
        result = Fraction(sum, common_denominator)
        return result

    def divide(self, fraction):
        numerator = fraction.numerator
        denominator = fraction.denominator
        return Fraction(self.numerator * numerator, self.denominator * denominator)

    def reduce(self, fraction):
        fraction_denominator_first = fraction.denominator
        self_denominator_first = self.denominator
        fractions_nww = Fraction.nww(self.denominator, fraction.denominator)
        self.denominator = fractions_nww
        fraction.denominator = fractions_nww
        divisor_self = self_denominator_first / self.denominator
        divisor_fraction = fraction_denominator_first / fraction.denominator
        self.numerator *= divisor_self
        fraction.numerator *= divisor_self


def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    print(f"{f1} + {f2} = {f1.add(f2)}")
    print(f"{f1} - {f2} = {f1.subtract(f2)}")
    print(f"{f1} * {f2} = {f1.multiple(f2)}")
    print(f"{f1} div {f2} = {f1.divide(f2)}")



if __name__ == "__main__":
    main()