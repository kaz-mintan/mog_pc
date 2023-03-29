import subprocess

#note `g++ -o heart heart_fsr.cpp
#please check /dev/ttyACM0

def get_hearts():
    cmd = "sudo ./heart_fsr /dev/ttyACM0"
    print(cmd)
    subprocess.call(cmd.split())

if __name__ == '__main__':
    get_hearts()
