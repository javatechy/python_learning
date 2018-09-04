import subprocess

import sys
import os

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ('First Argument List:', sys.argv[1])

def commands(str):
    subprocess.call(str)
    


def command2(str):
    subprocess.run(str, shell=True)




def commandOs(str):
    os.system(str)
    
commands(['df', '-h']);
command2('df -h');