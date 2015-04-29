# HEADER ################################
# air_resistance_funcs.py               #
#                                       #
# original model by Byron Philhour      #
# template designed by John C. Merfeld  #
#                      & Raewyn Duvall  #
#                                       #
#########################################


# DIRECTIONS:
#     
# Define the functions below that are used in the main simulation.
# Function headers tell you what the function should do, but use the given API
# to write the code.
#
# Notice how certain calculations are easily implemented here though they may
# be tedious when done by hand.
#

# IMPORTED PACKAGES #####################
from __future__ import division     # include decimal division
from visual import *                # include standard visual python
from numpy import pi                # include machine-precise value of pi


# GLOBAL CONSTANTS ######################

# TODO: add appropriate values here
g = ?               # acceleration due to g in m/s^2
rest_coeff = ?      # percentage of velocity remaining
                    #     after collision with ground
p = ?               # air density in kg/m^2

drag_1 = ?          # drag coefficient for one ball
drag_2 = 0          # other ball always zero drag for comparison

#########################################


# FUNCTION DEFINITIONS ##################


# function: initialize
# input: name
# output: 3D object (body)
# implementation: initialize a 3d object with the following properties:
#       body is a sphere with pos=(x,y,z) and radius=d (you decide x,y,z,d)
#       body has initial velocity vector of 
#           x along the x-axis (you decide x)
#           y along the y-axis (you decide y)
#           0 along the z-axis [(sorry, but this must be zero)]
#       body has initial zero acceleration vector
#       body has mass of m (you decide m)
#       if name==1 then body has color yellow and drag of drag_1
#       if name==2 then body has color red and drag of drag_2
#       note: the name is for differentiating the balls in the simulation
#       note: the balls have all the same properties besides color and drag to
#           show differences based solely on drag in this simulation
def initialize(name):

    # TODO: write initializations here

    return body    

# Why can you choose some initialization values for variables
# while others should be set to specific values, such as acceleration?


# function: calculate_drag
# input: b - drag of ball
#        p - density of air
#        v - velocity of ball
#        r - radius of ball
# output: F_drag - drag force on ball
# implementation: calculates the drag force on the ball by the following:
#       calulates area [hint: with A=pi*r^2]
#       initializes a zero drag force vector
#       sets drag force of x-axis and y-axis using the following formula:
#           drag = -0.5*b*p*A*velocity^2
#       note: velocity in this case is split into components corresponding to each axis
#       note: the syntax for x^2 in python is x**2
def calculate_drag(b, p, v, r):
    
    # TODO: write drag calculations here

    return F_drag

# How does this code for drag simplify the actual calculations?
# Do you know how the drag coefficient is actually derived? If so, how would
#       computation help in this derivation?


# function: calculate_forces
# input: body
# output: body
# implementation: set forces on body using the following:
#       set force of gravity on the body [hint: to -mg]
#       set force of drag on the body by calculate_drag
#       set net force on the body [to force of gravity plus force of drag]
def calculate_forces(body):

    # TODO: set the forces on the body here

    return body

# Are there any other natural forces that may act on the ball?
# How might you account for them?


# function: update_kinematics
# input: body
#        delta_t
# output: body
# implementation: update the kinematics of body with the following:
#       update acceleration of body using Newton's 2nd Law, F=ma
#       update velocity of body using the equation for velocity
#           as compared to acceleration           [hint: v=aΔt]
#       update position of body using the equation for position
#           as compared to velocity               [hint: p=vΔt]
def update_kinematics(body, delta_t):

    # TODO: update kinematics of the body here

    return body

# Why is the order of update acceleration, velocity, and then position?
# Does the order matter or could we do it position, velocity, then
#       acceleration, or even position, acceleration, and then velocity?
# What would be different in the simulation if the order was changed?


# function: collision_check
# input: body
#        ground
# output: body
# implementation: handle body's collision with ground by the following:
#       check if body has hit ground
#           if y of body minus radius of body is less than y of ground:
#               set y velocity of ball to go oposite direction and
#                   with only a percentage of it's current velocity
#                   note: this calculation is only relivant to the y-axis
#                       when ground is flat
#               update position y to avoid getting trapped
#                   note: if y is overlapping ground due to overcalculation
#                       in a timestep, it may get stuck in an infinite loop
#                       of switching its direction, so determine a good
#                       distance to shift the position
def collision_check(body, ground):

    # TODO: write code for collision check here
        
    return body

# Is there another way to determine where to shift the ball to avoid trapping?
# Why does the ball only keep a percentage of its velocity when it collides?
# Do you know how the resitance coefficient is actually derived? If so, how
#       would computation help in this derivation?


#########################################
