from time import sleep
print('-=-'*20)
sleep(0.5)
print('Analisador de triângulos')
sleep(0.5)
print('-=-'*20)
sleep(0.5)
a = float(input('1° lado: '))
b = float(input('2° lado: '))
c = float(input('3° lado: '))
if a+b > c:
    if a+c > b:
        if b+c > a:
            print('Esse triângulo pode existir.')
else:
    print('Esse triângulo não pode existir.')
input()