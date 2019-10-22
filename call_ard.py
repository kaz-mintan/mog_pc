import subprocess

#note `g++ -o heart heart_fsr.cpp
#please check /dev/ttyACM0

def get_hearts():
    cmd = "sudo ./heart"
    subprocess.call(cmd.split())
