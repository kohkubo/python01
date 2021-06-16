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
        try:
            print(capital_cities[states[args[1]]])
        except:
            print('Unknown state')


if __name__ == "__main__":
    main()
