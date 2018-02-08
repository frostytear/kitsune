#!/bin/bash

./manage.py migrate --noinput
./manage.py test --noinput --nologcapture -a '!search_tests' --with-nicedots
