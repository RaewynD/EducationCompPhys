# air_resistance.py

# original code by Byron Philhour
# modified by Raewyn Duvall & John C. Merfeld

# DONE:
#   drag coefficient now takes area into account
#   drag force now functionalized

# TODO

# primary:
# build boilerplate code appropriately 

# secondary:
# ensure that air resistance is discussed, the key concept being that it is
#   dependent on velocity
# this code is probably the most intuitive way to understand it, really. We 
#   need to facilitate that
# starting by thowing them up might be more useful than bouncing, as it
#   reveals other interesting features of the problem
# make sure the syntax and possible operations for objects are made clear
#   in the tutorial / outline
#   include members it can hold, ways we can act on it
# good way to introduce things like the rest coefficient: "How can we modify
#   this so that the ball loses energy each time it hits the ground?"
# always be asking questions. Talk about discretization, why it is necessary,
#   and how it can be coded
#   

from __future__ import division # import decimal division
from visual import *            # import standard visual python
from visual.graph import *      # import graphing features
from numpy import pi

# global constants:
gravity = 9.8                 # acceleration du to gravity in m/s^2
coeff_rest = .9               # % velocity remains after collision
p = 1.2                       # air density

# function definition:

def drag_equation(b, p, v, r):
    
    A = pi*(r**2)
    F_drag = vector(0,0,0)            # these three could be done in one line
    F_drag.x = -0.5*b*p*A*((v.x)**2)  # but it would be huge and gross
    F_drag.y = -0.5*b*p*A*((v.y)**2)

    return F_drag

def calculate_forces(body, p):

    body.F_gravity = vector(0, -body.mass*gravity,0) # gravitational force
    body.F_drag = drag_equation(body.b, p, body.velocity, body.radius)
    body.F_net = body.F_gravity + body.F_drag        # sum of forces

    return body


def update_kinematics(body):

    # Newton's 2nd Law
    body.accel = body.F_net / body.mass

    #update kinematics
    body.velocity = body.velocity + body.accel*deltat # delta-v = a * delta-t
    body.pos = body.pos + body.velocity*deltat        # delta-x = a * delta-a

    return body

def collision_check(body, ground, coeff_rest):

    if body.pos.y - body.radius < ground.pos.y:
        body.velocity.y = -1 * coeff_rest * body.velocity.y
        body.pos.y = body.radius #avoid getting trapped

    return body

# make the floor
ground = box(pos = (0,0,0), size = (15,0.1,100), color = color.green)

# make and set up our bouncing ball
ball = sphere(pos = (1,5,1), radius = 1, color = color.yellow)
ball2 = sphere(pos = (1,5,1), radius = 2, color = color.red)
ball.velocity = vector(3,20,0) # starting velocity in m/s
ball2.velocity = ball.velocity
ball.accel = vector(0,0,0)    # starig acceleration in m/s^2
ball2.accel = ball.accel
ball.mass = 2.0               # staring mass in kg
ball2.mass = ball.mass

ball.b = .1 # drag coefficient
ball2.b = .1

deltat = 0.01 # time step
t = 0         # starting time
t_end = 100   # end time

# set up graph
graph = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "y-velocity vs. time")
velocitycurve = gcurve(display = graph.display, color = color.yellow)

graph2 = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "y-velocity vs. time")
velocitycurve2 = gcurve(display = graph.display, color = color.red)


# simulate through time:
while t < t_end:
    # control flow of time -- rate sets loops/sec
    rate(100)    # rate (frequency)
                 # stops computation for 1 / frequency seconds

    # calculate forces
    ball = calculate_forces(ball, p)
    ball2 = calculate_forces(ball2, p)

    # respond to forces
    ball = update_kinematics(ball)
    ball2 = update_kinematics(ball2)

    # check for collision with the ground
    ball = collision_check(ball, ground, coeff_rest)
    ball2 = collision_check(ball2, ground, coeff_rest)

    # plot a single point on our graph -- the y-velocity of the ball vs. time
    velocitycurve.plot(pos=(t, ball.velocity.y))
    velocitycurve2.plot(pos=(t, ball2.velocity.y))

    # update time coordinate for plot
    t = t + deltat 

