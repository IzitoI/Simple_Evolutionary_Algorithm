from EA_Hyperparameters import *
from EA_Functions import *


# Create an initial sets of warms
warms = create_initial_population(SET_SIZE, LOWEST_NUMBER, HIGHEST_NUMBER)
print("Initial set:")
print(warms)
print()


while BUDGET > 0:

    print()
    print("#################### ITERATION NR: {} ####################".format(ITERATION_STARTING))
    ITERATION_STARTING += 1

    # Order the set of warms based on the error
    warms_sorted = sort(warms, SET_SIZE)

    worms_survived = select_survivors(warms_sorted, SET_SIZE)
    print("Warms survived:")
    print(worms_survived)
    print()

    end, error = evaluation(worms_survived[0][1], SET_SIZE, TOLERANCE)
    print("Error: {}".format(error))

    if end:
        BUDGET -= 1
        print("Solution has been found: {}, budget left: {}, error: {}".format(worms_survived[0], BUDGET, error))
        best_population = save_best_population(worms_survived)
        break
    else:
        BUDGET -= 1

    if BUDGET == 0:
        print("Best solution found: {}, no budget left, error: {}".format((worms_survived[0]), error))
        best_population = save_best_population(worms_survived)
        break

    # Select a couple of parents based on their error
    parents = select_parents(worms_survived, NUMBER_OF_PARENTS)
    # print("Parents:")
    # print(parents)
    # print()

    # Generate offspring by recombination of the parents
    offspring = generate_offspring(parents, NUMBER_OF_CHILDREN)
    # print("Offspring before mutation:")
    # print(offspring)
    # print()

    mutated_offspring = mutate_offspring_and_update_population(offspring, warms, MUTATION_STEP_SIZE, LOWEST_NUMBER,
                                                               HIGHEST_NUMBER)
    # print("Offspring after mutation:")
    # print(offspring)
    # print()
