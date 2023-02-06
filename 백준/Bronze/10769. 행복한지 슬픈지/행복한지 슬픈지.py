happy = ':-)'
sad = ':-('
string = input()
cnt = 0
cnt_happy = string.count(':-)')
cnt_sad = string.count(':-(')
if cnt_happy > cnt_sad:
    print('happy')
elif cnt_happy < cnt_sad:
    print('sad')
elif cnt_happy == cnt_sad == 0:
    print('none')
elif cnt_happy == cnt_sad :
    print('unsure')