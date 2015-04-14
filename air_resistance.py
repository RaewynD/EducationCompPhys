# air_resistance.py

# original code by Byron Philhour
# modified by Raewyn Duvall & John C. Merfeld

# TODO

# primary:
# build boilerplate code appropriately
# update drag coefficient to accurately take area into account
# 
# secondary:
# ensure that air resistance is discussed, the key concept being that it is
#   dependent on velocity
# this code is probably the most intuitive way to understand it, really. We 
#   need to facilitate that
# starting by thowing them up might be more useful than bouncing, as it
#   reveals other interesting features of the problem
# side-by-side comparison of b = 0 and b > 0 cases

from __future__ import division # import decimal division
from visual import *            # import standard visual python
from visual.graph import *      # import graphing features

# make the floor
ground = box(pos = (0,0,0), size = (15,0.1,15), color = color.green)

# make and set up our bouncing ball
ball = sphere(pos = (1,1,1), readius = 10, color = color.yellow)
ball.velocity = vector(3,20,0) # starting velocity in m/s
ball.accel = vector(0,0,0)    # starig acceleration in m/s^2
ball.mass = 2.0               # staring mass in kg
gravity = 9.8                 # acceleration du to gravity in m/s^2
coeff_rest = .9               # % velocity remains after collision

b = 1 # drag coefficient

deltat = 0.05 # time step
t = 0         # starting time
t_end = 100    # end time

# set up graph
graph = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "y-velocity vs. time")
velocitycurve = gcurve(display = graph.display, color = color.cyan)

# loop action
while t < t_end:
    # control flow of time -- rate sets loops/sec
    rate(10) # note if this number times deltat is one, we're in "real time"
    t = t + deltat # update time coordinate for plot

    # figure out the net force acting on the ball
    ball.F_gravity = vector(0, -ball.mass*gravity,0) # gravitational force
    ball.F_drag = -b * ball.velocity                 # drag force = -bv
    ball.F_net = ball.F_gravity + ball.F_drag        # sum of forces

    # Newton's 2nd Law
    ball.accel = ball.F_net / ball.mass

    #update kinematics
    ball.velocity = ball.velocity + ball.accel*deltat # delta-v = a * delta-t
    ball.pos = ball.pos + ball.velocity*deltat        # delta-x = a * delta-a

    #check for collision with the ground
    if ball.pos.y - ball.radius < ground.pos.y:
        ball.velocity.y = -1 * coeff_rest * ball.velocity.y
        ball.pos.y = ball.radius #avoid getting trapped

    # plot a single point on our graph -- the y-velocity of the ball vs. time
    velocitycurve.plot(pos=(t, ball.velocity.y))

