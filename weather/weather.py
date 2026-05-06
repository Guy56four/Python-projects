import requests

API_KEY = "d0d0ca21373119bfc5ac0e2b58e11589"
while True:
    city = input('Input city name:')

    if city.lower() =='quit':
        print('Goodbye.')
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()


    if data ['cod']  != 200:
        print(f"City '{city}' not found! Please check the spelling.")
    else:
        temp = data ['main'] ['temp']
        fells_like = data ['main'] ['feels_like']
        humidety = data ['main'] ['humidity']
        description = data ['weather'] [0] ['description']
        wind = data ['wind'] ['speed']

        print(f'\n Weather in {city}:')
        print(f'\n Temperature, {temp} °C')
        print(f'\n Feels like , {fells_like} °C')
        print(f'\n Humidity, {humidety} %')
        print(f'\n Description,{description}')
        print(f'\n Wind speed,{wind} m/s')


