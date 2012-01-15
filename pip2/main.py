"""
TODO: DOCSTRING
"""

import pip_parser

parser = pip_parser.create_parser()

args = parser.parse_args()
args.func(args)
