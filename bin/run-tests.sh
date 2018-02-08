#!/bin/bash

set -ex

echo "######## ALL ENV ##########"
env

echo "######## cat .env #########"
cat .env

./manage.py migrate --noinput
./manage.py test --noinput --nologcapture -a '!search_tests' --with-nicedots
