#!/bin/sh
echo UCCAAPP_ENV=$UCCAAPP_ENV
gunicorn --workers 3 --bind 0.0.0.0:8000 ucca.wsgi:application