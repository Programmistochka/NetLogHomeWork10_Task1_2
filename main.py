with open('datafile.txt', 'rt', encoding='utf-8') as file:
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

def print_dishes (dict):
    for key, value in dict.items():
        print(f'{key} :')
        for ing in value:
            print(ing)
    print('')
    
def get_shop_list_by_dishes(dishes, person_count):
    ingr_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr_quantity = int(ingr['quantity']) * person_count
                ingridient = ingr['ingridient_name']
                if ingridient not in ingr_dict.keys():
                    ingr_dict[ingridient]={'quantity': ingr_quantity, 'measure': ingr['measure']}
                else:
                    #если ингридиент уже есть, надо суммировать ingr_quantity с тем, что уже есть в словаре
                    for ingr_in_dict, compose in ingr_dict.items():
                        if ingr_in_dict == ingridient:
                            compose['quantity'] += ingr_quantity
                            break
        else:
            print(f'Рецепта для блюда - {dish} - нет в кулинарной книге')
            print()
    return ingr_dict
print_dishes(cook_book)

person_count = int(input('Укажите количество персон: '))
dishes = input(f'Укажите блюда для приготовления через "," ( {", ".join(cook_book.keys())}): ' ).split(', ')
#print(dishes)
print('\nСписок ингридиентов')
list_ingridients = get_shop_list_by_dishes(dishes, person_count) 
for ingridient, compose in list_ingridients.items():
    print(f'{ingridient}: {compose}')
print('______________________')