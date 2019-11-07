#!/bin/bash

MOGUDIR=/home/kazumi/mogura
if [ $# -ne 1 ]; then
  echo "指定された引数は$#個です。" 1>&2
  echo "実行するには1個の引数(user name)が必要です。" 1>&2
  exit 1
fi

DIR=/home/kazumi/mogura/$1
mkdir $DIR
chmod a+xwr $DIR

mv $MOGUDIR/sample.wav $DIR
mv $MOGUDIR/pic $DIR
mv $MOGUDIR/heart_out.csv $DIR
mv $MOGUDIR/new_exp $DIR

