import requests
import os.path


API = 'trnsl.1.1.20170612T092844Z.3dcd61750a7d75da.c6b01f07b225444678a712a42d48f793185fe344'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def get_translations(text, from_lang, to_lang='ru'):
    params = dict(
        key=API,
        text=text,
        lang='{}-{}'.format(from_lang, to_lang)
    )

    response = requests.get(url=URL, params=params)

    return response


def translate():

    result = 'Result'
    if not os.path.exists(result):
        os.mkdir('Result')

    from_lang = input('Какой текст перевести?\n de - немецкий\n es - Испанский\n fr - французский\n')

    if from_lang == 'de':
        lang_file = 'DE.txt'
    elif from_lang == 'es':
        lang_file = 'ES.txt'
    elif from_lang == 'fr':
        lang_file = 'FR.txt'

    with open(os.path.join(os.getcwd(), lang_file), 'r') as text:
        text = text.read()

    to_lang = input('На какой язык перевести?\nru - русский\nen - английский\n')

    resp = get_translations(text, from_lang, to_lang)

    response_text = resp.json()

    with open(os.path.join(os.getcwd(), 'Result', from_lang + '-to-' + to_lang + '.txt'), 'w') as f:
        for i in response_text['text']:
            f.write(i)


translate()
