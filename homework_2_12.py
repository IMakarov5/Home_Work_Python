# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y 
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#  Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать 
#  задуманные Петей числа.
# 
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

while True:
    try:
        print('Загадай два натуральных числа и не больше 1000.')
        S = int (input('Укажите сумму загадонных чисел: '))
        P = int (input('Укажите произведение загадонных чисел: '))

        if 1< S < 2001 and 0 < P < 1000001:
            X = 1
            Y = 1
            
            while X <= 1000: 
                while Y <= 1000:
                    if X+Y==S and X*Y==P:
                        print('Загаданные числа: ', X , ' и ', Y)
                        X=1001
                        Y=1001
                    else:
                        Y +=1
                X += 1
                if X==1001 and Y==1001:  print("Ты не Петя, а Катя. Запусти скрип и загадай два натуральных числа.")
                Y=1
                
            break
        # 
        # 
        else:
            print('Загаданные числа должны быть натуральные и не больше 1000')
            

    except:
        print('Некорректный ввод. Попробуйте еще раз!')   
