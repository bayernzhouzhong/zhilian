import matplotlib.pylab as plt
import pandas as pd
import jieba,numpy
from os import path
from wordcloud import WordCloud,ImageColorGenerator
import imageio,csv


#数据清洗
df1 = pd.read_csv('data.csv', encoding='gbk')
# 数据清洗,剔除实习岗位
df1.drop(df1[df1['emplType'].str.contains('实习')].index, inplace=True)
# 数据处理，工作地址具体地区
df1['city_display'] = df1['city_display'].str.split('-',expand=True)
# 将学历不限的职位要求认定为最低学历:大专
df1['eduLevel'] = df1['eduLevel'].replace('不限', '大专')

pattern = '\d+'
df1.to_csv('data_finall.csv', encoding='gbk',index=False)

df = pd.read_csv('data_finall.csv', encoding='gbk')



# -----------------------------------------------
#数据提取
count=dict(df["city_display"].value_counts())
# print(count)
m = []
for i,j in count.items():
	ss=[i,j]
	m.append(ss)

with open('count.csv', 'w+', newline='') as csvfile:
    fieldnames = ['city_display', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer  = csv.writer(csvfile)
    for row in m:
        writer.writerow(row)
        print(row)

df2 = pd.read_csv('count.csv',encoding='gbk')



#-------------数据图形可视化--------------

# pyplot并不默认支持中文显示，需要rcParams修改字体实现
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['font.serif'] = ['simhei']


#绘制公司类型饼状图
count = df['company_type'].value_counts()
plt.pie(count, labels=count.keys(), labeldistance=1.2, autopct='%2.1f%%')
plt.axis('equal')  # 使饼图为正圆形
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.savefig(r'C:\zhilian\zhilian\shuju\公司类型.png')
plt.show()



#绘制学历要求直方图
dict = {}
for i in df['eduLevel']:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1
index = list(dict.keys())
print('index:',index)
num = []
for i in index:
    num.append(dict[i])
print('num:',num)
plt.bar(index, num, width=0.5)
plt.savefig(r'C:\zhilian\zhilian\shuju\学历要求.png')
plt.show()


#绘制公司分布直方图
dict1 = []
for i in df2['city_display'][:10]:
    dict1.append(i)
dict2 = []
for j in df2['count'][:10]:
    dict2.append(j)
plt.bar(dict1,dict2,width=0.5)
plt.savefig(r'C:\zhilian\zhilian\shuju\公司主要分布.png')
plt.show()




#----------wordcloud词云----------
text = ''
for line in str(df['welfare']):
    text += line
cut_text = ''.join(text)                                            # 提取公司福利字段进字符串
jieba.load_userdict("userdict.txt")                                 # 自定义用户字典，减小容错
# old_text = ''.join(jieba.cut(cut_text,cut_all=False, HMM=True))     # 不采用全模式，精确模式

d = path.dirname(__file__)

mylist = [cut_text]
word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)                                      # 字符串
imagename = path.join(d, "timg.jpg")                                # 路径选择图片
coloring = imageio.imread(imagename)                                # 读取背景图片 image将在scipy1.2被移除
graph = numpy.array(coloring)

wordcloud = WordCloud(mask=coloring,font_path='msyh.ttc',background_color='black').generate(new_text)# 微软雅黑字体，背景颜色白色


plt.imshow(wordcloud)
image_color = ImageColorGenerator(graph)                            # 从背景图片生成颜色值
plt.imshow(wordcloud.recolor(color_func=image_color))               # 绘制背景图片为主色调的图片
plt.imshow(wordcloud)               # 绘制背景图片为颜色的图片

plt.axis("off")
plt.show()

wordcloud.to_file(r'C:\zhilian\zhilian\shuju\公司福利.jpg')