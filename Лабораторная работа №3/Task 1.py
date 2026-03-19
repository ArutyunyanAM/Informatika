def index(items,item): # Функция поиска товара в списке
    for i in range(len(items)):
        if items[i] == item: # Проверка соответствия i-го товара заданному
            return i
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] # Список товаров

for find_item in ['банан', 'груша', 'персик']:
    index_item = index(items_list, find_item) # Запрос функции поиска товара в списке
    if index_item is not None: # Проверка наличия товара в списке
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
