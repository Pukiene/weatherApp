
import urllib.request
import json

from time import sleep

while True:

    # Open remote URL
    f = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=Wolverhampton&units=metric&appid=050af488d34eebfda6d5bd119f3a662b')

    # Read content and convert to JSON object
    content = f.read()
    content = json.loads(content.decode('utf-8'))

    weather = content['weather'][0]['description']
    temperature = content ['main']['temp']
    humidity = content ['main']['humidity']
    print('=========================')
    print('The weather in Wolverhampton is:' , weather)
    print('The temperature in Wolverhampton is:' , temperature, '°C ')
    print('The humidity in Wolverhampton is:' , humidity, '%')

    sleep(3)
