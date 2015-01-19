#-*- coding:utf-8 -*-
import json, urllib2

API_KEY    = os.environ["REKOGNITION_API_KEY"]
API_SECRET = os.environ["REKOGNITION_API_SECRET"]

jobs = 'face_age_beauty'
pic_url = 'http://pic.prepics-cdn.com/smapphoto/12756846.jpeg'
url = 'http://rekognition.com/func/api/?api_key=' + API_KEY + '&api_secret=' + API_SECRET + '&jobs=' + jobs + '&urls=' + pic_url

r = urllib2.urlopen(url)
root = json.loads(r.read())

print(root)
print(root[u'face_detection'][0][u'age'])
print(root[u'face_detection'][0][u'beauty'])
