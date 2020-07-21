# Details

There is an API (http://api.open-notify.org/) that provides information on the
International Space Station. Documentation is provided via the website, along
with sample request/response.

Task

Implement a Python script that will accept the following command line arguments,
along with any required information, and print the expected results

## loc
print the current location of the ISS
Example: “The ISS current location at {time} is {LAT, LONG}”

## pass
print the passing details of the ISS for a given location
Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

## people
for each craft print the details of those people that are currently in space



When finished send me back your results! I am looking forward to hearing your
thoughts.

## Usage

``` bash
ahonnecke@homonym:~/Documents/professional/challenges/brooksource$ docker-compose run app loc
The ISS currnet location at 1595297080 is 44.7975, -97.9406
```

``` bash
ahonnecke@homonym:~/Documents/professional/challenges/brooksource$ docker-compose run app pass --lat=45 --lon=-122.3
The ISS will be overhead 45.0, -122.3 at 1595296591 for 550
```

``` bash
ahonnecke@homonym:~/Documents/professional/challenges/brooksource$ docker-compose run app people
Chris Cassidy
Anatoly Ivanishin
Ivan Vagner
Doug Hurley
Bob Behnken
```
