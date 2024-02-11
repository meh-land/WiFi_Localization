#!/bin/bash

# rescan wifi networks
sudo nmcli device wifi rescan

# list all available networks and get the desired columns
nmcli -f SSID,SIGNAL device wifi list | grep -E "YahiaWalid|Sam_s*" | sort > signals.temp

# format delimiters for python script
sed -i -E 's/([a-zA-Z0-9])\s+/\1,/g' signals.temp
sed -i -E 's/,$//g' signals.temp
