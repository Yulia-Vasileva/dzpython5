a = int(input("Введите число A:"))
b = int(input("Введите число B:"))     

def sum(a, b):
    if a < 0 or b < 0:       
        return print('Неверный ввод') 
    return a + b 
print(sum(a, b))