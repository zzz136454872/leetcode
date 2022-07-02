from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int,
                       stations: List[List[int]]) -> int:
        mem = [startFuel]

        for station in stations:
            mem.append(-1)

            for i in range(len(mem) - 1, 0, -1):
                if mem[i - 1] >= station[0]:
                    mem[i] = max(mem[i], mem[i - 1] + station[1])
                else:
                    break

        # print(mem)

        for i in range(len(mem)):
            if mem[i] >= target:
                return i

        return -1


target = 1
startFuel = 1
stations = []
target = 100
startFuel = 1
stations = [[10, 100]]
target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]

# target=1000
# startFuel=299
# stations=[[14,123],[145,203],[344,26],[357,68],[390,35],[478,135],[685,108],[823,186],[934,217],[959,80]]
print(Solution().minRefuelStops(target, startFuel, stations))
