import requests
import logging

FORMAT = '%(asctime)s [%(levelname)s] %(name)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

class Controller:
    HOST = 'http://raspberrypi.local'
    PORT = '8000'
    BASE_URL = HOST + PORT

    def __init__(self):
        logging.info('Control initiated!')
        
    def calibrate(self, cmd):
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
        __req__(url)

    def action(self, cmd):
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
        __req__(url) 

    def change_speed(self, speed):
        """
        :param speed: The speed to be set
        :type speed: int, float
        :where: speed is in range (0, 100)
        """
        url = BASE_URL + 'run?speed=' + speed
        if speed > 100 or speed < 0:
            raise ValueError('Speed should be in the range 0 ~ 100')
        __req__(url)    

    def check_connection(self):
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
            

