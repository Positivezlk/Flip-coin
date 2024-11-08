import random

def flip_coin():
    result = random.choice(["Орел", "Решка"])
    return result

print('ЧТОБЫ ОСТАНОВИТЬ РАБОТУ ПРОГРАММЫ, НАПИШИТЕ "stop"')
while True:
    _ = input('НАЖМИТЕ НА ENTER, ЧТОБЫ ПОДБРОСИТЬ МОНЕТУ: ')
    if _ == 'stop':
        break
    flip = flip_coin()
    print(f"Результат: {flip}")
