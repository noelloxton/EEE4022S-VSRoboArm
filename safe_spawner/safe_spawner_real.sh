
#! /bin/bash

#TO INSTAL x-term emulator run
#sudo apt-get update -y
#sudo apt-get install -y x-terminal-emulator

x-terminal-emulator -e roslaunch arm_bringup real_bringup.launch 2>/dev/null &&

sleep 5 &&

x-terminal-emulator -e roslaunch arm_bringup moveit.launch 2>/dev/null &&

sleep 3 &&

x-terminal-emulator -e roslaunch arm_bringup serial.launch 2>/dev/null &&

sleep 3 &&

x-terminal-emulator -e roslaunch arm_bringup rviz.launch rviz_config:=rviz_real 2>/dev/null &







