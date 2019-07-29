import json,csv
from urllib.request import urlopen, quote

def getlnglat(address):
    url0 = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'coGuf2YtBTE0WpGuMLGedBgdIePsBp1a' #'你申请的密钥***'
    add = quote(address) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    url1 = url0 + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak
    req = urlopen(url1)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

file = open(r'c:/zhilian/zhilian/shuju/point.json','w+') #建立json数据文件
with open(r'../../count.csv', 'r') as csvfile: #打开csv
    reader = csv.reader(csvfile)
    next(csvfile)
    for line in reader: #读取csv里的数据
            b = line[0].strip() #将第一列city读取出来并清除不需要字符
            c = line[1].strip()#将第二列price读取出来并清除不需要字符
        #     b = line[0].strip(['city_dispaly']) #将第一列city读取出来并清除不需要字符
        #     c = line[1].strip(['count'])#将第二列price读取出来并清除不需要字符
            lng = getlnglat(b)['result']['location']['lng'] #采用构造的函数来获取经度
            lat = getlnglat(b)['result']['location']['lat'] #获取纬度
            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
            print(str_temp)#输出json格式的经纬度
            file.write(str_temp) #写入文档
file.close() #保存