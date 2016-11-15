import random
import urllib.request
def download_image(url):
    name=random.randrange(0,1000)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
download_image('http://st3.cricketcountry.com/wp-content/uploads/2016/08/Joe.jpg')

