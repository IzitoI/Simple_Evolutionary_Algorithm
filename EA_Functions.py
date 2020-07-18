import numpy as np
from random import randint
import pickle
import os


def load_pickle():
    if os.path.isfile("best_solution.pkl"):
        data = pickle.load(open("best_solution.pkl", "rb"))
        if data is not None:
            decision = input('Do you want to use previous data ("Y" or "N"): ').lower()
            if decision == "y":
                return dict(data)
            else:
                return {}
        else:
            print("MESSAGE: No previous data found!")
            return {}
    print("MESSAGE: No previous data found!")
    return {}


def create_initial_population(set_size, lowest_number, highest_number):
    output = load_pickle()
    if output == {}:
        for i in range(set_size):
            output[i] = np.random.randint(low=lowest_number, high=highest_number + 1, size=set_size, dtype=int)
    return output


def calculate_error(lst, set_size):
    return sum([(set_size - element) ** 2 for element in lst])


def sort(dictionary, set_size):
    return sorted(dictionary.items(), key=lambda item: calculate_error(item[1], set_size))


def select_survivors(sorted_list, set_size):
    return sorted_list[:set_size]


def evaluation(lst, set_size, tolerance):
    error = calculate_error(lst, set_size)
    if error <= tolerance:
        return True, error
    return False, error


def save_best_population(lst):
    pickle.dump(lst, open("best_solution.pkl", 'wb'))
    print("MESSAGE: Best population has been pickled!")


def select_parents(lst, number_of_parents):
    return {lst[idx][0]: lst[idx][1] for idx in range(number_of_parents)}


def generate_offspring(dictionary, number_of_children):
    return [[int(np.mean(x)) for x in zip(*dictionary.values())] for _ in range(number_of_children)]


def pos_elements_to_mutate(lst, mutation_step_size):
    return set(randint(0, len(lst) - 1) for _ in range(int(mutation_step_size * len(lst))))


def mutate_offspring_and_update_population(lst, dictionary, mutation_step_size, lowest_number, highest_number):

    mutated_lst = []

    # Mutate children independently from each other
    for element in lst:
        indices = pos_elements_to_mutate(element, mutation_step_size)
        for idx in indices:
            element[idx] = randint(lowest_number, highest_number)
            mutated_lst.append(element)

        # Update the total population by adding the each child
        dictionary[list(dictionary.keys())[-1] + 1] = np.asarray(element)

    return mutated_lst
