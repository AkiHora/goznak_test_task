def prod(array):
    """
    Перемножение элементов массива
    """
    res = 1
    for a in array:
        res *= a
    return res

def multiplicate(A):
    """
    Расчет произведения всех чисел массива кроме i-го для i-го числа
    """
    # Расчет произведения для i-го числа 
    prod_A_except = lambda i: prod(A[:i] + A[i+1:])
    
    # Применение функции prod_A_except ко всем числам A
    return list(map(prod_A_except, range(len(A))))

# Пример 1 (из ТЗ)
A = [1, 2, 3, 4]
print(multiplicate(A))

# Пример 2
A = [2, 1, -4, .5]
print(multiplicate(A))
