import math
import matplotlib.pyplot as plt
import numpy as np

# A quick function to help us make sure our parameters don't spiral out of control:
# Takes in a value and an upper and lower limit and if the value is outside of the limits, "round" it to the edge of the limit


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


# How many iterations until we end one simulation--if the curves start flattening out you might want to increase this
max_weeks = 52
# How many simulations you want to do--one simulation is fine, but multiple allows you to see the variance.
num_sims = 1


fig, axs = plt.subplots(2)          # Setting up plots
#fig, axs = plt.subplots()
weeks = range(1, max_weeks + 1)     # X-axis vector

for i in range(num_sims):

    # P(opulation) = S(usceptible) + I(nfected) + R(ecovered)
    total_population = 300000000
    num_infected = 10
    num_susceptible = total_population - num_infected
    num_recovered = 0

    # Num interactions/person/week: does this seem like a reasonable assumption?
    avg_interactions_per_week = 5
    # Chance that an interaction creates an infection (given susceptibility): does this seem reasonable?
    infection_prob = .3

    # Chance that an infected person recovers (or dies) by the next week
    recovery_prob = .6

    new_cases = []
    total_cases = []
    for week in range(1, max_weeks + 1):

        # Each of our parameters varies a little week-to-week
        avg_interactions_per_week += np.random.normal(0, .1, 1)[0]
        avg_interactions_per_week = constrain(avg_interactions_per_week, 3, 10)

        # But it's not clear if they trend in any particular direction
        infection_prob += np.random.normal(0, .005, 1)[0]
        infection_prob = constrain(infection_prob, .2, .4)

        # No matter what, they don't go outside of some reasonable bounds
        recovery_prob += np.random.normal(0, .005, 1)[0]
        recovery_prob = constrain(recovery_prob, .5, .7)

        prop_susceptible = num_susceptible / total_population
        new_recoveries = math.floor(num_infected * recovery_prob)
        new_cases.append(math.floor(
            num_infected * avg_interactions_per_week * prop_susceptible * infection_prob))

        # Move new recoveries from infected to recovered
        num_recovered += new_recoveries
        num_infected -= new_recoveries

        # Move new cases from susceptible to infected
        num_infected += new_cases[week-1]
        num_susceptible -= new_cases[week-1]

        total_cases.append(num_recovered+num_infected)

        #print(f"Week {week}:")
        #print(f"There were {new_cases[week-1]} new cases this week.")
        #print(f"That makes our new cumulative case count {num_recovered + num_infected}")
        #print(f"{new_recoveries} people recovered this week.")

    # Draw plots of the new cases each week and the total cases
    axs[0].plot(weeks, new_cases)
    axs[1].plot(weeks, total_cases)
    #axs.plot(weeks, new_cases)


plt.xlabel("Week")
plt.ylabel("Infections")
plt.show()
