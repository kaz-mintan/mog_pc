#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python capture.py <idxCam1> <idxCam2> <ndisparities> <SADWindowSize>
import sys
import numpy as np
import cv2

import matplotlib.pyplot as plt
from drawnow import drawnow, figure
import datetime

width = 320
height = 240
limit = 180


def capture():

  cap_1 = cv2.VideoCapture(0)
  cap_2 = cv2.VideoCapture(1)
  cap_3 = cv2.VideoCapture(2)

  first_time = datetime.datetime.now()

  time = 0
  count_time = 0
  fig = figure()
  def draw():
    plt.plot(range(100),ave_gaze[1,:])

  while True:
    frame_got_1, frame_1 = cap_1.read()
    frame_got_2, frame_2 = cap_2.read()
    frame_got_3, frame_3 = cap_3.read()
    delta = datetime.datetime.now() - first_time
    if delta.total_seconds()>int(limit):
      break
    else:
      if frame_got_1 is False:
        break
      else:
        f_1 = cv2.flip(frame_1, 2)
        f_2 = cv2.flip(frame_2, 2)
        f_3 = cv2.flip(frame_3, 2)

        g_1 = cv2.cvtColor(f_1, cv2.COLOR_BGR2GRAY)
        g_2 = cv2.cvtColor(f_2, cv2.COLOR_BGR2GRAY)
        g_3 = cv2.cvtColor(f_3, cv2.COLOR_BGR2GRAY)

        r_1 = cv2.resize(g_1,(width,height))
        r_2 = cv2.resize(g_2,(width,height))
        r_3 = cv2.resize(g_3,(width,height))

        a_1 = np.array(r_1,dtype=np.uint8)
        a_2 = np.array(r_2,dtype=np.uint8)
        a_3 = np.array(r_3,dtype=np.uint8)

        frame = np.hstack((g_1,g_2,g_3))
        count_time = count_time + 1
        name = "/home/kazumi/mogura/pic/"+str(datetime.datetime.now()) + "-cap.png"
        print name
        cv2.imwrite(name,frame)
        #print datetime.datetime.today()
        cv2.imshow("pic",frame)
        if cv2.waitKey(1) == 27:
          break

if __name__ == '__main__':
    capture()
