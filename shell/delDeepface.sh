# !/bin/bash
operator_file_path="../facePictures/"
while :
do
  sudo find $operator_file_path -name "*.pkl" |xargs rm -rf
  sleep 8
done
