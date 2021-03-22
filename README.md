# Linux-Scripts

## powerswap.py
Used to swap governer to different states  
### How to use:
Needs sudo to change governer  
power-targets: performance, powersave, ondemand  
sudo ./powerswap.py power-target  
  
sudo ./powerswap.py powertarget max-logical-core  
Eg. sudo ./powerswap.py performance 8


## ipa.py
Prettier version of the ip a command Should be better to look

### How to use:
./ipa.py  

## make_wpa_supplicant
script to automatically make wpa_supplicant.conf file 

### How to use:
./make_wpa_supplicant
