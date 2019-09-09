#encoding: utf8
'''
Created on 2019/09/09

@author: HOLLY
'''

import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)
_basic_handler = logging.StreamHandler()
_basic_handler.setLevel(logging.DEBUG)
_formatter = logging.Formatter('%(asctime)s: %(name)s: '\
                               '%(levelname)s: %(message)s')
_basic_handler.setFormatter(_formatter)
_logger.addHandler(_basic_handler)


def calculate_set_probability():
    pass

if __name__ == '__main__':
    pass