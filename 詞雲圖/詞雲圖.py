import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import random
from palettable.colorbrewer.sequential import YlGnBu_9
text = open('test.txt', 'r', encoding='UTF-8-sig').read()#文字檔
text='-'.join(jieba.cut(text))
icon_path = 'comment.png'#圖檔
icon = Image.open(icon_path)
mask=Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon, icon)
mask = np.array (mask)
font_path='SNsanafonGyou.ttf'

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple ([255,255,255])

wc=WordCloud(font_path=font_path, background_color="black", max_words=2000, \
             mask=mask, max_font_size=300, random_state=1)
wc.generate_from_text(text)
wc.recolor(color_func=color_func, random_state=2)

output_path = 'wordcloud.png'
wc.to_file(output_path)
fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)
plt.rcParams["figure.figsize"] = (10,10)
plt.imshow(wc)