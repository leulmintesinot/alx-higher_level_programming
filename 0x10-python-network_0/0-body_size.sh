#!/bin/bash
URL=$1
curl -s "$URL" | wc -c
