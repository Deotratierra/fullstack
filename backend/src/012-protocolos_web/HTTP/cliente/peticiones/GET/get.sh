#!/bin/bash

# sudo apt-get install curl

response=$(curl https://min-api.cryptocompare.com/stats)
echo $response

