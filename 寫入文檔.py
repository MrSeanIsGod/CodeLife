numbers = list(range(1, 11))
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
reverse_numbers = list(range(10, 0, -1))
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

data = [numbers, letters, reverse_numbers, lowercase_letters]

for seq in data:
    print(' '.join(map(str, seq)))

with open('data.txt', 'w', encoding='utf-8') as file:
    for seq in data:
        file.write(' '.join(map(str, seq)) + '\n')
