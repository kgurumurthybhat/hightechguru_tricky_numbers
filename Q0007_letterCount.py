# Solution in python - How many letters?
from num2words import num2words


def letter_count():
    number_list = []
    n = int(input("Enter the number to count : "))
    for i in range(1, n + 1):
        number_list.append(num2words(i))
    print(number_list)
    count = 0
    k = 0
    for m in range(0, n):
        count += count_letters(number_list[k])
        k += 1
    print(count)


def count_letters(word):
    return len(word) - word.count(' ') - word.count('-')


letter_count()