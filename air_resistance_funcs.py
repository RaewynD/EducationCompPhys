# HEADER ################################
# air_resistance_funcs.py               #
#                                       #
# original model by Byron Philhour      #
# template designed by John C. Merfeld  #
#                      & Raewyn Duvall  #
#                                       #
#########################################

# NOTE FOR RAEWYN:
# I'm in the process of stripping this down. See update_kinematics for an
# idea of how I thought that could look

# TODO
# strip it all!
# give equations, tell them to implement


#     You will define the values and functions below, which will be used by
# the main simulation. 
#
#

# IMPORTED PACKAGES #####################
from __future__ import division     # include decimal division
from visual import *                # include standard visual python
from numpy import pi                # include machine-precise value of pi


# GLOBAL CONSTANTS ######################

# add appropriate values here 
# (some of which are known constants!)
g = ?                               # acceleration due to g in m/s^2
rest_coeff = ?                      # percentage of velocity remaining
                                    #     after collision with ground
p = ?                               # air density in kg/m^2

drag_1 = ?                          # drag coefficients for the two balls
drag_2 = 0                          # always compare to zero drag

#########################################


# FUNCTION DEFINITIONS ##################

# initialize
def initialize(name):

    # both spheres should have identitcal initial conditions
    body = sphere(pos = (1,5,1), radius = 1)
    body.velocity = vector(1,20,0)      # starting velocity in m/s
    body.accel = vector(0,0,0)          # starig acceleration in m/s^2
    body.mass = 2.0                     # mass in kg

    # but they should have different appearance and drag behavior
    if name == 1:
        body.color = color.yellow       # color
        body.b = drag_1                 # drag coefficient for object
    if name == 2:
        body.color = color.red          # color
        body.b = drag_2                 # drag coefficient

    return body    

# give equation. Tell them to set it for x and y
def calculate_drag(b, p, v, r):
    
    A = pi*(r**2)
    F_drag = vector(0,0,0)              # these three could be done in one line
    F_drag.x = -0.5*b*p*A*((v.x)**2)    # but it would be huge and gross
    F_drag.y = -0.5*b*p*A*((v.y)**2)

    return F_drag

def calculate_forces(body):

    # first, we make a vector for gravity and assign it to the body

    # the only other force we are concerned with is drag. We can handle this
    #     in a separate function
    body.F_drag = calculate_drag(body.b, p, body.velocity, body.radius)
    
    # are there any other natural forces that may act on the ball? How might
    #     account for them?

    # now, simply find F_net and assign it to the body

    return body

# update_kinematics
#
#     this function takes in a body and a time step. What we want to do is 
# use the forces acting on the body to update its acceleration, then use the
# definitions of acceleration and velocity to update the ball's position and
# velocity
#
#     recall that in our simulation, forces belong to the body and can be 
# accessed with body.F_net
def update_kinematics(body, delta_t):

    # apply Newton's 2nd Law to our object:
    # F = m*a

    # update kinematics of our object:
    # a = delta_v / delta_t
    # v = delta_x / delta_t

    # how can we use this information to appropriately change the ball's
    # velocity and position?
    return body

# collision_check
#
#     this function checks the object's position relative to the ground. If
# the object has in contact with the ground, it should bounce back up
def collision_check(body, ground):

    # check IF the object has made contact with the ground (recall that 
    #     bouncing is a strictly up-and-down motion, so if the ground is flat,
    #     only the y-coordinate of position is relevent)

        # if the ball hit the ground, we need to update its velocity so that
        #     it bounces back up (we should also shift its position up by 
        #     enough so that it does not too close to the ground at the next 
        #     time step
        #
        # what is a good distance to shift the position?
        #
        # how can we account for the ball losing some energy every time it 
        #     hits the ground?

    # if the ball didn't hit the ground, we have nothing to do!
        
    return body

#########################################
