import requests
                                                                                         
API_KEY = "d0d0ca21373119bfc5ac0e2b58e11589"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data ['cod']  != 200:
        return(f"City '{city}' not found! Please check the spelling.")
    else:
        temp = data ['main'] ['temp']
        fells_like = data ['main'] ['feels_like']
        humidety = data ['main'] ['humidity']
        description = data ['weather'] [0] ['description']
        wind = data ['wind'] ['speed']
        return(    
        f'\n Weather in {city}:'    
        f'\n Temperature, {temp} °C'
        f'\n Feels like , {fells_like} °C'
        f'\n Humidity, {humidety} %'
        f'\n Description,{description}'
        f'\n Wind speed,{wind} m/s'
    )
if __name__ =='__main__':
    while True:
        city = input('Input city name:')

        if city.lower() =='quit':
            print('Goodbye.')
            break
        print(get_weather(city))