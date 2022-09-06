# Car Fueling Problem

# Compute the minimum number of gas tank refills to get from one city to another.
#   Input: Integers d and m as well as a sequence of integers stop1 <stop2 < ... < stopn.
#   Output: The minimum number of refills to get from one city to another in a car can travel at most m miles on a full tank. The distance between the cities is d miles and there are gas stations at distances 
#      stop1;stop2; : : : ;stopn along the way.


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    min_refills, curr_index = 0, 0 # Instantiate count of refills and index pointer for traversing the list of stops
    stops = [0] + stops + [d] # include the start and destination of the journey in the stops

    # Check if we can get to our final destination without any stops or refills (best case)
    if d <= m:
        return 0
        
    # Traverse the entire stops till we get to the final destination
    while curr_index < len(stops) - 1:
        # We want to update our laststop if we eventually stopped at a gas station to refill
        lastStop = curr_index

        # We are going to be greedy when approaching a gas station by only stopping unless we cannot reach the next one on our tank
        while curr_index < len(stops) - 1 and stops[curr_index + 1] - stops[lastStop] <= m:  # We check that we haven't gotten to our final destination and we can still reach the next gas station on our current tank
            curr_index += 1

        # If we can't reach any more gas station and haven't gotten to the final destination (that means we'll be at the last gast station
        # Then It's impossible to complete our journey
        if curr_index == lastStop:
            return -1

        # update the num of refills we've had so far (as long as we haven't gotten to the final destination
        if curr_index < len(stops) - 1:
            min_refills += 1
            
    return min_refills



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))