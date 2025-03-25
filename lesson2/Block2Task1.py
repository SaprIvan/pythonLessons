first_word = input()
second_word = input()


if sorted(first_word) == sorted(second_word):
    print('Words is same')
else:
    print('Words are different')