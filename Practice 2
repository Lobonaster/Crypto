def t1():
    # Исходное слово
    word = "лебедев"
    # Порядок перестановки
    replace_table = [3, 1, 4, 2, 5, 7, 6]

    # Создаем массив для зашифрованного слова
    encrypted_word = [''] * len(word)
    # Переставляем буквы согласно порядку
    for index, new_position in enumerate(replace_table):
        encrypted_word[new_position - 1] = word[index]
    # Объединяем список в строку
    encrypted_word = ''.join(encrypted_word)

    print("Исходное слово:", word)
    print("Порядок перестановки:", replace_table)
    print("Зашифрованное слово:", encrypted_word)


def t2():
    word = "лебедев"
    print("Исходное слово:", word)
    print("Порядок перестановки:", [2, 3, 1])
    encrypted_word = ""

    while len(word) % 3 != 0:
        word += "я"
    for i in range(0, len(word), 3):
        encrypted_word += word[i + 2] + word[i] + word[i + 1]

    print("Зашифрованное слово:", encrypted_word)


def t3():
    word = "лебедев артём"
    print("Исходный текст:", word)
    enc_alph = []
    line = []
    enc_word = ""
    while len(word) % 4 != 0:
        word += "я"
    for i in word:
        line.append(i)
        if len(line) == 4:
            enc_alph.append(line)
            line = []
    for i in enc_alph:
        print(i)
    for i in range(4):
        for j in enc_alph:
            enc_word += j[i]
    print("Зашифрованное слово:", enc_word)

def t4():
    key = "вишня"
    nkey = "01324"
    word = "лебедев артём"
    print("Ключ:", key, ", Исходный текст:", word)
    enc_alph = []
    line = []
    enc_word = ""
    while len(word) % len(key) != 0:
        word += " "
    for i in word:
        line.append(i)
        if len(line) == len(key):
            enc_alph.append(line)
            line = []
    for i in range(len(key)):
        for j in enc_alph:
            enc_word += j[nkey.index(str(i))]
    for i in enc_alph:
        print(i)
    print("Шифротекст: ", enc_word,"Ключ: ", key + " " + nkey)

def t7():
    word = "лебедев+артём"
    print("Исходный текст:", word)
    enc_alph = []
    line = []
    enc_word = ""
    while len(word) % 4 != 0:
        word += "_"
    for i in word:
        line.append(i)
        if len(line) == 4:
            enc_alph.append(line)
            line = []
    swap_x = [2,0,3,1]
    swap_y = [3,0,2,1]
    for i in enc_alph:
        print(i)
    for i in range(len(swap_x)):
        for j in range(len(swap_y)):
            enc_word += enc_alph[swap_y.index(j)][swap_x.index(i)]
    print("Шифротекст:",enc_word, "Х:", swap_x, "У:", swap_y)

txt = input("Введите номер таска(1-7): ")
if txt == "1":
    t1()
elif txt == "2":
    t2()
elif txt == "3":
    t3()
elif txt == "4":
    t4()
elif txt == "5":
    print("Поворотная решётка")
elif txt == "6":
    print("Магические квадраты")
elif txt == "7":
    t7()
else: print("Ошибка ввода")
