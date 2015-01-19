#-*- coding:utf-8 -*-
import json, urllib2

API_KEY    = os.environ["REKOGNITION_API_KEY"]
API_SECRET = os.environ["REKOGNITION_API_SECRET"]

jobs = 'face_add'

pic_urls = [
    'http://up.gc-img.net/post_img_web/2014/11/QKsfBLucF3igAn3_14625.jpeg',
    'http://geitopi.com/wp-content/uploads/2013101508.jpg',
    'http://news632.com/wp-content/uploads/2014/03/BB3U7fJCAAAW485.jpg',
    'http://livedoor.blogimg.jp/seasoncolor/imgs/c/c/ccaae35d.JPG',
    'http://pic.prepics-cdn.com/72mixjetc/31222966.jpeg'
]

pic_tags = ['nakai','kimura','katori','kusanagi','inagaki']

for i in range(len(pic_urls)):
    url = 'http://rekognition.com/func/api/'
        + '?api_key=' + API_KEY
        + '&api_secret=' + API_SECRET
        + '&jobs=' + jobs
        + '&urls=' + pic_urls[i]
        + '&tag=' + pic_tags[i]
    r = urllib2.urlopen(url)

    print('%d枚目の画像を追加'%(i+1))

jobs = 'face_train'
url = 'http://rekognition.com/func/api/?api_key=' + API_KEY + '&api_secret=' + API_SECRET + '&jobs=' + jobs
r = urllib2.urlopen(url)
root = json.loads(r.read())
print(root)

print('学習完了')
