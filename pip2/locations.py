"""
These locations will be determined by the pip2 config file, but since it currently
does not exist values will temporarily be hard-coded in.
"""

import os
import sys

# path to user's directory where pip2 log, config, and other data are stored
usr_dir = os.path.expanduser('~')
# pip2 directory where pip2 specific data will be stored
default_storage_dir = None
# path and name of pip2 log file
default_log_file = None

if sys.platform == 'win32':
        usr_dir = os.environ.get('APPDATA', usr_dir)
        default_storage_dir = os.path.join(usr_dir, 'pip2')
else:
        default_storage_dir = os.path.join(usr_dir, '.pip2')
if not os.path.exists(default_storage_dir):
        os.mkdir(default_storage_dir)

default_log_file = os.path.join(default_storage_dir, 'pip2.log')