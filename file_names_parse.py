#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import io
import os
import locale

os.environ["PYTHONIOENCODING"] = "utf-8"
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")

base_dir = os.path.dirname(__file__)
files = os.listdir('.')

def get_height_width(height_widh):
    hw = height_widh.split('-')

    if hw[0] >= hw[1]:
        height, weigh = hw[0], hw[1]
    else:
        height, weigh = hw[1], hw[0]
    return height, weigh

def file_generate(jpg_file_name, params):
    print(jpg_file_name)
    file_name = jpg_file_name[:-5] + '.txt'
    os.makedirs(os.path.join(base_dir, 'out'), exist_ok=True)
    with io.open(os.path.join(base_dir, 'out', file_name), 'w') as file:
        file.write('Репродукция(1909г). {}. {} \n\
Продается репродукция(гелиогравюра, фототипия) издательства Кнебель. Из собрания "Московская государственная художественная галерея Третьяковых"\n \
Автор: {}\n\
Название произведения: {}\n\
Размер холста:{} на {} см.\n\
Размер внутренней рамки:{} на {} см.\n\
Размер картины:{} на {} см.\n\
Год издания: 1909 г.\n\
Цена: 600 рублей\n\
Отличный приобретение в подарок или для украшения интерьера - останется купить паспарту и рамку(стоят не дорого). \n\
Остальные работы вы можете посмотреть в профиле. Возможнжа покупка всего комплекта (20 выпусков. 2 из них неполных)\
                  '.format(
            params['author'],
            params['title'],
            params['author'],
            params['title'],
            params['pic_height'],
            params['pic_wight'],
            params['big_height'],
            params['big_wight'],
            params['small_height'],
            params['small_wight']
            ))
        file.close()

def get_params(filename):
    params = {}
    _, num, pic_size, bigHW , smallHW, author, title = filename.split('_')
    big_hw = get_height_width(bigHW)
    small_hw = get_height_width(smallHW)
    pic_size = get_height_width(pic_size)
    params['pic_height'] = pic_size[0]
    params['pic_wight'] = pic_size[1]
    params['big_height'] = big_hw[0]
    params['big_wight'] = big_hw[1]
    params['small_height'] = small_hw[0]
    params['small_wight'] = small_hw[1]
    params['author'] = '{}.{}. {}'.format(author[0], author[1], author[2:].title())
    params['title'] = title.split('-')[1]
    return params

def main():
    for file in files:
        re_out = re.search(r'Выпуск_\d{1,}_\d{2}-\d{2}_\d{2}-\d{2}_\w+', file)
        if re_out:
            # File example: Выпуск_2_51-40_40-29_35-21_ИЕРЕПИН_-Крестный ход в Курской губернии-.JPG
            params = get_params(file)
            file_generate(file, params)

if __name__ == "__main__":
    main()