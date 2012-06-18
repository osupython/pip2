"""
Entry point for pip2
"""

# If you change the version here, be sure to also change it in setup.py and
# docs/conf.py
__version__ = '0.0.1.dev1'

import pip2.pip_parser
import pip2.log


def main():
    pip2.log.setup_logger()

    parser = pip2.pip_parser.create_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()

if __name__ == '__main__':
    main()
