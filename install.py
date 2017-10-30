#!/usr/bin/env python3

import os, sys
from stat import *

# exit if root
if os.geteuid() == 0:
  sys.exit("\nOnly root can run this script\n")


home = os.environ['HOME']
executable_files = ["zetproxy", "proxyhelper.py", "torpinger", "uninstall.sh"]
old_files = [ "/usr/bin/phelp",
              "/usr/bin/zetproxy",
              "/usr/bin/torpinger",
              "/etc/network/if-up.d/zetproxy",
              "/etc/network/if-up.d/torpinger"
            ]

if not os.path.basename(os.getcwd()) == '.proxyhelper':
  print("Exiting. This script should be run from \"~/.proxyhelper\" directory")
  sys.exit()


for file in executable_files:
  file_path = "{}/.proxyhelper/{}".format(home,file)
  os.chmod(file_path, os.stat(file_path).st_mode | 0o111)


for file in old_files:
  try:
    os.remove(file)
  except:
    os.system("sudo rm {}".format(file))


# symlinks fail if the path is not absolute
os.symlink("{}/.proxyhelper/{}".format(home, "zetproxy"), "/etc/network/if-up.d/zetproxy")
os.symlink("{}/.proxyhelper/{}".format(home, "torpinger"), "/etc/network/if-up.d/torpinger")
os.symlink("{}/.proxyhelper/{}".format(home, "proxyhelper.py"), "/usr/bin/phelp")

print("Installation complete")