"""
Entry point for pip2
"""

__version__ = '0.0.1'

import pip2.pip_parser


def main():
    parser = pip2.pip_parser.create_parser()

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
