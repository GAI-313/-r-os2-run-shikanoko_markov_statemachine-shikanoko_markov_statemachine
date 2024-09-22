#!/usr/bin/env python3
from rclpy.node import Node
import rclpy

from sensor_msgs.msg import Image

from ament_index_python.packages import get_package_share_directory

import smach
import smach_ros

import traceback
import random
import time
import os
import cv2


VIDEO_PREFIX = os.path.join(
    get_package_share_directory('shikanoko_markov_statemachine'), 'video'
)

def video_publisher(node, file_name):
    global pub

    video = os.path.join(VIDEO_PREFIX, '%s.mov'%file_name)
    cap = cv2.VideoCapture(video)

    while rclpy.ok():
        ret, frame = cap.read()
        if ret:
            cv2.putText(frame, file_name, (10,200), 1, 5, (255,0,0), 5)
            cv2.imshow('view', frame)
            cv2.waitKey(30)
        else:
            break

@smach.cb_interface(outcomes=['success', 'failure'])
def ShikanokoDays(userdata, node):
    try:
        node.get_logger().info('Start shikanoko_markov_statemachine')
        node.get_logger().info('NUN : ぬん')
        video_publisher(node, 'nun')
        return 'success'
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['ka', 'ta', 'failure'])
def Shi(userdata, node):
    try:
        node.get_logger().info('SHI : し')
        video_publisher(node, 'shi')
        return random.choice(['ka', 'ta'])
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['no', 'failure'])
def Ka(userdata, node):
    try:
        node.get_logger().info('KA : か')
        video_publisher(node, 'ka')
        return 'no'
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['ko', 'failure'])
def No(userdata, node):
    try:
        node.get_logger().info('NO : の')
        video_publisher(node, 'no')
        return 'ko'
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['no', 'ko', 'shi', 'failure'])
def Ko(userdata, node):
    try:
        node.get_logger().info('NO : こ')
        video_publisher(node, 'ko')
        return random.choice(['no', 'no', 'ko', 'shi'])
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['nn', 'failure'])
def Ta(userdata, node):
    try:
        node.get_logger().info('TA : た')
        video_publisher(node, 'ta')
        return 'nn'
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['empty', 'ta', 'failure'])
def Nn(userdata, node):
    try:
        node.get_logger().info('SHI : ん')
        video_publisher(node, 'nn')
        return random.choice(['empty', 'ta'])
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

@smach.cb_interface(outcomes=['empty', 'shi', 'failure'])
def Empty(userdata, node):
    try:
        node.get_logger().info(' : ')
        video_publisher(node, 'empty')
        return random.choice(['empty', 'shi'])
    except:
        node.get_logger().error(traceback.format_exc())
        return 'failure'

def main():
    #global pub
    
    rclpy.init()
    node = Node('shikanoko_markov_statemachine')
    pub = node.create_publisher(Image, 'sms_image', 10)

    sm = smach.StateMachine(outcomes=['success', 'failure'])

    with sm:
        smach.StateMachine.add('NUN', smach.CBState(ShikanokoDays, cb_kwargs={'node':node}),
                    transitions={'success':'SHI',
                                 'failure':'failure'})

        smach.StateMachine.add('SHI', smach.CBState(Shi, cb_kwargs={'node':node}),
                    transitions={'ka':'KA',
                                 'ta':'TA',
                                 'failure':'failure'})

        smach.StateMachine.add('KA', smach.CBState(Ka, cb_kwargs={'node':node}),
                    transitions={'no':'NO',
                                 'failure':'failure'})

        smach.StateMachine.add('NO', smach.CBState(No, cb_kwargs={'node':node}),
                    transitions={'ko':'KO',
                                 'failure':'failure'})

        smach.StateMachine.add('KO', smach.CBState(Ko, cb_kwargs={'node':node}),
                    transitions={'ko':'KO',
                                 'no':'NO',
                                 'shi':'SHI',
                                 'failure':'failure'})

        smach.StateMachine.add('TA', smach.CBState(Ta, cb_kwargs={'node':node}),
                    transitions={'nn':'NN',
                                 'failure':'failure'})

        smach.StateMachine.add('NN', smach.CBState(Nn, cb_kwargs={'node':node}),
                    transitions={'empty':'EMPTY',
                                 'ta':'TA',
                                 'failure':'failure'})

        smach.StateMachine.add('EMPTY', smach.CBState(Empty, cb_kwargs={'node':node}),
                    transitions={'empty':'EMPTY',
                                 'shi':'SHI',
                                 'failure':'failure'})

    sis = smach_ros.IntrospectionServer('smach_server', sm, '/SHIKANOKO_DAYS')
    sis.start()
    outcome = sm.execute()
    if outcome == 'success':
        node.get_logger().info('success')
    else:
        node.get_logger().error('except finish')
    node.destroy_node()
