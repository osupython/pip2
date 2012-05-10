"""
Command line argument parser
"""

import argparse

import pip2.cli_wrapper


def create_parser():
    parser = argparse.ArgumentParser(prog='pip2')
    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('install', help='- Install a package or list of packages')
    parser_install.add_argument('package_list', nargs='+', help='- Package or list of packages to install')
    parser_install.set_defaults(func=pip2.cli_wrapper.install)

    parser_uninstall = subparsers.add_parser('uninstall', help='- Uninstall a package or list of packages')
    parser_uninstall.add_argument('package_list', nargs='+', help='- Package or list of packages to uninstall')
    parser_uninstall.set_defaults(func=pip2.cli_wrapper.uninstall)

    parser_freeze = subparsers.add_parser('freeze', help='- Display locally installed packages')
    parser_freeze.set_defaults(func=pip2.cli_wrapper.freeze)

    parser_search = subparsers.add_parser('search', help='- Search for a package on PyPi')
    parser_search.add_argument('package')
    parser_search.set_defaults(func=pip2.cli_wrapper.search)

    return parser
