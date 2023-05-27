# ; *Задача 20: * В настольной игре Скрабл (Scrabble) 
# ; каждая буква имеет определенную ценность. В случае 
# ; с английским алфавитом очки распределяются 
# ; так:
# ; A, E, I, O, U, L, N, S, T, R – 1 очко; 
# ; D, G – 2 очка; 
# ; B, C, M, P – 3 очка; 
# ; F, H, V, W, Y – 4 очка; 
# ; K – 5 очков; 
# ; J, X – 8 очков; 
# ; Q, Z – 10 очков. 
# ; А русские буквы оцениваются так: 
# ; А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# ; Д, К, Л, М, П, У – 2 очка; 
# ; Б, Г, Ё, Ь, Я – 3 очка; 
# ; Й, Ы – 4 очка; 
# ; Ж, З, Х, Ц, Ч – 5 очков; 
# ; Ш, Э, Ю – 8 очков; 
# ; Ф, Щ, Ъ – 10 очков. 
# ; Напишите программу, которая вычисляет стоимость введенного 
# ; пользователем слова. Будем считать, что на вход подается 
# ; только одно слово, которое содержит либо только английские, 
# ; либо только русские буквы.

# ; *Пример:*

# ; ноутбук
# ;     12


Point_Table_1 = set('AEIOULNSTRАВЕИНОРСТ')
Point_Table_2 = set('DGДКЛМПУ')
Point_Table_3 = set('BCMPБГЁЬЯ')
Point_Table_4 = set('FHVWYЙЫ')
Point_Table_5 = set('KЖЗХЦЧ')
Point_Table_8 = set('JXШЭЮ')
Point_Table_10 = set('QZФЩЪ')

xword = str(input('Введите словл: '))
Point_W = 0


for i in range (len(xword)):
     if Point_Table_1.intersection(xword[i].upper()) != set(''): 
        Point_W  += 1
     if Point_Table_2.intersection(xword[i].upper()) != set(''): 
        Point_W  += 2
     if Point_Table_3.intersection(xword[i].upper()) != set(''): 
        Point_W  += 3
     if Point_Table_4.intersection(xword[i].upper()) != set(''): 
        Point_W  += 4
     if Point_Table_5.intersection(xword[i].upper()) != set(''): 
        Point_W  += 5
     if Point_Table_8.intersection(xword[i].upper()) != set(''): 
        Point_W  += 8
     if Point_Table_10.intersection(xword[i].upper()) != set(''): 
        Point_W  += 10

print ('Количество очков: ', Point_W)

                                   
                                   


