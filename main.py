import numpy as np
import os

#DIR="/media/kazumi/4b35d6ed-76bb-41f1-9d5d-197a4ff1a6ab/backup/home/kazumi/mogura/"
DIR="/home/kazumi/prog/mogura/"

class MoguLearn:
    def __init__(self,name):
        self.name=name
        self.sensor_filename = DIR+self.name+"/sensor_data.csv"
        self.motion_rule_filename = DIR+self.name+"/motion_rule.csv"
        self.sudata_filename = DIR+self.name+"/sudata.csv"

    def read_sensor(self):
        reading_data=np.loadtxt(self.sensor_filename,delimiter=",")
        os.remove(self.sensor_filename)
        return reading_data

    def get_emotion(self,sensor_data):
        emotion=np.zeros(5)
        return emotion

    def learn_new_sudata(self,sensor_data,emotion_data):
        new_sudata=np.hstack((sensor_data,emotion_data))
        print("you may have to convert sensor data to other format")
        np.savetxt(new_sudata,self.sudata_filename,delimiter=",")

    def update_motion_rule(self):
        rule=np.zeros(3)
        np.savetxt(rule,self.motion_rule_filename,delimiter=",")
        
def main(name):
    mog=MoguLearn(name)
    while(True):
        if(os.path.exists(mog.sensor_filename)):
            print("exist!")
            sensor_data=mog.read_sensor()
            emotion_data=mog.get_emotion(sensor_data)
            mog.learn_new_sudata(sensor_data,emotion_data)
            mog.update_motion_rule()

if __name__ == "__main__":
    name = "test"
    main(name)


