#!/bin/sh
## pihole tweeter
NAMEOFAPP="tweetStats"
WHATITDOES="This script will install tweetStats and setup a cronjob that runs every day at 23:55"

 { if
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP? $WHATITDOES" 8 78)
then
echo "Declined $NAMEOFAPP"
else
pip3 install -U -r https://raw.githubusercontent.com/mwoolweaver/tweetStats/master/requirements.txt
wget https://raw.githubusercontent.com/mwoolweaver/tweetStats/master/tweetStats.py -O ~/tweetStats/tweetStats.py
wget https://raw.githubusercontent.com/mwoolweaver/tweetStats/master/config.ini.example -O ~/tweetStats/config.ini
CONSUMER_KEY=$(whiptail --inputbox "Consumer Key" 20 60 "" 3>&1 1>&2 2>&3)
CONSUMER_SECRET=$(whiptail --inputbox "Consumer Secret" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN=$(whiptail --inputbox "Access Token" 20 60 "" 3>&1 1>&2 2>&3)
ACCESS_TOKEN_SECRET=$(whiptail --inputbox "Access Token Secret" 20 60 "" 3>&1 1>&2 2>&3)
sed -ie "s/VALUE1/$CONSUMER_KEY/" ~/tweetStats/config.ini
sed -ie "s/VALUE2/$CONSUMER_SECRET/" ~/tweetStats/config.ini
sed -ie "s/VALUE3/$ACCESS_TOKEN/" ~/tweetStats/config.ini
sed -ie "s/VALUE4/$ACCESS_TOKEN_SECRET/" ~/tweetStats/config.ini
fi }
{ if
(whiptail --title "$NAMEOFAPP" --yes-button "Skip" --no-button "Proceed" --yesno "Do you want to setup $NAMEOFAPP as a cronjob?" 8 78)
then
rm ~/pihole_tweeter/config.inie
echo "did not install cronjob"
else
sudo wget http://raw.githubusercontent.com/mwoolweaver/tweetStats/master/tweetStats -O /etc/cron.d/tweetStats
rm ~/tweetStats/config.inie
fi }
