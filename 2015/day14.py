from dataclasses import dataclass

with open("input14.txt", "r") as file:
    stats = file.read().splitlines()


@dataclass
class Reindeer:
    name: str
    speed: int
    duration: int
    rest: int

    def get_distance(self, time):
        cycle_time = self.duration + self.rest
        intervals, remainder = divmod(time, cycle_time)
        return (intervals * self.speed *
                self.duration) + (self.speed * min(self.duration, remainder))


reindeer = []
for line in stats:
    sp = line.split()
    reindeer.append(Reindeer(sp[0], int(sp[3]), int(sp[6]), int(sp[-2])))


RACE_FINISH = 2503

# Part 1
print(max(deer.get_distance(RACE_FINISH) for deer in reindeer))

# Part 2
names_to_speeds = dict()
names_to_points = dict()
for t in range(1, RACE_FINISH + 1):
    for deer in reindeer:
        names_to_speeds[deer.name] = deer.get_distance(t)
    farthest_dist = max(names_to_speeds.values())
    for deer in reindeer:
        if deer.get_distance(t) != farthest_dist:
            continue
        if deer.name not in names_to_points:
            names_to_points[deer.name] = 1
        else:
            names_to_points[deer.name] += 1
print(max(names_to_points.values()))