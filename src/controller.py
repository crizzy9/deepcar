import requests
import logging

FORMAT = '%(asctime)s [%(levelname)s] %(name)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

class Controller:
    """
    This class contacts the car server on the raspberry pi and sends
    corresponding action requests which is responsible for making the car move
    N.B. This is only a controller class without any gui
    TL;DR This class is used to control the car programatically
    """

    HOST = 'http://raspberrypi.local'
    PORT = '8000'
    BASE_URL = '' 

    def __init__(self, host=None, port=None):
        logging.info('Controller initiated!')
        
        if host is not None:
            HOST = host
        if port is not None:
            PORT = port
        
        BASE_URL = '{}:{}'.format(HOST, PORT)
        # is login really needed? differnt story if its password protected
        # can use connection_ok
        self.__login__()
        # calibrate
        
    """
    To simulate a real driving experience these functions will pretty much
    recreate the controls on a real car like
        - Accelerate (should it be with speed?) (start with constant speed first)
        - Brake
        - Reverse
        - Go Straight
        - Turn Left
        - Turn Right (Could give angles too in the future)
    """
    def accelerate(self):
        self.__action('forward')

    def brake(self):
        self.__action('stop')

    def reverse(self):
        self.__action('backward')

    def go_straight(self):
        self.__action('fwstraight')

    def turn_left(self):
        self.__action('fwleft')

    def turn_right(self):
        self.__action('fwright')

    def __calibrate(self, cmd):
        """
        In running mode post actions to car server for calibration.
        :param cmd: The calibration action to be performed by the car
            Options:
                # ============== Back wheels =============
                'bwcali' | 'bwcalileft' | 'bwcaliright' | 'bwcaliok'

                # ============== Front wheels =============
                'fwcali' | 'fwcalileft' | 'fwcaliright' |  'fwcaliok'

                # ================ Camera =================
                'camcali' | 'camcaliup' | 'camcalidown' | 'camcalileft' | 'camright' | 'camcaliok' 
        """
        url = BASE_URL + 'cali?action=' + cmd
        self.__req__(url)

    def __action(self, cmd):
        """
        In running mode post actions to car server for movement.
        :param cmd: The action to be performed by the car.
            Options:
                # ============== Back wheels =============
                'bwready' | 'forward' | 'backward' | 'stop'

                # ============== Front wheels =============
                'fwready' | 'fwleft' | 'fwright' |  'fwstraight'

                # ================ Camera =================
                'camready' | 'camleft' | 'camright' | 'camup' | 'camdown'
        """
        url = BASE_URL + 'run?action=' + cmd
        self.__req__(url) 

    # initially for training only give an option to brake or move at constant speed (0 or 1)
    def __change_speed(self, speed):
        """
        :param speed: The speed to be set
        :type speed: int, float
        :where: speed is in range (0, 100)
        """
        url = BASE_URL + 'run?speed=' + speed
        if speed > 100 or speed < 0:
            raise ValueError('Speed should be in the range 0 ~ 100')
        self.__req__(url)    

    def __connection_ok__(self):
        """
        Check whether connection is working,
        server will respond with 'ok'
        :return: 
            True if connection ok,
            False if no connection
        :rtype: bool
        """
        url = BASE_URL + 'connection_test'
        try:
            r=requests.get(url)
            if r.text == 'OK':
                logging.info('Connection OK')
                return True
        except Exception as e:
            
            return False

    def __login__():
        if self.__connection_ok__():
            logging.info('Login successful')
        else:
            raise ConnectionError('Unable to contact the car server')

    def __req__(self, url):
        """
        Internal method to send a request to the server
        :param url: the url to send the request to
        """
        try:
            logging.info('Calling - {}'.format(url))
            requests.get(url)
            return 0
        except Exception as e:
            
