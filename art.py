import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def art():
    cprint(figlet_format('InstaDMer 1.0', font='big'),
           'blue', attrs=[] )
           
    cprint(figlet_format('by m1r3x', font='big'),
           'red', attrs=[])
       
       

