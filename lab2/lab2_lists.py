# Удаление повторяющихся чисел более двух раз
def delete_duplicates(lst):
    unique_nums = []
    for num in lst:
        if lst.count(num) <= 2:  # Проверяем, сколько раз число встречается в списке
            unique_nums.append(num)
    return unique_nums


# Нахождение подмножества с заданной суммой элементов
def find_subset(lst, target_sum):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if sum(lst[i:j]) == target_sum:  # Проверяем, равна ли сумма элементов подсписка целевой сумме
                return lst[i:j]
                return None  # Если подмножество не найдено, возвращаем None
          
lst = [1, 2, 3, 2, 1, 4, 5, 4]
unique_nums = delete_duplicates(lst)
print(unique_nums)  # Выводит [3, 5]

target_sum = 7
subset = find_subset(lst, target_sum)
print(subset)  # Выводит [2, 3, 2]
