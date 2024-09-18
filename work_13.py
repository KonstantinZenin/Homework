import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint
import json
from string import ascii_letters, digits

MAIN_URL: str = "https://books.toscrape.com/"

mark_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}


def definition_file_name() -> str:
    """
    Функция позволяет пользователю ввести название файла,
    в который будут сохранены данные, и проверяет его корректность.
    :return: Строка с названием файла
    """
    name = input("Введите название файла в который сохранятся данные,"
                 "название должно состоять только из латинских букв и цифр и не иметь пробелов и иных знаков!")
    if name[0] not in ascii_letters:
        print("Имя файла должно начинаться с латинской буквы")
        return definition_file_name()
    for letter in name:
        if letter not in ascii_letters and letter not in digits:
            print("Вы ввели некорректное название файла")
            return definition_file_name()
    return name


def definition_parse_next() -> bool:
    """
    Функция позволяет пользователю выбрать будет он собирать данные со всего сайта или с 1 страницы
    :return: bool
    """
    user_input = input("Если вы хотите получить данные с одной страницы то введите \"0\","
                       " иначе введите \"1\".")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Вы ввели не число.")
        return definition_parse_next()
    if user_input > 1 or user_input < 0:
        print("Введите \"0\" или \"1\"!")
        return definition_parse_next()
    else:
        if user_input == 1:
            return True
        else:
            return False


def definition_page() -> int:
    """
    Функция для ввода номера страницы с которой начнёт работать программа
    :return: номер страницы в виде числа
    """
    user_input = input("введите с какой страницы начать собирать данные(всего на сайте 50 страниц)")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Вы ввели не числовое значение."
              "Введите с какой страницы начать собирать данные в виде числа")
        return definition_page()
    if user_input > 50 or user_input < 0:
        print("Такой страницы не существует.")
        return definition_page()
    else:
        return user_input


def create_url() -> str:
    """
    Функция создаёт url из введённого номера страницы
    :return: url
    """
    user_input = definition_page()
    if user_input > 1:
        url: str = f"https://books.toscrape.com/catalogue/page-{user_input}.html"
    else:
        url: str = MAIN_URL
    return url


def create_driver_chrome():
    """
    Функция создает экземпляр веб-драйвера Chrome
    :return: драйвер Chrome
    """
    driver = webdriver.Chrome()
    return driver


def parse_page(driver) -> list:
    """
    Функция собирает данные о книгах на странице
    :param driver: образец драйвера браузера, по умолчанию программа работает с драйвером Chrome
    :return: служебный список selenium с данными карточек книг на странице
    """
    books_on_page = driver.find_elements(By.CLASS_NAME, "product_pod")
    return books_on_page


def parse_book_data(driver, url=MAIN_URL, parse_next=True) -> list[dict]:
    """
    Функция для доступа к сайту, перебора страниц с книгами и формирования списка словарей с данными книг.
    Может работать с определённой страницы, а так же не перелистывать их.
    :param driver: Образец драйвера браузера, по умолчанию программа работает с драйвером Chrome
    :param url: Адрес по которому производится доступ.
    :param parse_next: Отвечает за перелистывание сайта вперёд
    :return: Список словарей с данными карточек книг
    """
    books = []
    driver.get(url)
    sleep(1)
    parse_data = parse_page(driver)
    books_data = create_book(parse_data)
    books.extend(books_data)
    if parse_next:
        while True:
            try:
                nex_button = driver.find_element(By.LINK_TEXT, "next")
                nex_button.click()
                sleep(1)
                parse_data = parse_page(driver)
                books_data = create_book(parse_data)
                books.extend(books_data)
                sleep(1)
            except selenium.common.exceptions.NoSuchElementException:
                break
    return books


def create_book(books) -> list[dict]:
    """
    Функция создаёт список словарей с данными книг
    :param books: Служебный список selenium с данными карточек книг
    :return:
    """
    book_list = []
    for book in books:
        full_title = parse_full_title(book)
        book_url = parse_book_url(book)
        book_cover = parse_book_cover(book)
        book_price = parse_book_price(book)
        book_availability = parse_book_availability(book)
        mark = parse_book_rating(book)
        book_list.append(
            {
                "full_title": full_title,
                "book_url": book_url,
                "book_cover": book_cover,
                "book_price": book_price,
                "book_availability": book_availability,
                "book_rating": mark
            }
        )
    return book_list


def parse_full_title(book) -> str:
    """
    Функция для получения полного названия книги
    :param book: selenium.webdriver.remote.webelement.WebElement
    :return: Строка с названием книги
    """
    full_title = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
    return full_title


def parse_book_url(book) -> str:
    """
    Функция для получения ссылки на страницу книги на сайте
    :param book: selenium.webdriver.remote.webelement.WebElement
    :return: Строка с адресом книги
    """
    book_url = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("href")
    return book_url


def parse_book_cover(book) -> str:
    """
    Функция для получения ссылки на изображение книги
    :param book: selenium.webdriver.remote.webelement.WebElement
    :return: Строка с адресом изображения книги
    """
    book_cover = book.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
    return book_cover


def parse_book_price(book) -> float:
    """
    Функция для получения цены книги
    :param book: selenium.webdriver.remote.webelement.WebElement
    :return: Цена книги
    """
    book_price = float(book.find_element(By.CSS_SELECTOR, "p.price_color").text.lstrip("£"))
    return book_price


def parse_book_availability(book) -> bool:
    """
    Функция для определения доступности книги к покупке
    :param book: selenium.webdriver.remote.webelement.WebElement
    :return: True если книга есть в продаже и False если отсутствует
    """
    book_availability_classes = (book.find_element(By.CSS_SELECTOR, "p.instock").get_attribute("class"))
    book_availability = True if "availability" in book_availability_classes.lower() else False
    return book_availability


def parse_book_rating(book) -> int:
    """
    Функция для определения рейтинга книги в числах
    :param book: selenium.webdriver.remote.webelement.WebElement
    :return: Рейтинг в виде числа от 1 до 5
    """
    str_mark = (book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split(" ")[1])
    mark = mark_dict[str_mark]
    return mark


def save_data(list_books_data: list, file_name: str) -> None:
    """
    Функция для записи данных в файл JSON
    :param list_books_data: Список с данными книг
    :param file_name: Имя файла в который будут сохранены данные
    :return: Отчёт о том сколько книг было сохранено
    """
    json_file_path: str = f"./Data/{file_name}.json"
    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(list_books_data, file, ensure_ascii=False, indent=4)
    return print(f"В файл \"{json_file_path}\" было записано {len(list_books_data)} книг")


def main():
    parse_next = definition_parse_next()
    start_page = create_url()
    file_name = definition_file_name()
    driver = create_driver_chrome()
    books = parse_book_data(driver, parse_next=parse_next, url=start_page)
    pprint(books)
    save_data(books, file_name)


# if __name__ == '__main__':
#     main()
