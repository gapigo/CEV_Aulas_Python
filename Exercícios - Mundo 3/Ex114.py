import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Deu certo')
