from abc import ABC

from flask_translator.providers.translate_interface import TranslateInterface
from google.cloud import translate_v2 as translate


class Translate(TranslateInterface, ABC):
    def translate(self, text: str, target_language: str) -> str:
        translate_client = translate.Client()

        if isinstance(text, bytes):
            text = text.decode('utf-8')

        result = translate_client.translate(text, target_language=target_language)

        return result['translatedText']
