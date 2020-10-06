#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import rospy
from std_msgs.msg import Int16
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm")
#gripper_group = moveit_commander.MoveGroupCommander("gripper")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
#positions = [[0,0,1.57,0,0,0]]#[[0,-1.1,1.9,0,-1.4,0]] //0.35 box

#ADD Objects to the Planning Scene For obstacle Avoidance
# Ground and a Box

box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "base_link"
box_pose.pose.orientation.w = 0.0
box_pose.pose.orientation.x = 0.0
box_pose.pose.orientation.y = 0.0
box_pose.pose.orientation.z = 0.0
box_pose.pose.position.x = 0.3
box_pose.pose.position.y = 0.0 
box_pose.pose.position.z = 0.0 
box_name = "box"
scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))

ground_pose = geometry_msgs.msg.PoseStamped()
ground_pose.header.frame_id = "base_link"
ground_pose.pose.orientation.w = 0.0
ground_pose.pose.orientation.x = 0.0
ground_pose.pose.orientation.y = 0.0
ground_pose.pose.orientation.z = 0.01
ground_pose.pose.position.x = -3
ground_pose.pose.position.y = 0.0 
ground_pose.pose.position.z = 0.0 
ground_name = "ground"
scene.add_box(box_name, box_pose, size=(6, 6, 0.1))


positions = [[1.5,0.5,0.0,0.0],[-1.5,0.5,0.0,0.0]]
for pos in positions:
	group_variable_values = group.get_current_joint_values()
	print group_variable_values
	group_variable_values[0] = pos[0]
	group_variable_values[1] = pos[1]
	group_variable_values[2] = pos[2]
	group_variable_values[3] = pos[3]

	group.set_joint_value_target(group_variable_values)
	group.set_planning_time(10);
	plan = group.plan()
	# Display trajectory in RViz
	display_trajectory = moveit_msgs.msg.DisplayTrajectory()
	display_trajectory.trajectory_start = robot.get_current_state()
	display_trajectory.trajectory.append(plan)
	# Publish
	display_trajectory_publisher.publish(display_trajectory);
	group.execute(plan, wait=True)
	rospy.sleep(2)
'''
gripper_group.set_named_target("gripper_close") 
plan_gripper = gripper_group.plan()
gripper_group.go(wait=True)
rospy.sleep(1)
'''
moveit_commander.roscpp_shutdown()
