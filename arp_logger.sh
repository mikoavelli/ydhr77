#!/bin/bash

INTERFACE="eth0"
LOG_FILE="/var/log/arp_logger.log"
INTERVAL=60

if [[ $EUID -ne 0 ]]; then
  echo "You need to be root to run this script." >&2
  exit 1
fi

get_arp_entries() {
  ip neigh show dev "$INTERFACE" | awk '/lladdr/ {print "IP: "$1", MAC: "$4}'
}

while true; do
  arp_entries=$(get_arp_entries)

  if [ -z "$arp_entries" ]; then
    echo "ARP cache for interface $INTERFACE is empty" | tee -a "$LOG_FILE"
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ARP-logs for interface $INTERFACE:" | tee -a "$LOG_FILE"
    echo "$arp_entries" | tee -a "$LOG_FILE"
  fi

  sleep "$INTERVAL"
done
