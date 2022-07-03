'''Комп сам загадывает и сам угадывает'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    '''Сначала устанавливаем границы и находим середину между ними'''

    x = 1
    y = 100
    predict = (x+y) // 2 #находим середину между границами, которая будет предполагаемым числом
    count = 1

    while number != predict: #если предполагаемое число не равно загаданному
        count += 1 #считаем попытки
        if number > predict: #если загаданное число больше, то меняем границу, сдвигаясь на +1 от предполагаемого числа
            x = predict + 1
            predict = (x+y) // 2
        else: #если загаданное число меньше, то меняем границу, сдвигаясь на -1 от предполагаемого числа
            y = predict - 1
            predict = (x+y) // 2
    return(count) #возвращаем кол-во попыток




def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == "__main__":

    #print(f'Количество попыток: {random_predict(10)}')
    #print(f'Количество попыток: {random_predict()}')

    # RUN
    score_game(random_predict)