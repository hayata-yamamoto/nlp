import gensim
from gensim import matutils, models


class Vectorizer:
    """
    Bag of Wordsベースのベクトル化クラス
    """

    def __init__(self, tf_idf: bool = False, normalize=False):
        """

        Args:
            tf_idf:
            normalize:
        """
        self.dictionary = None
        self.tf_idf = tf_idf
        self.normalize = normalize

    def set_dictionary(self, dictionary: gensim.corpora.Dictionary) -> None:
        """
        Args:
            dictionary (gensim.corpora.Dictionary) : 辞書

        Returns:
            None
        """
        if type(dictionary) is not gensim.corpora.Dictionary:
            raise TypeError('dictionary must be gensim.corpora.Dictionary.')
        self.dictionary = dictionary

    def __get_corpus(self, tokens: list) -> list:
        """
        Bag of Wordsを使ったコーパスを作成する
        Args:
            tokens (list) : 分かち書きされた文字列のリスト

        Returns:
            list
        """

        return [corpus for corpus in self.dictionary.doc2bow(tokens)]

    def __embedding(self, corpus: list) -> list:
        """
        単語を埋め込む
        Args:
            corpus (list) : 辞書から作成されたコーパス

        Returns:
            list
        """
        return list(matutils.corpus2dense([corpus], num_terms=len(self.dictionary)).T[0])

    def vectorize(self, sentences: list) -> list:
        """
        分かち書きされた文字列からコーパスを作成してベクトル化する
        Args:
            sentences (list) : 文字列のリスト

        Returns:
            list
        """

        corpora = [self.__get_corpus(sentence) for sentence in sentences]
        if self.tf_idf:
            model = models.TfidfModel(corpus=corpora, normalize=self.normalize)
            return [model[corpus] for corpus in corpora]
        return [self.__embedding(corpus) for corpus in corpora]
