from abc import ABC
from os import getenv
from flask import current_app
from flask_translator.providers.translate_interface import TranslateInterface
import deepl


class Translate(TranslateInterface, ABC):
    def translate(self, text: str, target_language: str) -> str:
        translator = deepl.Translator(getenv('DEEPL_API_KEY'))

        current_app.logger.info("target_language: " + target_language)
        result = translator.translate_text(text, target_lang=target_language)

        return result.text
