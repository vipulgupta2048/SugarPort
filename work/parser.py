# Configparser Demo

import configparser
cp = configparser.ConfigParser()

cp.read('activity.info')
print (cp.get('Activity','website'))
