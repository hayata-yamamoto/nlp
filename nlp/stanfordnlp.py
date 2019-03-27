import stanfordnlp
from typing import Dict


class StanfordNLP:
    def __init__(self):
        self.nlp = stanfordnlp.Pipeline()

    def download(self, model=''):

    def parse_sentence(self, sentence: str) -> Dict:
        result: Dict = {
            'word': [],
            'dependency_relation': [],
            'xpos': [],
            'upos': [],
            'lemma': [],
            'feature': [],
            'governor': [],
            'text': [],
            'parent_token': [],
            'index': []
        }
        for word in self.nlp(sentence).sentences[0].words:
            words


        return result