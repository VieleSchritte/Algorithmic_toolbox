import sys


def count_refills(distance, full_tank, journey_stops):
    num_refills, current_refill = 0, 0
    journey_stops = [0] + journey_stops + [distance]
    overall_miles = len(journey_stops) - 1

    while current_refill < overall_miles:
        last_refill = current_refill

        while journey_stops[current_refill + 1] - journey_stops[last_refill] <= full_tank:
            current_refill += 1
            if current_refill == overall_miles:
                break

        if current_refill == last_refill:
            return -1
        if current_refill < overall_miles:
            num_refills += 1
        else:
            break

    return num_refills


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    full_distance, full_tank, stops_number = data[:3]
    stops = data[3:]

    print(count_refills(full_distance, full_tank, stops))
