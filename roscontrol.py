'''
编写一个ROS的python节点，能够将用户在终端的按键信息转换成速度指令，控制机器人的运动。
'''
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control Your TurtleBot3!
---------------------------
Moving around:
        w
   a    s    d
        x
w/x : increase/decrease linear velocity (Burger : ~ 0.22, Waffle and Waffle Pi : ~ 0.26)
a/d : increase/decrease angular velocity (Burger : ~ 2.84, Waffle and Waffle Pi : ~ 1.82)
space key, s : force stop
CTRL-C to quit
"""

moveBindings = {
        'w':(0.1,0),
        'x':(-0.1,0),
        'a':(0,0.1),
        'd':(0,-0.1),
}

speedBindings = {
        'q':(0.1,0.1),
        'e':(0.1,-0.1),
}

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    
    speed = 0.1
    turn = 0.1
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0
    
    try:
        print(msg)
        print(vels(speed,turn))
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                z = moveBindings[key][1]
            elif key in speedBindings.keys():
                speed = speed + speedBindings[key][0]
                turn = turn + speedBindings[key][1]
                
                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            elif key == ' ' or key == 's':
                x = 0
                z = 0
            else:
                if (key == '\x03'):
                    break
                
            twist = Twist()
            twist.linear.x = x*speed
            twist.linear.y = y*speed
            twist.linear.z = z*speed
            
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = th*turn
            
            pub.publish(twist)
            
    except Exception as e:
        print(e)
    
    finally:
        twist = Twist()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        
        pub.publish(twist)
        
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)