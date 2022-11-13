with open('datafile.txt', 'rt') as file:
    cook_book = {}
    dishes = []
    for line in file:
        dish_name = line.strip()
        ingrid_count = int(file.readline())
        ingridients = []
        for i in range(ingrid_count):
            ingrid = file.readline().strip().split(' | ')
            ingrid_name, quantity, measure = ingrid
            ingridients.append({'ingridient_name': ingrid_name,
                                'quantity': quantity,
                                'measure': measure})
        file.readline()
        cook_book[dish_name] = ingridients
    
print(cook_book)