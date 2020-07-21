import argparse

LOC = "loc"
PASS = "pass"
PEOPLE = "people"
BASE_API = "http://api.open-notify.org"


def get_args():
    parser = argparse.ArgumentParser(description="Print location and time of the ISS")

    parser.add_argument(
        "type",
        help="Specify the type of check to perform",
        choices=[LOC, PASS, PEOPLE],
    )
    parser.add_argument("lat", help="Specify the latitude", nargs="?")
    parser.add_argument("long", help="Specify the longitude", nargs="?")
    return parser.parse_args()


def _loc():
    url = "/".join([BASE_API, "iss-now.json"])
    print(url)


def _pass(lat, lon):
    url = "/".join([BASE_API, f"iss-pass.json?lat={lat}&lon={lon}"])
    print(url)


def _people():
    url = "/".join([BASE_API, "astros.json"])
    print(url)


def main(args):
    if args.type == LOC:
        return _loc()
    elif args.type == PASS:
        return _pass(45.0, -122.3)
    elif args.type == PEOPLE:
        return _people()

    raise TypeError("Unsupported type passed in ")


if __name__ == "__main__":
    args = get_args()
    main(args)
