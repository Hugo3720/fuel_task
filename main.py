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

    def find_most_sellable(self, name):
        dict_date = dict()
        max_count = 0
        max_date = ""
        for fuel in self.fuel_list:
            if fuel.name == name:
                try:
                    count = dict_date[fuel.date]
                    dict_date[fuel.date] = count + 1
                except:
                    dict_date.update({fuel.date: 1})

                if dict_date[fuel.date] > max_count:
                    max_count = dict_date[fuel.date]
                    max_date = fuel.date

        return max_date




if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.readlines()

    fuel_list = MakeFuelList(data)
    fuel_list.print_fuel_list()
    print(fuel_list.find_most_sellable("DT"))

