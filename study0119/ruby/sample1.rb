require 'rekognize'

client = Rekognize::Client::Base.new(api_key: ENV['REKOGNITION_API_KEY'], api_secret: ENV['REKOGNITION_API_SECRET'])

jobs = 'face_recognize'
pic_url = 'http://pic.prepics-cdn.com/nakai0818/27014912.jpeg'

puts client.face_detect(
  urls: 'http://pic.prepics-cdn.com/nakai0818/27014912.jpeg',
  jobs: 'face_detect'
)

