import logging
from stat import filemode

from second import Second
# import second

class One():

    def __init__(self):
        pass

    def generate_log(self):
        # generate example log
        logging.debug('debug1')
        logging.info('info1')
        logging.warning('warning1')
        logging.error('erro1')

logging.basicConfig(
            filename = './log/main.log',
            filemode = 'w',
            level = logging.DEBUG,
            format = '%(asctime)s.%(msecs)03d %(levelname)8s %(module)s - %(funcName)s: %(message)s',
            datefmt = '%Y-%m-%d %H:%M:%S',
        ) 

obj = One()
obj.generate_log()
obj = Second()
obj.generate_log()
obj.finaliza()

print("end_main")