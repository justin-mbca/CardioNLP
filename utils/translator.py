from googletrans import Translator

def translate_text(text, target='zh-cn'):
    translator = Translator()
    return translator.translate(text, dest=target).text

