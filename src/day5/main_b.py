import numpy

with open('input/input', 'r') as f:
    seeds = list(map(int, (f.readline().strip().split('seeds: ')[1].split())))
    seeds = numpy.reshape(seeds, (int(len(seeds) / 2), 2))
    f.readline()
    f.readline()
    seeds_to_soil_lines = []
    while (line := f.readline().strip()) != '':
        seeds_to_soil_lines.append(list(map(int, line.split())))
    seeds_to_soil_lines = sorted(seeds_to_soil_lines, key=lambda item: item[1])
    f.readline()
    soil_to_fertilizer_lines = []
    while (line := f.readline().strip()) != '':
        soil_to_fertilizer_lines.append(list(map(int, line.split())))
    soil_to_fertilizer_lines = sorted(soil_to_fertilizer_lines, key=lambda item: item[1])
    f.readline()
    fertilizer_to_water_lines = []
    while (line := f.readline().strip()) != '':
        fertilizer_to_water_lines.append(list(map(int, line.split())))
    fertilizer_to_water_lines = sorted(fertilizer_to_water_lines, key=lambda item: item[1])
    f.readline()
    water_to_light_lines = []
    while (line := f.readline().strip()) != '':
        water_to_light_lines.append(list(map(int, line.split())))
    water_to_light_lines = sorted(water_to_light_lines, key=lambda item: item[1])
    f.readline()
    light_to_temperature_lines = []
    while (line := f.readline().strip()) != '':
        light_to_temperature_lines.append(list(map(int, line.split())))
    light_to_temperature_lines = sorted(light_to_temperature_lines, key=lambda item: item[1])
    f.readline()
    temperature_to_humidity_lines = []
    while (line := f.readline().strip()) != '':
        temperature_to_humidity_lines.append(list(map(int, line.split())))
    temperature_to_humidity_lines = sorted(temperature_to_humidity_lines, key=lambda item: item[1])
    f.readline()
    humidity_to_location_lines = []
    while (line := f.readline().strip()) != '':
        humidity_to_location_lines.append(list(map(int, line.split())))
    humidity_to_location_lines = sorted(humidity_to_location_lines, key=lambda item: item[1])
    f.readline()


def find(results: list[list[int, int]], value: list[int, int], lookups: list[list[int]]) -> list[list[int, int]]:
    if value[0] < lookups[0][1]:  # current item is smaller than a mapping e.g. no mapping
        results.append([value[0], min(value[1], lookups[0][0] - value[0])])
        if lookups[0][0] - value[0] < value[1]:
            return results  # e.g. lookup table starts at 10 and item range ends at 8
        value[1] -= lookups[0][1] - value[0]
        value[0] = lookups[0][0]
        if value[1] == 0:
            return results
    if lookups[0][1] <= value[0] <= lookups[0][1] + lookups[0][2]:
        if value[0] + value[1] <= lookups[0][1] + lookups[0][2]:  # List is done
            results.append([lookups[0][0] - lookups[0][1] + value[0], min(value[1], lookups[0][2])])
            return results
        results.append([lookups[0][0] - lookups[0][1] + value[0], lookups[0][1] + lookups[0][2] - value[0]])
        value[1] -= lookups[0][1] + lookups[0][2] - value[0]  # reduce range
        value[0] = lookups[0][1] + lookups[0][2]  # Increase start
        if value[1] == 0:
            return results
    if len(lookups) == 1:
        results.append(value)
        return results
    return find(results, value, lookups[1:])


soils = []
for item in seeds:
    soils.extend(find([], item, seeds_to_soil_lines))

fertilizers = []
for item in soils:
    fertilizers.extend(find([], item, soil_to_fertilizer_lines))

waters = []
for item in fertilizers:
    waters.extend(find([], item, fertilizer_to_water_lines))

lights = []
for item in waters:
    lights.extend(find([], item, water_to_light_lines))

temperatures = []
for item in lights:
    temperatures.extend(find([], item, light_to_temperature_lines))


humiditys = []
for item in temperatures:
    humiditys.extend(find([], item, temperature_to_humidity_lines))


locations = []
for item in humiditys:
    locations.extend(find([], item, humidity_to_location_lines))

print(min(map(lambda location: location[0], locations)))