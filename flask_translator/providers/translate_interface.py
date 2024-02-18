from abc import ABC, abstractmethod


class TranslateInterface(ABC):
    @abstractmethod
    def translate(self, text: str, target_language: str) -> str:
        pass

    @abstractmethod
    def get_target_languages(self):
        pass
