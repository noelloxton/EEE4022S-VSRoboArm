PROJECT NAME: Visual Servoing of a Simulated Robot Arm

DESCRIPTION: This project involves implementing a visual sensor on a robot arm simulation in order for the arm to learn different poses using a Convolutional neural network (CNN) using tensorflow. All robot simulations were done using Gazebo and the Robot Operating System (ROS)

INSTALLATION:

ROS/GAZEBO

    NOTE: This program requires a linux machine running Ubuntu 18.04 'Bionic Beaver' - newer versions will not work since MOVEIT requires this older version of Ubuntu at the
    time of writing this...

    1) Install ROS Melodic - http://wiki.ros.org/melodic/Installation/Ubuntu
    2) Install MOVEIT for ROS melodic - http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/getting_started/getting_started.html
    3) Download and install the robot arm using the following set of instructions (These are taken from Matthew Markey's source code https://github.com/matthewmarkey44/eee4022f)

        1. Make a custom directory for your workspace
        "mkdir <your_workspace_name>"
        2. Enter your workspace 
        "cd <your_workspace_name>"
        3. Make a 'src' folder
        "mkdir src"
        4. Enter the src folder 
        "cd src"
        5. clone this github source code
        "github clone git@github.com:noelloxton/EEE4022S-VSRoboArm.git"
    
        6. To include depdencies:
        "rosdep install --from-paths src --ignore-src -r -y"

        6.a. You may want to run just to be sure:
        "sudo apt-get install ros-melodic-ros-control ros-melodic-ros-controllers"

        7. Build the catkin workspace and source the setup file (NOTE: You can add the source command to automatically run on the startup of your bash terminal otherwise make
        sure to always run this command on a new terminal)
        "catkin_make && source devel/setup.bash"

    TO LAUNCH SIMULATION

        1. To launch Gazebo + Controllers
        "roslaunch arm_bringup sim_bringup.launch world:=empty"
        2. To launch Moveit (No need for setting start location though)
        "roslaunch arm_bringup moveit.launch"
        3. To launch RViz with custom config
        "roslaunch arm_bringup rviz.launch rviz_config:=rviz_sim"

        Script files to launch all commands at once.
        1. Install prerequisites for xterm emulator
        "sudo apt-get update -y"
        "sudo apt-get install -y x-terminal-emulator"
    
        then
        "roscd safe_spawner"               (I made this into a package just to be able to use roscd)
        "ls -a"                            (make sure they appear green or else set the permissions e.g "chmod +x safe_spawner_sim.sh")
    
        Then you can enter
        "./safe_spawner_sim.sh"
    
        P.S make sure the python executables also have the permissions (e.g roscd arm_bringup/scripts && chmod +x ...)

    Now you can run the movement scripts
 
        1. Make arm move to predefined positions consecutively 
        "rosrun arm_bringup pos_exec.py"
        2. Move arm to start position [upright]
        "rosrun arm_bringup set_start_pos.py"
        3. Run 1 and 2
        "rosrun arm_bringup moveit_command.py"

    Consult MOVEIT Tutorials for more info/examples

TENSORFLOW

    1. Install Tensorflow - https://www.tensorflow.org/install {I used the pip install guide using the python3 virtual environment}, {The GPU compatability is not required...}
