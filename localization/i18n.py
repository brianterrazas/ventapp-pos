from . import es, en

class Translator:
    def __init__(self, lang="es"):
        self.languages = {
            "es": es.translations,
            "en": en.translations
        }
        #seteo por defecto espanol
        self.set_language(lang)

    #metodo para elegir el language
    def set_language(self, lang):
        self.current_lang = self.languages.get(lang, es.translations)

    #metodo para recuperar la palabra
    def t(self, key):
        return self.current_lang.get(key, f"[{key}]")

#creamo ya la instancia, de manera que con el import se genere solo y no tengamos que isntanciar la clase en el otro .py
translator = Translator()