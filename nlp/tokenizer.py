import MeCab
from typing import Union


class Tokenizer:
    """
    This module is parsing sentence to several tokens.
    For example,
        >>> sentence = '私は、トムです。'
        >>> tokenizer = Tokenizer()
        >>> tokenizer.parse(sentence)
        ['私', 'は', '、', 'トム', 'です', '。']
    """

    def __init__(self, neologd=True):
        """
        Args:
            neologd (True) : mecab-ipadic-neologdを使うかどうか
        """
        if neologd:
            self.tagger = MeCab.Tagger(
                '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        else:
            self.tagger = MeCab.Tagger('-Ochasen')
        self.tagger.parse('')

    def __get_morphemes(self, sentence: str):
        return self.tagger.parseToNode(sentence)

    def parse(self, sentence: str, condition: Union[None, list] = None) -> list:
        """
        文章を分かち書きして、返すメソッド
        infoをTrueにすると、品詞情報も返します。

        Args:
            sentence (str) : 文章
            condition (None or list): 取得したい品詞名

        Returns:
            list
        """

        # todo: 品詞情報のエラー処理を書く
        node = self.__get_morphemes(sentence)
        morphemes = []
        i = 0
        # todo: 再帰関数を使ってかける？
        while node.next:

            # 一行目に形態素は現れない
            if i == 0:
                i += 1
                node = node.next
                continue

            # 品詞情報のフィルターが不要な場合の処理
            # conditionにリストを渡すとここで上に戻る
            if condition is None:
                morphemes.append(node.surface)
                node = node.next
                continue

            # 品詞情報でフィルターをかけたい時
            parts = node.feature.split(',')[0]
            if parts in condition:
                # TODO: もっと純度の高いデータを取得するなら、node.feature.split(',')[6]を使う。（単語の原形が記載されているため）
                morphemes.append(node.surface)
                node = node.next
                continue
            node = node.next
        return morphemes


if __name__ == '__main__':
    print(
        Tokenizer().parse(
            "七月のはじめ、めっぽう暑いさかりのある日ぐれどき、ひとりの青年が、S横町のせまくるしい間借り部屋(まがりべや)からおもてに出て、のろくさと、どこかためらいがちに、K橋のほうへ歩きだした。 "
            "青年はうまいこと階段で下宿の主婦(おかみ)と出くわさずにすんだ。"
            "彼の部屋は、五階建ての高い建物をのぼりつめた屋根裏(うら)にあり、部屋というより押入れに近かった。"
            "おまけに階段ひとつ下が、まかないと女中つきでここを彼に貸している主婦(おかみ)の住居(すまい)なので、"
            "青年は外出のたび、たいてい階段のほうに向けてあけはなしになっている主婦の台所のわきを、いやでも通らなければならなかった。"
            "青年は毎度、そこを通るたびに、一種病的な気おくれにとらわれ、それがわれながら恥ずかしく、顔をしかめた。"
            "主婦(おかみ)にたいそう借りがあるので、顔を合わすのがこわかったのである。 ", condition=[
                '名詞', '動詞']))
