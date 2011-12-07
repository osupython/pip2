from . import _install, _uninstall, _search, _freeze

def install(args):
    _install.run(args)

def uninstall(args):
    _uninstall.run(args)

def search(args):
    _search.run(args)

def freeze(args):
    _freeze.run(args)
