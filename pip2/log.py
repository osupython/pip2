"""
Sets up the pip2 logger for use
"""

import logging

from pip2.compat import packaging
from pip2.locations import default_log_file

logger = logging.getLogger(__name__)

def setup_logger():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    fmtr = logging.Formatter(fmt='%(asctime)-6s: %(name)s - %(levelname)s: ' +
                             '%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    hndlr = logging.FileHandler(default_log_file, mode='w')
    hndlr.setFormatter(fmtr)

    logger.addHandler(hndlr)
    # since packaging/distutils2 is very heavily intertwined with pip2 its a
    # good idea to capture the packaging logger's messages in the same file as
    # pip2's
    packaging.logger.addHandler(hndlr)
