import re
import mojimoji


class Cleaner:
    def __init__(
            self,
            stopwords: list = None,
            number_to: str = '0',
            symbol_to: str = '0',
            lower_string: bool = True,
            half_string: bool = True):
        """
        テキストを掃除する人
        Args:
            stopwords (list or None) : いらない文字列のリスト
            symbol_to (str) : 統一する記号
            number_to (str) : 統一する数字
            lower_string (bool) : 大文字、小文字の選択
            half_string (bool) : 半角全角の選択
        """
        self.stopwords = stopwords
        self.symbol_to = symbol_to
        self.number_to = number_to
        self.lower_string = lower_string
        self.half_string = half_string

    def lower(self, token: str) -> str:
        """
        string to lower case
        Args:
            token (str) : 文字列

        Returns:
            str
        """
        if self.lower_string:
            return token.lower()
        return token.upper()

    def half(self, token: str) -> str:
        """
        string to half case
        Args:
            token (str) : 文字列

        Returns:
            str
        """
        if self.half_string:
            return mojimoji.zen_to_han(token)
        return mojimoji.han_to_zen(token)

    def replace_numbers(self, token: str) -> str:
        """

        Args:
            token (str) :

        Returns:
            str
        """
        return re.sub(r'\d', self.number_to, token)

    def replace_symbol(self, token: str) -> str:
        """

        Args:
            token (str) :

        Returns:
            str
        """
        return re.sub('[!-/:-@[-`{-~]', self.symbol_to, token)

    def remove_stopwords(self, token: str) -> str:
        """
        トークンの集合から、
        ストップワード（よく出るけどそれほど重要じゃない単語）や
        記号、数字などのリストを渡して削除する
        Args:
            token (str) : 分かち書きされた単語たち

        Returns:
            str
        """
        if self.stopwords is None:
            raise AttributeError('No stop-word list')
        if token in self.stopwords:
            return ''
        return token

    @staticmethod
    def strip_blank(token: str) -> str:
        """
        文字列の中の空白を無くす
        Args:
            token (str) : 文字列

        Returns:
            str
        """
        token = token.replace('　', '')
        return token.replace(' ', '')

    @staticmethod
    def check_empty(token: str) -> bool:
        """
        文字列が空かどうかを判定する
        Args:
            token (str) : str

        Returns:
            bool
        """
        return token == ''
