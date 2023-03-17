array = list(map(int, input().split()))
element = int(input())


def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


sort(array)
print(array)

left = 0
right = len(array)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if middle >= len(array):
        return "Число не соотвествует заданному условию"
    if array[middle] == element:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif array[middle - 1] < element and array[middle] > element:
        return middle - 1
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, left, right))