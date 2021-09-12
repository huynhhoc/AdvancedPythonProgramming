import requests
API_KEY = 'AIzaSyCfKDzIrmmLSyZLq_fHyKzifb_s_4pNDEU'
video_id='7cmvABXyUC0'
url = "https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&part=statistics&key="+API_KEY
response = requests.get(url).json()
print(response)
