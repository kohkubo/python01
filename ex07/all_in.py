import sys

def main():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    args = sys.argv
    if 2 == len(args):
        list = [x.strip() for x in args[1].split(",")]
        for x in list:
            tmp = x.title()
            if not x:
                pass
            elif tmp in states:
                pass
            elif tmp in capital_cities.values():
                ab = [k for k, v in capital_cities.items() if v == tmp]
                state = [k for k, v in states.items() if v == ab[0]]
                print(tmp, "is the capital of", state[0])
            else:
                print(x, "is neither a capital city nor a state")


if __name__ == "__main__":
    main()
