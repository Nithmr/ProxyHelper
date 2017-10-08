
import os; 

rmfile1 = "/etc/network/if-up.d/torpinger"
rmfile2 = "/etc/network/if-up.d/zetproxy"
rmfile3 = "/usr/bin/phelp"
if os.getuid()!=0:
    print ('This script should be run with root permission');
else:
    if os.path.isfile(rmfile1):
        os.remove(rmfile1);

    if os.path.isfile(rmfile2):
        os.remove(rmfile2);

    if os.path.isfile(rmfile3):
        os.remove(rmfile3);
    print("Uninstallation complete")
