# HEADER ################################
# air_resistance_solution.py            #
#                                       #
# original model by Byron Philhour      #
# template designed by John C. Merfeld  #
#                      & Raewyn Duvall  #
#                                       #
#########################################

#     This is a fully implemented sample solution to the problem, for 
# reference and testing. This is by no means the only functional implementation
# and not all the parameters added here are necessary for the functionality
# of the simulatiion.

# IMPORTED PACKAGES #####################
from __future__ import division     # include decimal division
from visual import *                # include standard visual python
from numpy import pi                # include machine-precise value of pi


# GLOBAL CONSTANTS ######################

# add appropriate values here 
# (some of which are known constants!)
g = 9.81                               # acceleration due to g in m/s^2
rest_coeff = .9                      # percentage of velocity remaining
                                    #     after collision with ground
p = 1.2                               # air density in kg/m^2

drag_1 = .1                           # drag coefficients for the two balls
drag_2 = 0

#########################################


# FUNCTION DEFINITIONS ##################

def initialize(name):

    # both spheres should have identitcal initial conditions
    body = sphere(pos = (1,5,1), radius = 1)
    body.velocity = vector(1,20,0)      # starting velocity in m/s
    body.accel = vector(0,0,0)          # starig acceleration in m/s^2
    body.mass = 2.0                     # mass in kg

    # but they should have different appearance and drag behavior
    if name == 1:
        body.color = color.yellow       # color
        body.b = .1                     # drag coefficient for object
    if name == 2:
        body.color = color.red          # color
        body.b = 0                      # drag coefficient

    return body    

def calculate_drag(b, p, v, r):
    
    A = pi*(r**2)
    F_drag = vector(0,0,0)              # these three could be done in one line
    F_drag.x = -0.5*b*p*A*((v.x)**2)    # but it would be huge and gross
    F_drag.y = -0.5*b*p*A*((v.y)**2)

    return F_drag

def calculate_forces(body):

    body.F_g = vector(0, -body.mass*g,0) # gravitational force
    body.F_drag = calculate_drag(body.b, p, body.velocity, body.radius)
    body.F_net = body.F_g + body.F_drag        # sum of forces

    return body


def update_kinematics(body, delta_t):

    # Newton's 2nd Law
    body.accel = body.F_net / body.mass

    #update kinematics
    body.velocity = body.velocity + body.accel*delta_t # delta-v = a * delta-t
    body.pos = body.pos + body.velocity*delta_t        # delta-x = a * delta-a

    return body

def collision_check(body, ground):

    if body.pos.y - body.radius < ground.pos.y:
        body.velocity.y = -1 * rest_coeff * body.velocity.y
        body.pos.y = body.radius #avoid getting trapped

    return body

#########################################

