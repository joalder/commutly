import pprint
from datetime import datetime

import googlemaps

from key import KEY

PRINT_EVERYTHING = True


def calculate_directions(origin, destination):
    client = googlemaps.Client(KEY)
    directions = client.directions(
        origin=origin,
        destination=destination,
        mode="transit",
        departure_time=datetime(2020, 3, 24, 10, 0)
    )

    if PRINT_EVERYTHING:
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(directions)

    for direction in directions:
        legs = direction['legs']
        if len(legs) == 1:
            print("We have only one leg... :(")
        else:
            print("We have more than one leg :D")

        for leg in legs:
            print(f"Total Duration: {leg['duration']['text']} Distance: {leg['distance']['text']}")

            for step in leg['steps']:
                print(f"Step Duration: {step['duration']['text']}")
                if 'transit_details' in step:
                    mode = step['transit_details']['line']['vehicle']['name']
                else:
                    mode = step['travel_mode']
                print(f"By: {mode}")


if __name__ == '__main__':
    calculate_directions("Fehraltorf", "Im Rietpark 19, Bülach")
