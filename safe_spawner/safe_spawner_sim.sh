
#! /bin/bash

#TO INSTAL x-term emulator run
#sudo apt-get update -y
#sudo apt-get install -y x-terminal-emulator

x-terminal-emulator -e roslaunch arm_bringup sim_bringup.launch world:=empty 2>/dev/null &&

sleep 7 &&

x-terminal-emulator -e roslaunch arm_bringup moveit.launch 2>/dev/null &&

sleep 4 &&

x-terminal-emulator -e roslaunch arm_bringup rviz_sim.launch 2>/dev/null &







