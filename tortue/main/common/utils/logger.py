# coding utf-8

import logging

LOGGER = logging.getLogger()

LOGGER.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

LOGGER.addHandler(stream_handler)

