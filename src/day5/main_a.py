with open('input/input', 'r') as f:
    seeds = list(map(int, (f.readline().strip().split('seeds: ')[1].split())))
    print(seeds)
    f.readline()
    f.readline()
    seeds_to_soil_lines = []
    while (line := f.readline().strip()) != '':
        seeds_to_soil_lines.append(list(map(int, line.split())))
    f.readline()
    soil_to_fertilizer_lines = []
    while (line := f.readline().strip()) != '':
        soil_to_fertilizer_lines.append(list(map(int, line.split())))
    f.readline()
    fertilizer_to_water_lines = []
    while (line := f.readline().strip()) != '':
        fertilizer_to_water_lines.append(list(map(int, line.split())))
    f.readline()
    water_to_light_lines = []
    while (line := f.readline().strip()) != '':
        water_to_light_lines.append(list(map(int, line.split())))
    f.readline()
    light_to_temperature_lines = []
    while (line := f.readline().strip()) != '':
        light_to_temperature_lines.append(list(map(int, line.split())))
    f.readline()
    temperature_to_humidity_lines = []
    while (line := f.readline().strip()) != '':
        temperature_to_humidity_lines.append(list(map(int, line.split())))
    f.readline()
    humidity_to_location_lines = []
    while (line := f.readline().strip()) != '':
        humidity_to_location_lines.append(list(map(int, line.split())))
    f.readline()


def find(value: int, lookups: list[list[int]]) -> int:
    for lookup in lookups:
        if lookup[1] <= value < lookup[1] + lookup[2]:
            return lookup[0] - lookup[1] + value
    return value


soils = [find(item, seeds_to_soil_lines) for item in seeds]
fertilizers = [find(item, soil_to_fertilizer_lines) for item in soils]
waters = [find(item, fertilizer_to_water_lines) for item in fertilizers]
lights = [find(item, water_to_light_lines) for item in waters]
temperatures = [find(item, light_to_temperature_lines) for item in lights]
humiditys = [find(item, temperature_to_humidity_lines) for item in temperatures]
locations = [find(item, humidity_to_location_lines) for item in humiditys]
print(min(locations))