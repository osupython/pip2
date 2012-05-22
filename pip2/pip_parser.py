"""
Command line argument parser
"""

import argparse

import pip2.cli_wrapper


def create_parser():
    parser = argparse.ArgumentParser(prog='pip2', description="Manage python projects")
    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('install', help='- Install a project or list of projects')
    parser_install.add_argument('project_list', nargs='+', help='- project or list of projects to install')
    parser_install.set_defaults(func=pip2.cli_wrapper.install)

    parser_uninstall = subparsers.add_parser('uninstall', help='- Uninstall a project or list of projects')
    parser_uninstall.add_argument('project_list', nargs='+', help='- project or list of projects to uninstall')
    parser_uninstall.set_defaults(func=pip2.cli_wrapper.uninstall)

    parser_freeze = subparsers.add_parser('freeze', help='- Display locally installed projects')
    parser_freeze.set_defaults(func=pip2.cli_wrapper.freeze)

    parser_search = subparsers.add_parser('search', help='- Search for a project on PyPI')
    parser_search.add_argument('project')
    parser_search.set_defaults(func=pip2.cli_wrapper.search)

    return parser
