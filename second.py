import logging

class Second():

    @staticmethod
    def generate_log():
        # generate example log
        logging.debug('debug2')
        logging.info('info2')
        logging.warning('warning2')
        logging.error('erro2')

    @staticmethod
    def finaliza():
        logging.info('EndSecond')