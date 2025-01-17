"""
Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя и возвращает его в качестве строки

get_domain_name("http://google.com") => "google"
get_domain_name("http://google.co.jp") => "google"
get_domain_name("www.xakep.ru") => "xakep"
get_domain_name("https://youtube.com") => "youtube"
get_domain_name("https://www.asos.com") => "asos"
get_domain_name("http://www.lenovo.com") => "lenovo"

Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://  https://, могут также содержать www.
"""
import re

def get_domain_name(url):
    """
    Извлекает доменное имя из URL-адреса.

    Args:
        url: Строка URL.

    Returns:
        Доменное имя в виде строки.
    """
    # Удаляем протокол (http://, https://) и www
    url = re.sub(r'^(https?://)?(www\.)?', '', url)
    # Извлекаем доменное имя (берем первую часть до точки, после удаления протокола и www)
    domain = url.split('.')[0] if '.' in url else url
    return domain

# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')

"""
как вариант без импортов
"""


def get_domain_name(url):
    """
    Извлекает доменное имя из URL-адреса (без использования re).

    Args:
        url: Строка URL.

    Returns:
        Доменное имя в виде строки.
    """
    # Удаляем протокол (http://, https://)
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]

    # Удаляем www.
    if url.startswith("www."):
        url = url[4:]

    # Извлекаем доменное имя (берем первую часть до точки)
    if "." in url:
        domain = url.split(".")[0]
    else:
        domain = url
    return domain


# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") == 'github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')