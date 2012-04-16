"""
TODO: DOCSTRING
"""

import argparse
import pip2.cli_wrapper


def create_parser():
    parser = argparse.ArgumentParser(prog='pip2')
    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('install')
    parser_install.add_argument('package_list', nargs='+')
    parser_install.set_defaults(func=pip2.cli_wrapper.install)

    parser_install = subparsers.add_parser('uninstall')
    parser_install.add_argument('package_list', nargs='+')
    parser_install.set_defaults(func=pip2.cli_wrapper.uninstall)

    parser_freeze = subparsers.add_parser('freeze')
    parser_freeze.set_defaults(func=pip2.cli_wrapper.freeze)

    parser_search = subparsers.add_parser('search')
    parser_search.add_argument('package')
    parser_search.set_defaults(func=pip2.cli_wrapper.search)

    return parser
