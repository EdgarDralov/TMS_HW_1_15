# Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку.
# В качестве функции в map использовать lambda
# =================================================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

string_numbers = list(map(lambda x: str(x), numbers))

print(string_numbers)
