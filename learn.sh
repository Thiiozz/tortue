#!/usr/bin/env bash

set -e

pip3 install -r requirements.txt

if [ ! -f ./dataset.csv ]; then
  touch ./dataset.csv
  echo "subject;text" > ./dataset.csv
fi

if [ -f ./model.sav ]; then
  rm ./model.sav
fi

python3 wiki-scrapper.py 10
python3 learn.py
python3 predict.py
