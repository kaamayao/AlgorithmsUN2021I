import sys

def compute_min_refills(distance, tank, stops):
    stops.insert(0,0)
    stops.append(distance)
    last_refill_stop = 0
    current_tank = tank
    refills = 0
    i = 0
    while i<(len(stops)-1):
        current_stop = stops[i]
        next_stop = stops[i+1]
        distance_stops = next_stop - current_stop

        if distance_stops > current_tank:
            if last_refill_stop == current_stop:
                return -1
            refills = refills + 1
            last_refill_stop = current_stop
            current_tank = tank
        else:
            current_tank = current_tank - distance_stops
            i = i+1
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
