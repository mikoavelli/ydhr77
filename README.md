To make the process a daemon, put ```arp_logger.service``` in ```/etc/systemd/system/arp_logger.service``` 
and ```arp_logger.sh``` in ```/usr/local/bin/arp_logger.sh```, then ```sudo systemctl enable arp_logger.service``` and 
```sudo systemctl start arp_logger.service```. 
Also make the script executable with ```sudo chmod +x /usr/local/bin/arp_logger.sh```.

```arp_logger.py``` is an alternative to ```arp_logger.sh```. No difference, just in python
