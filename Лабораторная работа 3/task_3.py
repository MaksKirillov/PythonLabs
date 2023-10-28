def count_letters(text):
    dict_of_letters = {}
    lower_text = text.lower()
    for _, char in enumerate(lower_text):
        if not char.isalpha():
            continue
        if char not in dict_of_letters:
            dict_of_letters[char] = 0
        dict_of_letters[char] += 1
    return dict_of_letters


def calculate_frequency(dict_of_letters):
    sum_of_letters = sum(dict_of_letters.values())
    new_dict_of_letters = {}
    for char, count in dict_of_letters.items():
        new_dict_of_letters[char] = round(count / sum_of_letters, 2)
    return new_dict_of_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

frequency_of_letters_dict = calculate_frequency(count_letters(main_str))
for letter, frequency in frequency_of_letters_dict.items():
    print(f"{letter}: {frequency:.2f}")
