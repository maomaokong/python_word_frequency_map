#!/usr/bin/python

"""
Import Packages / Libraries
"""
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from my_constants import Config as cfg
from my_constants import Environment as env


def main():
    hm_data = pd.read_csv(
        '{pp}/{pd}/{fn}'.format(
            pp=cfg.PATH_PARENT
            , pd=cfg.PATH_DATA
            , fn=cfg.DATA_HM
        )
    )
    df_hm = hm_data[hm_data['cleaned_hm'].notnull()]
    #print(df_hm)

    text = ' '.join(df_hm['cleaned_hm'].tolist())
    text = text.lower()
    for word in cfg.LIMIT_WORDS:
        text = text.replace(' ' + word, '')
        text = text.replace(word + ' ', '')

    wordcloud = WordCloud(
        background_color='white'
        , font_path='{fp}/{fn}'.format(fp=cfg.PATH_FONT, fn=cfg.FONT_ARIAL)
        , height=2700
        , width=3600
    ).generate(text)
    plt.figure(figsize=(14, 8))
    plt.imshow(
        wordcloud.recolor(colormap=plt.get_cmap('Set2'))
        , interpolation='bilinear'
    )
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
