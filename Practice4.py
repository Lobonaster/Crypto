def practice4(key="", text=""):
    key = key.replace(" ", "").lower()
    text = text.replace(" ", "").lower()
    alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з','и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у','ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    def operation1(txt,key_):
        while len(key_)<len(txt):
            key_+=key
        result = ""
        for i in range(len(txt)):
            result+=alph[(alph.index(txt[i])+alph.index(key_[i]))%len(alph)]

        return result

    print(operation1(text,key))

practice4("вишня", "лебедев артём романович")

