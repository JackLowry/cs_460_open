import rospy
import matplotlib.pyplot as plt
from nav_tester.msg import Challenge
from math import atan2

MAP_FILE = "/home/jack/comp_robotics_open/catkin_ws/nav_tester/mymap.pgm"

def talker():
    with open(MAP_FILE, 'rb') as pgmf:
        map = plt.imread(pgmf)
        plt.imshow(map)
        plt.title("Please select the starting position, and the orientation of the start pose.")
        start_pts = plt.ginput(n=2)
        print(start_pts)
        plt.quiver(start_pts[0][0], start_pts[0][1], start_pts[1][0] - start_pts[0][0], -(start_pts[1][1] - start_pts[0][1]), color='r')
        plt.title("Please select the goal position, and the orientation of the goal pose.")
        goal_pts = plt.ginput(n=2)
        plt.quiver(goal_pts[0][0], goal_pts[0][1], goal_pts[1][0] - goal_pts[0][0], -(goal_pts[1][1] - goal_pts[0][1]), color='g')
        plt.title("Confirm the positions, and exit out of the window when ready.")
        plt.show()

        pub = rospy.Publisher('chatter', Challenge, queue_size=10)
        rospy.init_node('director', anonymous=True)
        msg =  Challenge()
        msg.start = (start_pts[0][0], start_pts[0][1], atan2(start_pts[1][1] - start_pts[0][1], -(start_pts[1][1] - start_pts[0][1])))
        msg.goal = (goal_pts[0][0], goal_pts[0][1], atan2(goal_pts[1][1] - goal_pts[0][1], -(goal_pts[1][1] - goal_pts[0][1])))
        pub.publish(msg)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass