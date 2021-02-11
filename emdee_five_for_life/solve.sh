#!/bin/bash

req() {
	echo "Sending data: 'hash=$1'"
	curl -X POST --data "hash=$1" http://209.97.184.58:30039/ 
}



while :
do

	OUT=$(curl -s http://209.97.184.58:30039/ | grep "h3" | cut -d ">" -f4 | cut -d "<" -f1)
	echo $OUT
	HASH=$(./md5.py $OUT)
	echo $HASH
	req $HASH
done
