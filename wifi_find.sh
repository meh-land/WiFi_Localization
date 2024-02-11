#!/bin/bash

# rescan wifi networks
sudo nmcli device wifi rescan

# list all available networks and get the desired columns
nmcli -f SSID,SIGNAL device wifi list | grep -E "YahiaWalid|Sam_s*" > signals.temp#!/bin/bash

