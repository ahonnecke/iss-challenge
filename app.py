import argparse
import requests

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
    parser.add_argument("--lat", help="Specify the latitude")
    parser.add_argument("--lon", help="Specify the longitude")
    return parser.parse_args()


# {
#     "message": "success",
#     "timestamp": 1595296455,
#     "iss_position": {"latitude": "18.2417", "longitude": "-132.0077"},
# }
def _loc():
    url = "/".join([BASE_API, "iss-now.json"])
    body = requests.get(url).json()
    print(
        f"The ISS currnet location at {body['timestamp']} is "
        f"{body['iss_position']['latitude']}, {body['iss_position']['longitude']}"
    )


# {
#     "message": "success",
#     "request": {
#         "altitude": 100,
#         "datetime": 1595296427,
#         "latitude": 45.0,
#         "longitude": -122.3,
#         "passes": 5,
#     },
#     "response": [
#         {"duration": 550, "risetime": 1595296591},
#         {"duration": 654, "risetime": 1595302318},
#         {"duration": 632, "risetime": 1595308153},
#         {"duration": 628, "risetime": 1595314000},
#         {"duration": 654, "risetime": 1595319816},
#     ],
# }
def _pass(lat, lon):
    url = "/".join([BASE_API, f"iss-pass.json?lat={lat}&lon={lon}"])
    body = requests.get(url).json()
    print(
        f"The ISS will be overhead",
        f"{body['request']['latitude']}, {body['request']['longitude']}",
        f"at {body['response'][0]['risetime']} for {body['response'][0]['duration']}",
    )


# {
#     "message": "success",
#     "number": 5,
#     "people": [
#         {"craft": "ISS", "name": "Chris Cassidy"},
#         {"craft": "ISS", "name": "Anatoly Ivanishin"},
#         {"craft": "ISS", "name": "Ivan Vagner"},
#         {"craft": "ISS", "name": "Doug Hurley"},
#         {"craft": "ISS", "name": "Bob Behnken"},
#     ],
# }
def _people():
    url = "/".join([BASE_API, "astros.json"])
    body = requests.get(url).json()
    for person in body["people"]:
        print(person.get("name", "Ghostronaut"))


def main(args):
    if args.type == LOC:
        return _loc()
    if args.type == PASS:
        return _pass(args.lat, args.lon)
    if args.type == PEOPLE:
        return _people()

    raise TypeError(f"Unsupported type {args.type} passed in")


if __name__ == "__main__":
    args = get_args()
    main(args)
