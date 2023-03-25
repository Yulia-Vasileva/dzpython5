A = int(input("Введите число A:"))
B = int(input("Введите число B:"))     

def Number(A,B):
    if B == 0:
        return 1
    return A**B
print(Number(A,B))