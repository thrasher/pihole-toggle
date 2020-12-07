#! /bin/sh

set -e

cd "$(dirname "$0")/.."

echo "=> Stopping pihole-toggle...\n"
sudo update-rc.d pihole-toggle.sh remove
sudo /etc/init.d/pihole-toggle.sh stop

echo "=> Removing pihole-toggle...\n"
sudo rm -rf /usr/local/bin/pihole-toggle.py
sudo rm -rf /etc/init.d/pihole-toggle.sh

echo "pihole-toggle uninstalled.\n"
