# Задача 1
cook_book = {}
with open('recipes.txt', 'rt', encoding='utf8') as file:
    for i in file:
        dish = i.strip()
        ingredients = []
        ing_count = file.readline()
        for j in range(int(ing_count)):
            ingr = file.readline()
            ingredient_name, quantity, measure = ingr.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book.update({dish: ingredients})
print(cook_book)

# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ing in cook_book[dish_name]:
                ing_list = {}
                if ing['ingredient_name'] not in ing_list:
                    ing_list['measure'] = ing['measure']
                    ing_list['quantity'] = int(ing['quantity']) * person_count
                    shop_list[ing['ingredient_name']] = ing_list
                else:
                    shop_list[ing['ingredient_name']]['quantity'] += int(ing['quantity'] * person_count)
        else:
            print('Введите корректное название блюда!')
    return shop_list

# Проверка из задачи 2
test_shop_list = get_shop_list_by_dishes(dishes = ['Запеченный картофель', 'Омлет'], person_count = 2)
print(test_shop_list)


# Задача 3
path_1 = '1.txt'
path_2 = '2.txt'
path_3 = '3.txt'
with open(path_1, encoding='utf-8') as f_1:
    file_1 = f_1.readlines()
with open(path_2, encoding='utf-8') as f_2:
    file_2 = f_2.readlines()
with open(path_3, encoding='utf-8') as f_3:
    file_3 = f_3.readlines()

with open('final_file.txt', 'w', encoding='utf-8') as file:
    if len(file_1) < len(file_2) and len(file_1) < len(file_3):
        file.write(path_1 + '\n')
        file.write(str(len(file_1)) + '\n')
        file.write(str(file_1))
        file.write('\n')
        if len(file_2)<len(file_3):
            file.write(path_2 + '\n')
            file.write(str(len(file_2)) + '\n')
            file.write(str(file_2))
            file.write('\n')
            file.write(path_3 + '\n')
            file.write(str(len(file_3)) + '\n')
            file.write(str(file_3))
        else:
            file.write(path_3 + '\n')
            file.write(str(len(file_3)) + '\n')
            file.write(str(file_3))
            file.write('\n')
            file.write(path_2 + '\n')
            file.write(str(len(file_2)) + '\n')
            file.write(str(file_2))
    elif len(file_2) < len(file_1) and len(file_2) < len(file_3):
        file.write(path_2 + '\n')
        file.write(str(len(file_2)) + '\n')
        file.write(str(file_2))
        file.write('\n')
        if len(file_1) < len(file_3):
            file.write(path_1 + '\n')
            file.write(str(len(file_1)) + '\n')
            file.write(str(file_1))
            file.write('\n')
            file.write(path_3 + '\n')
            file.write(str(len(file_3)) + '\n')
            file.write(str(file_3))
        else:
            file.write(path_3 + '\n')
            file.write(str(len(file_3)) + '\n')
            file.write(str(file_3))
            file.write('\n')
            file.write(path_1 + '\n')
            file.write(str(len(file_1)) + '\n')
            file.write(str(file_1))
    else:
        file.write(path_3 + '\n')
        file.write(str(len(file_3)) + '\n')
        file.write(str(file_3))
        file.write('\n')
        if len(file_1) < len(file_2):
            file.write(path_1 + '\n')
            file.write(str(len(file_1)) + '\n')
            file.write(str(file_1))
            file.write('\n')
            file.write(path_2 + '\n')
            file.write(str(len(file_2)) + '\n')
            file.write(str(file_2))
        else:
            file.write(path_2 + '\n')
            file.write(str(len(file_2)) + '\n')
            file.write(str(file_2))
            file.write('\n')
            file.write(path_1 + '\n')
            file.write(str(len(file_1)) + '\n')
            file.write(str(file_1))