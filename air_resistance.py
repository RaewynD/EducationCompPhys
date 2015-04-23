# air_resistance.py

# original code by Byron Philhour
# modified by Raewyn Duvall & John C. Merfeld

# DONE:
#   drag coefficient now takes area into account
#   drag force now functionalized

# TODO

# primary:
# build boilerplate code appropriately
# add support for side-by-side comparison of b = 0 and b > 0 cases
 

# secondary:
# ensure that air resistance is discussed, the key concept being that it is
#   dependent on velocity
# this code is probably the most intuitive way to understand it, really. We 
#   need to facilitate that
# starting by thowing them up might be more useful than bouncing, as it
#   reveals other interesting features of the problem

from __future__ import division # import decimal division
from visual import *            # import standard visual python
from visual.graph import *      # import graphing features
from numpy import pi

# function definition:

# drag equation:
#   I think if we left it as something like:

#   def drag_equation():    # add parameters!
#       (maybe outline the algorithm here?)
#       return drag

#   That could be a good way to do it. Basically every calculation down there 
#       I think we could spread to up here. All the kinematics stuff, etc. We
#       could still call the functions with the right arguments in the main 
#       code so they know what to work with, but they'd have to figure out
#       what to do with those parameters

def drag_equation(b, p, v, r):
    
    A = pi*(r**2)
    drag = vector(0,0,0)            # these three could be done in one line
    drag.x = -0.5*b*p*A*((v.x)**2)  # but it would be huge and gross
    drag.y = -0.5*b*p*A*((v.y)**2)

    return drag

def update_kinematics(body):

    # Newton's 2nd Law
    body.accel = body.F_net / body.mass

    #update kinematics
    body.velocity = body.velocity + body.accel*deltat # delta-v = a * delta-t
    body.pos = body.pos + body.velocity*deltat        # delta-x = a * delta-a

    return body

# make the floor
ground = box(pos = (0,0,0), size = (15,0.1,100), color = color.green)

# make and set up our bouncing ball
ball = sphere(pos = (1,5,1), radius = 1, color = color.yellow)
ball2 = sphere(pos = (1,5,1), radius = 1, color = color.red)
ball.velocity = vector(3,20,0) # starting velocity in m/s
ball2.velocity = ball.velocity
ball.accel = vector(0,0,0)    # starig acceleration in m/s^2
ball2.accel = ball.accel
ball.mass = 2.0               # staring mass in kg
ball2.mass = ball.mass
gravity = 9.8                 # acceleration du to gravity in m/s^2
coeff_rest = .9               # % velocity remains after collision
p = 1.2                       # air density

ball.b = .1 # drag coefficient
ball2.b = 0

deltat = 0.05 # time step
t = 0         # starting time
t_end = 100    # end time

# set up graph
graph = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "y-velocity vs. time")
velocitycurve = gcurve(display = graph.display, color = color.cyan)

graph2 = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "y-velocity vs. time")
velocitycurve2 = gcurve(display = graph.display, color = color.cyan)


# loop action
while t < t_end:
    # control flow of time -- rate sets loops/sec
    rate(50) # note if this number times deltat is one, we're in "real time"
    t = t + deltat # update time coordinate for plot

    # figure out the net force acting on the ball
    ball.F_gravity = vector(0, -ball.mass*gravity,0) # gravitational force
    ball2.F_gravity = vector(0, -ball2.mass*gravity,0)
    ball.F_drag = drag_equation(ball.b, p, ball.velocity, ball.radius)  
    ball2.F_drag = drag_equation(ball2.b, p, ball2.velocity, ball2.radius)
    ball.F_net = ball.F_gravity + ball.F_drag        # sum of forces
    ball2.F_net = ball2.F_gravity + ball2.F_drag

    ball = update_kinematics(ball)
    ball2 = update_kinematics(ball2)

    #check for collision with the ground
    if ball.pos.y - ball.radius < ground.pos.y:
        ball.velocity.y = -1 * coeff_rest * ball.velocity.y
        ball.pos.y = ball.radius #avoid getting trapped

    if ball2.pos.y - ball2.radius < ground.pos.y:
        ball2.velocity.y = -1 * coeff_rest * ball2.velocity.y
        ball2.pos.y = ball2.radius

    # plot a single point on our graph -- the y-velocity of the ball vs. time
    velocitycurve.plot(pos=(t, ball.velocity.y))
    velocitycurve2.plot(pos=(t, ball2.velocity.y))

