def main():
    greetings()
    bye()


def greetings():
    name = input("Name: ")
    print(f"hello, {name}")


def bye():
    name = input("Name: ")
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()
