'''
Created on 16-Apr-2020

@author: apoorv
'''

import logging

LEVELS = {
            0: logging.DEBUG,
            1: logging.INFO,
            4: logging.WARNING,
            5: logging.ERROR,
            6: logging.CRITICAL,
          }


def get_logger(logger_name, log_level=4, log_format=None):
    '''
    
    :param logger_name:
    :param log_level:
    :param log_format:
    '''
    level = LEVELS.get(log_level, logging.INFO)
    if not log_format:
        log_format = '%(asctime)s %(levelname)s {} : %(message)s'.format(logger_name)
    logging.basicConfig(level=level, format=log_format)
    return logging.getLogger(logger_name)
