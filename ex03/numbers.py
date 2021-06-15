def numbers():
    f = open("./numbers.txt", "r", encoding="UTF-8")
    s = f.read()
    print(s.replace(",", "\n"))


if __name__ == "__main__":
    numbers()
