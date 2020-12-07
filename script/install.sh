#! /bin/sh

set -e

cd "$(dirname "$0")/.."

echo "=> Installing pihole-toggle...\n"
sudo cp pihole-toggle.py /usr/local/bin/
sudo chmod +x /usr/local/bin/pihole-toggle.py
sudo cp pihole-toggle.sh /etc/init.d/
sudo chmod +x /etc/init.d/pihole-toggle.sh

echo "=> Starting pihole-toggle...\n"
sudo update-rc.d pihole-toggle.sh defaults
sudo /etc/init.d/pihole-toggle.sh start

echo "pihole-toggle installed.\n"
