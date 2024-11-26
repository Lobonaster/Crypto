ru_alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
           'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def Caesar_Encoder(text, key, alph_lang="ru"):
    result = ""
    if alph_lang == "ru":
        alph = ru_alph
    elif alph_lang == "en":
        alph = en_alph
    for i in text.lower():
        if i in alph:
            result += alph[(alph.index(i)+key)%len(alph)]
        else:
            result += i

    return result


#print("Исходное сообщение(ключ=17): Whereas cryptography is the practice of protecting the contents of a message alone, steganography is concerned with concealing the fact that a secret message is being sent, as well as concealing the contents of the message")
#print("\nЗашифровнанное сообщение: ",Caesar_Encoder("Whereas cryptography is the practice of protecting the contents of a message alone, steganography is concerned with concealing the fact that a secret message is being sent, as well as concealing the contents of the message",17,"en"))

def Caesar_Decoder(text, key, alph_lang="ru"):
    result = ""
    if alph_lang == "ru":
        alph = ru_alph
    elif alph_lang == "en":
        alph = en_alph
    for i in text.lower():
        if i in alph:
            result += alph[(alph.index(i)-key)%len(alph)]
        else:
            result += i
    return result


#print("@  Исх.Сообщение(Вар1,Ключ=6): Yzkmgtumxgvne otirajky znk iutikgrsktz ul otluxsgzout coznot iusvazkx lorky")
#print("РАСШИФРОВАННОЕ СООБЩЕНИЕ: ",Caesar_Decoder("Yzkmgtumxgvne otirajky znk iutikgrsktz ul otluxsgzout coznot iusvazkx lorky",6,"en"))
#print("@@  Исх.Сообщение(Вар2,Ключ=7): Aol johunl pz zv zbiasl aoha zvtlvul dov pz uva zwljpmpjhssf svvrpun mvy pa pz busprlsf av uvapjl aol johunl")
#print("РАСШИФРОВАННОЕ СООБЩЕНИЕ: ",Caesar_Decoder("Aol johunl pz zv zbiasl aoha zvtlvul dov pz uva zwljpmpjhssf svvrpun mvy pa pz busprlsf av uvapjl aol johunl",7,"en"))
#print("@@@  Исх.Сообщение(Вар3,Ключ=9): Cqn orabc anlxamnm dbn xo cqn cnav fjb rw (1499) kh Sxqjwwnb Carcqnvrdb rw qrb Bcnpjwxpajyqrj")
#print("РАСШИФРОВАННОЕ СООБЩЕНИЕ: ",Caesar_Decoder("Cqn orabc anlxamnm dbn xo cqn cnav fjb rw (1499) kh Sxqjwwnb Carcqnvrdb rw qrb Bcnpjwxpajyqrj",9,"en"))
#print("@@@@  Исх.Сообщение(Вар4,Ключ=12): Yqeemsqe iduffqz uz Yadeq oapq az kmdz mzp ftqz wzuffqp uzfa m buqoq ar oxaftuzs iadz nk m oagduqd")
#print("РАСШИФРОВАННОЕ СООБЩЕНИЕ: ",Caesar_Decoder("Yqeemsqe iduffqz uz Yadeq oapq az kmdz mzp ftqz wzuffqp uzfa m buqoq ar oxaftuzs iadz nk m oagduqd",12,"en"))

def Frequency_Decoder(text):
    letter_frequency = {}
    alphabet = ru_alph
    # Подсчет частоты букв
    for i in text.lower():
        if i in alphabet:
            if i not in letter_frequency.keys():
                letter_frequency[i] = 0
            letter_frequency[i] += 1

    # Получение трех наиболее частых букв
    top_letters = sorted(letter_frequency, key=letter_frequency.get, reverse=True)[:3]
    print("Топ 3 буквы:", top_letters)

    # Декодирование с использованием наиболее частых букв
    for i in top_letters:
        for common_letter in ["о", "е", "ё", "а"]:  # Замена на самые встречающиеся буквы в русском языке
            shift = alphabet.index(i) - alphabet.index(common_letter)  # Ключ
            print(Caesar_Decoder(text, shift), "ключ:", shift, "буква:", i)

#Frequency_Decoder("Пэпыютшжэкь юрапчюь юяафуфыофвбо жпбвювэюбвл уыо ргъс")

