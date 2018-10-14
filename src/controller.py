import requests

class CarController:
    HOST = 'http://raspberrypi.local'
    PORT = '8000'
    BASE_URL = HOST + PORT

    def __init__(self):
        
    #login

    def change_direction():

    def change_speed(speed):
    """
    :param speed: The speed to be set
    :type speed: int, float
    :where: speed is in range (0, 100)
    """

    def move_cam():

    def run_action(self, cmd):
        requests.get()

    def check_connection():
    """
    Check whether connection is working,
    server will respond with 'ok'
    :return: 
        True if connection ok,
        False if no connection
    :rtype: bool
    """
    loc = 'connection_test'
    url = BASE_URL + loc
    try:
        r=requests.get(url)
        if r.text == 'OK':
            return True
    except e as Exception:
        return False
