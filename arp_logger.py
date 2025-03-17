import subprocess
import time
import logging
import os

LOG_FILE = "/var/log/arp_logger.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

INTERFACE = "eth0"
SLEEP_INTERVAL: int = 60


def get_arp_entries(interface: str):
    try:
        result = subprocess.run(["ip", "neigh", "show", "dev", interface], capture_output=True, text=True, check=True)
        output = result.stdout
        arp_entries = []

        for line in output.splitlines():
            parts = line.split()

            if len(parts) >= 4 and parts[1] == 'lladdr':
                ip_addr = parts[0]
                mac_addr = parts[3]
                arp_entries.append(f"IP: {ip_addr}, MAC: {mac_addr}")

        return arp_entries
    except subprocess.CalledProcessError as e:
        logging.error(e)
        return None


def main():
    if os.getuid() != 0:
        logging.error("You need to be root to run this script")
        print("You need to be root to run this script")
        return

    while True:
        arp_entries = get_arp_entries(INTERFACE)

        if arp_entries is not None:
            if arp_entries:
                logging.info(f"ARP logs for {INTERFACE}")
                for entry in arp_entries:
                    logging.info(entry)
            else:
                logging.info(f"No ARP logs for {INTERFACE}")
        else:
            pass

        time.sleep(SLEEP_INTERVAL)


if __name__ == '__main__':
    main()
