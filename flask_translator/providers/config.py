from flask_translator.providers.google.translate import Translate as GoogleTranslate
from flask_translator.providers.deepl.translate import Translate as DeeplTranslate
from flask_translator.providers.translate_interface import TranslateInterface


def proxy_provider(name) -> TranslateInterface:
    translate_providers = {
        'google': GoogleTranslate,
        'deepl': DeeplTranslate,
    }

    if name in translate_providers:
        translator_class = translate_providers[name]

        return translator_class()
    else:
        raise ValueError('Translate provider not found: {}'.format(name))
