import logging
import random
logging.basicConfig(filename="logging_loto.log", level=logging.INFO)
prosloe = set()
while True:
    logging.info("Включение программы")
    print('Введите номер бочонка')
    try:
        bochonok = int(input())
        logging.info(f"Пользователь ввел {bochonok}")
        if bochonok<=0:
            print('Нужно ввести целое положительное число')
            logging.error("Неправильное число")
            continue
        generated_range = [*range(1, bochonok+1)] #цифры от 1 до введенного номера
        loto = list(set(generated_range) - prosloe)
        loto.sort(key=lambda _: random.random()) #рандомный порядок
        prosloe.add(bochonok)
        for c in loto:
            print(c)
            logging.info(f"Программа вывела {c}")
            input("Нажмите enter")
        logging.info("Конец программы")
    except ValueError:
        print("Нужно ввести целое положительное число")
        logging.error("Неправильное число")
        continue

        
        
