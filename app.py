import argparse

LOC = "loc"
PASS = "pass"
BASE_API = "http://api.open-notify.org/"


def get_args():
    parser = argparse.ArgumentParser(description="Print location and time of the ISS")

    parser.add_argument(
        "type", help="Specify the type of check to perform", choices=[LOC, PASS],
    )
    return parser.parse_args()


def _loc():
    print("loc")
    # iss - now.json


def _pass():
    print("pass")


#    iss - now.json


def main(args):
    if args.type == LOC:
        return _loc()
    if args.type == PASS:
        return _pass()

    raise TypeError("Unsupported type passed in ")


if __name__ == "__main__":
    args = get_args()
    main(args)
