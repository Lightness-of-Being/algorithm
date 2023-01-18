Croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_ = input()
cnt = 0
for i in Croatian_alphabet:
    input_ = input_.replace(i, ' ')

print(len(input_))