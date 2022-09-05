#!/bin/sh
pip-compile requirements.in;
mv requirements.txt /tmp/build/requirements.txt