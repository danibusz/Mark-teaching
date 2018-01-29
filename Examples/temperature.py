from filereader import FileReader

File = FileReader('temperatureoftheyear.txt')
temperatures = File.get_temperatures()

"""for temperature in temperatures:
    print("Day:{} Temps:{}".format(temperature, temperatures[temperature]))"""

all_temperature = {}

for temperature in temperatures:
    for day in range(0,len(temperature)):
        all_temperature[temperature] = temperatures[temperature]




lowest_temp = '100'
key = ''

#def lowest_temperature():
for temperature in temperatures:
    for time in range(0,len(all_temperature[temperature])):
        current = all_temperature[temperature][time]
        if current < lowest_temp:
            lowest_temp = current
            key = temperature

print(lowest_temp)
print(key)