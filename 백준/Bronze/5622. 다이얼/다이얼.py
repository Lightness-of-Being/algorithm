alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']

alphabet_dict = {
    
}
for alphabet, index in zip(alphabet_list, range(26)):
    if index < 3:
        alphabet_dict[alphabet] = 3
    elif index < 6:
        alphabet_dict[alphabet] = 4
    elif index < 9:
        alphabet_dict[alphabet] = 5
    elif index < 12:
        alphabet_dict[alphabet] = 6
    elif index < 15:
        alphabet_dict[alphabet] = 7
    elif index < 19:
        alphabet_dict[alphabet] = 8
    elif index < 22:
        alphabet_dict[alphabet] = 9
    else:
        alphabet_dict[alphabet] = 10
input_ = input().lower()
res = 0
for i in input_:
    res += alphabet_dict[i]
print(res)
