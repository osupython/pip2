import argparse
import cli_wrapper

def create_parser():
    parser = argparse.ArgumentParser(prog='pip2')
    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('install')
    parser_install.add_argument('package_list', nargs='+')
    parser_install.set_defaults(func=cli_wrapper.install)
    
    return parser
