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

import numpy
from itertools import product, combinations
from collections import Counter


def generate_set_cards(randomize: bool = True) -> numpy.ndarray:
    cards_list = list(product([0,1,2], repeat=4))
    cards = numpy.array(cards_list)
    if randomize:
        numpy.random.shuffle(cards)
    return cards


def check_set(cards: numpy.ndarray, set_num: int = 3, return_first: bool = False):
    found_sets = []
    for c1, c2, c3 in combinations(range(len(cards)), set_num):
        sum_of_cards = numpy.sum(cards[[c1, c2, c3]], axis=0)
        if numpy.all(sum_of_cards % 3 == 0):
            found_sets.append(cards[[c1, c2, c3]])
            if return_first:
                return found_sets
    return found_sets


def calculate_set_probability(num_of_try: int = 100000):
    _logger.info('start calculation')
    result_counter = Counter()
    for trial in range(num_of_try):
        cards = generate_set_cards()
        for i in range(len(cards) - 2):
            found_sets = check_set(cards[:i+3], return_first=True)
            if len(found_sets) != 0:
                result_counter[i+1] += 1
                break
        if (trial+1) % 1000 == 0:
            _logger.info(f'done {trial+1}th trial')
    _logger.info(f'done {num_of_try} times calculation')
    probabilities = {}
    for played, count in result_counter.items():
        probabilities[played] = count / num_of_try
    print('probabilities...\nplayed\tprob')
    for played, prob in sorted(probabilities.items(), key=lambda x: x[0]):
        print(f'{played:>3g}\t{prob:>5.3f}')


if __name__ == '__main__':
    calculate_set_probability(100)