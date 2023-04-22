#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator  import BasicNavigator

# me learning getFeedback() and BasicNavigator()

def main(): 
    rclpy.init()
    nav = BasicNavigator()

    # --- Wait for Nav2 
    nav.waitUntilNav2Active()


    print(nav)
    print( nav.getFeedback() , '\n')
    while not nav.isTaskComplete() or True: 
        print(nav, '\n')
        print(nav.getFeedback() , '\n----------------------------\n\n')
        

    rclpy.shutdown()

if __name__ == '__main__' : 
    main()