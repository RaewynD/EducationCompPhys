# HEADER ################################
# air_resistance_funcs.py               #
#                                       #
# original model by Byron Philhour      #
# template designed by John C. Merfeld  #
#                      & Raewyn Duvall  #
#                                       #
#########################################

#     You will define the values and functions below, which will be used by
# the main simulation. 
#
#

# IMPORTED PACKAGES #####################
from visual import *                # include standard visual python
from visual.graph import *          # include graphing features
from __future__ import division     # include decimal division
from numpy import pi                # include machine-precise value of pi


# GLOBAL CONSTANTS ######################

# add appropriate values here 
# (some of which are known constants!)
g = ?                               # acceleration due to gravity in m/s^2
rest_coeff = ?                      # percentage of velocity remaining
                                    #     after collision with ground
p = ?                               # air density in kg/m^2

drag_1 = ?                           # drag coefficients for the two balls
drag_2 = ?

#########################################


# FUNCTION DEFINITIONS ##################

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

#########################################
