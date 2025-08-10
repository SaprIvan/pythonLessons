class Decrement:
    number = 0

    def decrement(self):

       self.number -= 1


decrement = Decrement()
decrement.number = 2
decrement.decrement()

if decrement.number == 1:
    print('Верный результат')
else:
    print('Неверный результат')