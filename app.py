import argparse

LOC = "loc"
PASS = "pass"
BASE_API = "http://api.open-notify.org/"


def get_args():
    parser = argparse.ArgumentParser(description="Print location and time of the ISS")

    parser.add_argument(
        "type", help="Specify the type of check to perform", choices=[LOC, PASS],
    )
    parser.add_argument("lat", help="Specify the latitude")
    parser.add_argument("long", help="Specify the longitude")
    return parser.parse_args()


def _loc():
    print("loc")
    url = "iss-now.json"
    print(url)


def _pass(lat, lon):
    url = f"iss-pass.json?lat={lat}&lon={lon}"
    print(url)


#    iss - now.json


def main(args):
    if args.type == LOC:
        return _loc()
    if args.type == PASS:
        return _pass(45.0, -122.3)

    raise TypeError("Unsupported type passed in ")


if __name__ == "__main__":
    args = get_args()
    main(args)
