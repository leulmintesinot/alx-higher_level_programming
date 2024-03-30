#!/bin/bash
SIZE=$(curl -s "$1" | wc -c)
echo $SIZE
