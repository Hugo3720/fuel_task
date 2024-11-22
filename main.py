import re


class Fuel:
    def __init__(self, data):
        self.name = re.findall(r'"(.*?)"', data)[0]
        self.date = re.findall(r'\d{4}.\d{2}.\d{2}', data)[0]
        self.price = float(re.search(r'\d+,\d+', data).group(0).replace(',', '.'))

    def __str__(self):
        return f'{self.name}  {self.date}  {self.price}'


class MakeFuelList:
    def __init__(self, data_list):
        fuel_list = []
        for data in data_list:
            fuel_list.append(Fuel(data))
        self.fuel_list = fuel_list

    def print_fuel_list(self):
        for item in self.fuel_list:
            print(item)





if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.readlines()

    fuel_list = MakeFuelList(data)
    fuel_list.print_fuel_list()

