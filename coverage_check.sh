#!/bin/sh

git pull
coverage run _tweetStats.py -dba
coverage run -a _tweetStats.py -dbl
coverage run -a _tweetStats.py -dbp
coverage run -a _tweetStats.py -dbs
coverage run -a _tweetStats.py -dbt
coverage run -a _tweetStats.py -dbv
coverage run -a _tweetStats.py
coverage xml
coverage report
export CODACY_PROJECT_TOKEN=
python-codacy-coverage -r coverage.xml -c $(git rev-parse HEAD)
