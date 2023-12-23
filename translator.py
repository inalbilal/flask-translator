import logging
import os
import yaml
from flask import current_app, session, request, Flask


class Translator(object):
    def __init__(self, app=None):
        self._language = None
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        self._set_default_config(app)

        app.before_request(self._get_locale)

    def translate(self, key: str, **kwargs):
        try:
            data = self._get_file_data()

            value = data
            for k in key.split('.'):
                value = value[k]
            for k, v in kwargs.items():
                value = value.replace('{' + k + '}', str(v))

            return value

        except Exception as e:
            logging.error(e)
            return current_app.config['DEFAULT_MESSAGE']

    # Initialize from ISO 639-1 code standards

    def _get_locale(self):
        lang_initializer = current_app.config['LANG_INITIALIZER']

        if lang_initializer == 'headers':
            self._language = request.headers.get('Accept-Language')
        elif lang_initializer == 'cookies':
            self._language = request.cookies.get('language')
        elif lang_initializer == 'sessions':
            self._language = session.get('language')

        self._language = self._language or current_app.config['DEFAULT_LANG']

    def _get_file_data(self):
        translation_file = os.path.join(current_app.root_path, current_app.config['TRANSLATIONS_PATH'],
                                        f'messages.{self._language}.yaml')

        with open(translation_file, 'r') as file:
            data = yaml.safe_load(file)

        return data

    @staticmethod
    def _set_default_config(app: Flask):
        app.config.setdefault('DEFAULT_LANG', 'en')
        app.config.setdefault('LANG_INITIALIZER', 'headers')
        app.config.setdefault('TRANSLATIONS_PATH', 'translations')
        app.config.setdefault('DEFAULT_MESSAGE', 'Process finished!')
