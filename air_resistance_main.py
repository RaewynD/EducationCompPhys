# HEADER ################################
# air_resistance_main.py                #
#                                       #
# original model by Byron Philhour      #
# template designed by John C. Merfeld  #
#                      & Raewyn Duvall  #
#                                       #
#########################################

#     You do not need to modify this code. This is the main simulation,
# which sets up the system, runs it, and graphs it. You will write the
# functions that govern the physics of the system in air_resistance_funcs.py
#
#     You may modify this code; doing so may yield interesting results,
# but for the simulation to run, you must complete the template in the
# the funcs file. This will be an important reference and should help you
# figure out what each function is responsible for.

# INCLUDE THE CODE YOU WILL WRITE #######

import air_resistance_funcs


# GRPAH AND VISUALIZATION SETUP #########

# graphs:
graph_1 = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "YELLOW y-velocity vs. time")
velocitycurve_1 = gcurve(display = graph.display, color = color.cyan)

graph2_2 = gdisplay(x = 0, y = 400, width = 425, height = 400, \
                 title = "RED y-velocity vs. time")
velocitycurve_2 = gcurve(display = graph.display, color = color.cyan)

# visualize ground in the simulation:
ground = box(pos = (0,0,0), size = (15,0.1,100), color = color.green)


# INITIALIZE OBJECTS ####################

ball_1 = initialize(1)
ball_2 = initialize(2)


# DISCRETIZE SYSTEM #####################

deltat = 0.01 # time step
t_0 = 0         # starting time
t_end = 100   # end time


# SIMULATE THROUGH TIME #################

for t in range(t_0, t_end):

    # calculate forces
    ball_1 = calculate_forces(ball_1, p)
    ball_2 = calculate_forces(ball_2, p)

    # respond to forces
    ball_1 = update_kinematics(ball_1)
    ball_2 = update_kinematics(ball_2)

    # check for collision with the ground
    ball_1 = collision_check(ball_1, ground)
    ball_2 = collision_check(ball_2, ground)

    # plot a single point on our graph -- the y-velocity of the ball vs. time
    velocitycurve_1.plot(pos=(t, ball_1.velocity.y))
    velocitycurve_2.plot(pos=(t, ball_2.velocity.y))

    # update time coordinate for plot
    t = t + deltat
    rate(100)    # rate (frequency)
                 # stops computation for 1 / frequency seconds



