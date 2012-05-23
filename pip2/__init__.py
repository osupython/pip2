"""
Entry point for pip2
"""

# If you change the version here, be sure to also change it in setup.py and
# docs/conf.py
__version__ = '0.0.1.dev1'

import logging

import pip2.pip_parser


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    parser = pip2.pip_parser.create_parser()

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
