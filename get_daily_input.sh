#!/bin/bash

day=$( TZ=America/New_York date +%d )
# Strip the leading zero
day=$((10#$day))

# Read session cookie from config file
cookie=`cat cookie.conf`

mkdir Day${day}
curl "https://adventofcode.com/2022/day/$day/input" --cookie "session=$cookie" > Day${day}/day${day}_input.txt
