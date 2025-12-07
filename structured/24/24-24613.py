s = open("24_24613.txt").read()

maxl = (9 + 5 + 5) * 5
cnt = 0

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d.count("HALLOWEEN") > 5 or d.count("TRICK") > 5 or d.count("TREAT") > 5:
            break

        if d.count("HALLOWEEN") == 5 and d.count("TRICK") == 5 and d.count("TREAT") == 5:
            cnt += 1

    if l % 100000 == 0:
        print(l)


print(cnt)




# Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
# Определите, сколько в этом файле подпоследовательностей подряд идущих символов, в которых каждое из слов:
# 'HALLOWEEN', 'TRICK' и 'TREAT' встречается ровно по 5 раз.
# В ответе запишите число — количество подходящих подпоследовательностей.