"""
Adds an extra handler to the pip2 logger so that tests can be easily ran
"""

import logging
from io import StringIO

import pip2.log


def setup_logger():
        pip2.log.setup_logger()

        test_fmtr = logging.Formatter(fmt='%(message)s')
        test_hndlr = logging.StreamHandler(stream=StringIO())
        test_hndlr.setLevel(logging.INFO)
        test_hndlr.setFormatter(test_fmtr)
        pip2.log.logger.addHandler(test_hndlr)

        return test_hndlr.stream
