list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index = 0
for i, now_number in enumerate(list_numbers): #назначение элементам списка индекса
    max_maximum = list_numbers[index] #назначение, что первый элемент списка максимальеый
    if max_maximum <= now_number: #условие для нахождения максимального числа, чтоб оно проверяло каждый элемент списка
        index = i #вывод индекса последнего максимального элемента
list_numbers[-1], list_numbers[index] = list_numbers[index], list_numbers[-1] #меняем последний элемент списка и последний максимальный
print(list_numbers)
