import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


class GreetingsToQiao:
    def __init__(self):
        self.stopwords = self.get_stopwords('stopwords.txt')
        self.word_frequency = dict()


    @staticmethod
    def get_stopwords(file):
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
        return [line.strip() for line in lines]

    def comments_cut(self, data):
        words = jieba.cut(data)
        for word in words:
            if word not in self.stopwords:
                self.word_frequency[word] = self.word_frequency.get(word, 0) + 1

    def draw_word_cloud(self):
        mask = np.array(Image.open('backgroundpicture.jpg'))
        wc = WordCloud(
            font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
            mask=mask,
            max_words=200,
            max_font_size=100
        )
        wc.generate_from_frequencies(self.word_frequency)
        image_colors = ImageColorGenerator(mask)
        wc.recolor(color_func=image_colors)
        wc.to_file('greeting.jpg')

    def run(self):
        self.comments_cut(comments)
        print(self.word_frequency)
        self.draw_word_cloud()


if __name__ == '__main__':
    Main = GreetingsToQiao()
    Main.run()