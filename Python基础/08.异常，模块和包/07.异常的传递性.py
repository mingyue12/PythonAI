def f02():
    print("02start")
    1 / 0
    print("02end")


def f01():
    print("01start")
    f02()
    print("01end")


def main():
    f01()

try:
    main()
except Exception as e:
    print(e)
