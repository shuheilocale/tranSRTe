import deepl

class Translator():

    def __init__(self, auth_key, target_language='JA') -> None:
        self.translator = deepl.Translator(auth_key)
        self.default_target_language = target_language

    def translate(self, text, target_language=None):

        target_language = target_language or self.default_target_language
        result = self.translator.translate_text(text, target_lang=target_language)
        return result.text



