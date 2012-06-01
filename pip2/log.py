"""
Sets up the pip2 logger for use
"""

import logging

from pip2.compat import packaging
from pip2.locations import default_log_file

logger = logging.getLogger('pip2')

def setup_logger():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    hndlr = logging.FileHandler(default_log_file, mode='w')
    hndlr.setFormatter(fmt='%(asctime)s: %(name)s: %(level)s: %(message)s')

    logger.addHandler(hndlr)
    # since packaging/distutils2 is very heavily intertwined with pip2 its a
    # good idea to capture the packaging logger's messages in the same file as
    # pip2's
    packaging.logger.addHandler(hndlr)

