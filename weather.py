import requests


def Weather(city):
    url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+ '6525acbfea167405e28bfc98db3a1261'
    json_data=requests.get(url).json()  
    format_add=json_data['main']
    
    print('weather is {0} Temp is minimum {1} celcius is {2} nd maximum '.format(
    json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    
    return format_add
