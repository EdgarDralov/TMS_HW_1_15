# Написать лямбда-функцию определяющую четное\нечетное. Функция принимает параметр (число) и если четное, то
# выдает слово "четное", если ет - то "нечетное"
# -------------------------------------------------------------------------------------------------------------

check_even_or_odd = lambda x: "even" if x % 2 == 0 else "odd"

# Example
num = int(input("Enter num: "))
result = check_even_or_odd(num)
print(f"Number {num} - {result}")
