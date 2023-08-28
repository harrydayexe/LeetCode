from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = []
        for car_index in range(len(position)):
            distance_to_go = target - position[car_index]
            arrival_times.append((distance_to_go / speed[car_index], position[car_index]))

        arrival_times.sort(key=lambda x: x[1])
        print(arrival_times)

        answer, current_max = 0, 0
        for time, _ in reversed(arrival_times):
            if time > current_max:
                current_max = time
                answer += 1

        return answer
