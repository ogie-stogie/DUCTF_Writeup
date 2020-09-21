import sys
import string

enc_msg = r"Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj"
index = 0
dec_msg = ""
for letter in enc_msg:
    letter_value = ord(letter)
    # if (letter_value < 65) or (letter_value > 148):
    #     dec_msg += letter
    #     index = index + 1
    #     continue
    if letter_value in [32, 39, 95, 33, 123, 125]:
        new_letter_value = letter_value
    elif letter_value < 97:
        new_letter_value = letter_value - ( index % 26 )
        if new_letter_value > 122:
            new_letter_value = letter
        elif new_letter_value < 65:
            new_letter_value = new_letter_value + 26
    else:
        new_letter_value = letter_value - ( index % 26 )
        if new_letter_value < 97:
            new_letter_value = new_letter_value + 26
    new_letter = chr(new_letter_value)
    dec_msg += new_letter
    index = index + 1

print(dec_msg)