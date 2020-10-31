
#! /bin/bash

#TO INSTAL x-term emulator run
#sudo apt-get update -y
#sudo apt-get install -y x-terminal-emulator

#edit -x -y -z for location of target in sim -Y for yaw/rotation
x-terminal-emulator -e rosrun gazebo_ros spawn_model -file ~/catkin_ws/src/arm_description/models/qr_code_target/model.sdf -sdf -model target -x 0.2 -z 0.5105






