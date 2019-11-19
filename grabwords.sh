#!/bin/bash 

echo "Grabbing wordlists"

curl https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt --output wordlists/common.txt
curl https://raw.githubusercontent.com/arineng/arincli/master/lib/male-first-names.txt --output wordlists/male-names.txt
#curl https://raw.githubusercontent.com/arineng/arincli/master/lib/female-first-names.txt -- wordlists/female-first-names.txt

echo "Finishing up..."
