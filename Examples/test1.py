from filereader import FileReader

File = FileReader('temperature.log')
temperatures = File.get_temperatures()

for temperature in temperatures:
    print("Day:{} Temps:{}".format(temperature, temperatures[temperature]))