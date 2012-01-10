"""
TODO: DOCSTRING
"""

import parser

command_parser = parser.create_parser()

args = command_parser.parse_args()
args.func(args)
