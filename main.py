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
def sum_file(*files):
    text = {}
    for file in files:
        summary = []
        with open(file, 'rt', encoding='utf-8') as f:
            text_in_file = f.readlines()
            length = len(text_in_file)
            summary.append([length])
            text.update({file: summary})
    sorted_files = sorted(text.items(), key=lambda x: x[1])
    with open('sum_file.txt', 'w', encoding='utf-8') as final_file:
        for item in sorted_files:
            final_file.writelines(f'{item[0]}\n')
            final_file.writelines(f'{item[1][0][0]}\n')
            with open(item[0], 'rt', encoding='utf-8') as f:
                final_file.writelines(f)
                final_file.writelines('\n')

#Проверка для задачи 3
sum_file('1.txt', '2.txt', '3.txt')