# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input("Введите трёхзначное число: "))

# print (n//100)
# print ((n//10)%10)
# print (n%10)

m = n//100 + (n//10)%10 + n%10

print ("Сумма цифр трехзначного числа = " + str(m))
print (str(n) + " -> " + str(m)+ " (" + str(n//100)+ " + " + str((n//10)%10) + " + " + str (n%10) + ")" )