import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from jonty2 import menu

    menu()

elif bit == '32bit':

    from jonty3 import menu

    menu()