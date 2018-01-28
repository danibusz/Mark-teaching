import re

class FileReader:

    def __init__(self, filename):
        self.filename = filename
        self.temperatures = self.get_temperatures_per_day(filename)

    def get_temperatures_per_day(self, filename):
        with open(filename, 'r') as file:

            data_from_file = re.findall('(\d{4}-\d{2}-\d{2})\W+(\[.*\])', file.read())

            temperatures_per_day = {}
            for data in data_from_file:
                day = data[0]
                temperatures = self.get_temperatures_from_file(data[1])
                temperatures_per_day[day] = temperatures
        return temperatures_per_day

    def get_temperatures_from_file(self, temperatures):
        split_temperatures = temperatures
        delete_chars = ['[', ']', ' ']
        for char in delete_chars:
            split_temperatures = split_temperatures.replace(char, '')
        split_temperatures = split_temperatures.split(',')
        return split_temperatures

    def get_temperatures(self):
        return (self.temperatures)