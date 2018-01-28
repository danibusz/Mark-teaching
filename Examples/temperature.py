from filereader import FileReader

File = FileReader('temperatureoftheyear.txt')
temperatures = File.get_temperatures()


for temperature in temperatures:
    print("Day:{} Temps:{}".format(temperature, temperatures[temperature]))

