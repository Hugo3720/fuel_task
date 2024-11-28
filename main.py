import re
from collections import Counter

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
        dates = [fuel.date for fuel in self.fuel_list if fuel.name == name]

        # Используем Counter для подсчета количества продаж по датам
        date_counts = Counter(dates)

        # Находим дату с максимальным количеством продаж
        if date_counts:
            max_date = date_counts.most_common(1)[0]  # Получаем дату с максимальным количеством
            return max_date [0]
        else:
            return None




if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.readlines()

    fuel_list = MakeFuelList(data)
    fuel_list.print_fuel_list()
    print(fuel_list.find_most_sellable("92"))
