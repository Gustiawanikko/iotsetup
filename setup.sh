#change repo to local
sudo mv /etc/apt/sources.list /etc/apt/sources.list.old
cd /etc/apt/
sudo wget https://raw.githubusercontent.com/FosterG4/iotset/main/sources.list

sudo apt-get update
sleep 3
sudo apt install python3 idle3
sleep 3
sudo apt install python3-netifaces
sleep 3

#go to folder
cd /home/pi/IOT/iotset/
#change permission execute
sudo chmod +x x728.sh
#start script
sudo ./x728.sh
sleep 3
sudo ./etc/x728pwr.sh
