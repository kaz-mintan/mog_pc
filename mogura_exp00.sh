#!/bin/bash
DIR="/home/kazumi/mogura/new_exp/"
if [ ! -e $DIR ];then
  mkdir $DIR
  chmod a+xwr $DIR
fi


DIR2="/home/kazumi/mogura/pic/"
if [ ! -e $DIR2 ];then
  mkdir $DIR2
  chmod a+xwr $DIR2
fi

echo "カメラ確認。顔の位置を確認してください。Ctrl-Cで終了。"
python3 camera_test.py
