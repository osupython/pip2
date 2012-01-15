import argparse
import pip2.commands

def create_parser():
    parser = argparse.ArgumentParser(prog='pip2')
    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('install')
    parser_install.add_argument('package_name')
    parser_install.add_argument('-e', '--editable', action='store_true')
    parser_install.set_defaults(func=pip2.commands.install)

    parser_uninstall = subparsers.add_parser('uninstall')
    parser_uninstall.add_argument('package_name')
    parser_uninstall.set_defaults(func=pip2.commands.uninstall)

    parser_search = subparsers.add_parser('search')
    parser_search.add_argument('package_name')
    parser_search.set_defaults(func=pip2.commands.search)

    parser_freeze = subparsers.add_parser('freeze')
    parser_freeze.set_defaults(func=pip2.commands.freeze)

    return parser
