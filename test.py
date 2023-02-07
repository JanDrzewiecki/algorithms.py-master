class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.__prywatne = 1, 2, 3
def main():
    test = Test()
    print(test.publiczne)
    print(test._chronione)
    print(test._Test__prywatne)
if __name__ == "__main__":
    main()
## 1
## 2
## 3