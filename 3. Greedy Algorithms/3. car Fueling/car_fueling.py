def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    min_refills, curr_index = 0, 0 # Instantiate count of refills and index pointer for traversing the list of stops
    stops = [0] + stops + [d]

    # Check if we can get to our final destination without any refills
    if d <= m:
        return 0
    else:
        # Traverse the entire stop list till we get to the final destination
        while curr_index < len(stops) - 1:
            # We want to update our last stop
            lastStop = curr_index
            # We are going to be greedy when approaching a gas station by only stopping unless we cannot reach the next one on our tank
            # We check that we haven't gotten to our final destination and we can still reach the next gas station on our current tank
            while curr_index < len(stops) - 1 and stops[curr_index + 1] - stops[curr_index] <= m:
                curr_index += 1

            # If we can't reach any more gas station and haven't gotten to the final destination (that means we'll be at the last gast station
            # Then It's impossible to complete our journey
            if curr_index == lastStop:
                return -1

            # update the num of refills we've had so far (as long as we haven't gotten to the final destination
            if curr_index < len(stops) - 1:
                min_refills += 1
                print(min_refills)

        return min_refills

if __name__ == '__main__':
    #input_d = int(input())
    #print(input_d)
    #input_m = int(input())
    #print(input_m)
    #input_n = int(input())
    #input_stops = list(map(int, input().split()))
    #print(input_stops, len(input_stops))
    #assert len(input_stops) == input_n

    #print(compute_min_number_of_refills(input_d, input_m, input_stops))
    print(compute_min_number_of_refills(950, 400, [200,350,550, 750]))