#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from std_msgs.msg import Int16
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
#gripper_group = moveit_commander.MoveGroupCommander("gripper")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
#positions = [[0,0,1.57,0,0,0]]#[[0,-1.1,1.9,0,-1.4,0]] //0.35 box

# We can get the name of the reference frame for this robot:
planning_frame = move_group.get_planning_frame()
print "============ Planning frame: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = move_group.get_end_effector_link()
print "============ End effector link: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Available Planning Groups:", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "============ Printing robot state"
print robot.get_current_state()
print ""

print "=========== Printing current pose"
print move_group.get_current_pose().pose
print ""

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x = -0.403404226084
pose_goal.orientation.y = 0.738467510497
pose_goal.orientation.z = 0.259025496666
pose_goal.orientation.w = 0.474169335148
pose_goal.position.x = 0.136853931231
pose_goal.position.y = 0.213115454564
pose_goal.position.z = 0.223646255796

move_group.set_pose_target(pose_goal)

plan = move_group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
move_group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
move_group.clear_pose_targets()

#positions = [[1.5,0.5,0.0,0.0],[-1.5,0.5,0.0,0.0]]
#for pos in positions:
#	group_variable_values = group.get_current_joint_values()
#	print group_variable_values
#	group_variable_values[0] = pos[0]
#	group_variable_values[1] = pos[1]
#	group_variable_values[2] = pos[2]
#	group_variable_values[3] = pos[3]
#
#	group.set_joint_value_target(group_variable_values)
#	group.set_planning_time(10);
#	plan = group.plan()
	# Display trajectory in RViz
#	display_trajectory = moveit_msgs.msg.DisplayTrajectory()
#	display_trajectory.trajectory_start = robot.get_current_state()
#	display_trajectory.trajectory.append(plan)
	# Publish
#	display_trajectory_publisher.publish(display_trajectory);
#	group.execute(plan, wait=True)
#	rospy.sleep(2)
