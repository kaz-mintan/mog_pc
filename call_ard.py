import subprocess

#note `g++ -o heart heart_fsr.cpp

def get_hearts():
    cmd = "sudo ./heart"
    subprocess.call(cmd.split())
