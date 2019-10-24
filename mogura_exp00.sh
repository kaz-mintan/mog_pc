#!/bin/bash
DIR="/home/kazumi/mogura/pic/"
if [ ! -e $DIR ];then
  mkdir $DIR
fi
echo "カメラ確認。顔の位置を確認してください。Ctrl-Cで終了。"
python camera_test.py
