from requests import get

class conexion():

    __api_id = ''

    def __init__(self):
        super().__init__()
        self.__api_id = 'ace20b49fb38a51829a45560cbf2311f'

    
    def getClima(self, city):
        city = city.lower()
            
        request = get('https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid={}'.format(city, self.__api_id))
        response = request.json()
        
        if response["cod"] == '404':
            raise ValueError('Provincia "{}" invalida.'.format(city))

        return (response["main"]["temp"], response["main"]["feels_like"], response["main"]["humidity"])