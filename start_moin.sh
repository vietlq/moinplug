#!/usr/bin/env bash

export THE_HOST=localhost
export THE_PORT=9090

moin server standalone --hostname $THE_HOST --port $THE_PORT --start --config-dir=`pwd` --wiki-url=http://${THE_HOST}:${THE_PORT}/ --pidfile=`pwd`/temp/moin.pid &

