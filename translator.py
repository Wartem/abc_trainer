from settings import Settings

language_code_to_language_name = {
    "sv": "Swedish",
    "fr": "French",
    "es": "Spanish",
    "pt": "Portuguese",
    "de": "German",
    "it": "Italian",
    "da": "Danish",
    "no": "Norwegian",
    "fi": "Finnish",
    "pl": "Polish",
    "nl": "Dutch",
    "en": "English",
    "af": "Afrikaans",
    "sq": "Albanian",
    "eo": "Esperanto",
    "et": "Estonian",
    "hr": "Croatian",
    "ht": "Haitian Creole",
    "hu": "Hungarian",
    "id": "Indonesian",
    "is": "Icelandic",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "ro": "Romanian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "tl": "Tagalog",
    "cs": "Czech",
    "tr": "Turkish",
    "vi": "Vietnamese"
}

language_name_to_language_code = {
    "Swedish": "sv",
    "French": "fr",
    "Spanish": "es",
    "Portuguese": "pt",
    "German": "de",
    "Italian": "it",
    "Danish": "da",
    "Norwegian": "no",
    "Finnish": "fi",
    "Polish": "pl",
    "Dutch": "nl",
    "English": "en",
    "Afrikaans": "af",
    "Albanian": "sq",
    "Esperanto": "eo",
    "Estonian": "et",
    "Croatian": "hr",
    "Haitian Creole": "ht",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Icelandic": "is",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Romanian": "ro",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Tagalog (Filipino)": "tl",
    "Czech": "cs",
    "Turkish": "tr",
    "Vietnamese": "vi"
}

class Translator:
    def __init__(self):
        self.langs = Settings.r_instructions()


    def find(self, command, lang="English"):
        return self.langs[lang][command]
    
    
    def get_code(self, lang="English"):
        return language_name_to_language_code[lang]


    def keys(self):
        return self.langs.keys()
    
    
    def tr(self, command, lang):
        """Returns a command, translated from English to set language.

        Args:
            command (str): String in English

        Returns:
            str: String translated to set language. 
        """        
        return self.find(command, lang)