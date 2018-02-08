#!/bin/bash

set -ex

./manage.py test --noinput --nologcapture -a '!search_tests' --with-nicedots
