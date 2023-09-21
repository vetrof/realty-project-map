import pickle

import requests
from bs4 import BeautifulSoup

from tbot.models import DataCall
from tbot.views import my_test_view



def parsing():

    # Отправляем GET-запрос к странице
    url = "https://krisha.kz/arenda/kvartiry/astana/"
    response = requests.get(url)

    with open('flats', 'rb') as file:
        flats = pickle.load(file)

    # flats = {}

    flats_new = {}
    print('********** test *************')

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для анализа HTML-кода страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все объявления на странице (предположим, что объявления находятся в блоках с классом "a-card")
        ad_blocks = soup.find_all('div', class_='a-card')

        # Итерируемся по блокам объявлений и извлекаем информацию
        for ad_block in ad_blocks:
            # Извлекаем текст ссылки
            link = ad_block.find('a', href=True, text=lambda text: text and 'квартира' in text.lower())
            link_text = link.text.strip() if link else "Ссылка не найдена"

            # Извлекаем URL ссылки
            link_url = link['href'] if link else "URL не найден"

            # Извлекаем цену (предположим, что цена находится в элементе с классом "a-card__price")
            price_element = ad_block.find('div', class_='a-card__price')
            price = price_element.text.strip() if price_element else "Цена не найдена"

            # Выводим информацию
            # print(f"Текст ссылки: {link_text}")
            # print(f"URL ссылки: https://krisha.kz{link_url}")
            # print(f"Цена: {price}")
            # print()


            if link_url in flats:
                ...
            else:
                # print('******** NEW Link ***********')
                # print(f"Текст ссылки: {link_text}")
                # print(f"URL ссылки: https://krisha.kz{link_url}")
                # print(f"Цена: {price}")
                # print()
                flats_new[link_url] = [link_text, price]

            flats[link_url] = [link_text, price]


    else:
        print("Не удалось получить доступ к странице.")

    with open('flats', 'wb') as file:
        pickle.dump(flats, file)

    print('******** Old Link ***********')

    # for i in flats:
    #     print(f'https://krisha.kz{i}', flats[i])

    print(len(flats))

    # if len(flats_new) < 1:
    #     flats_new[''] = ['квартир', 'нет']

    DataCall().save()
    my_test_view(flats_new)

    return flats_new

