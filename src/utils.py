import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import base64
from io import BytesIO

class Individual:
    """
    An individual has an initial state, where he is 100% a specific person.
    As the time and the days goes he might change. We can define the probability of him changing,
    And by how much percent he will change by day (if he does).
    
    Of course it is also possible to change back to the original person, growth does not always go in one direction.
    
    We can also decide to let the individual change to a random new person, showing that two changes on the row on the same part of an individual will result in a fully new individual who's neither the first nor the second individual.
    
    :param change_probability: The probability of the individual changing to a new person. A value between 0 and 1
    :param change_percent: The percent of the individual changing to a new person per day. A value between 0 and 100
    :param change_to_random: If the individual should change to a random new person. For visualization, we considered only 20 different "person"
    A boolean value.
    """
    
    def __init__(self, change_probability: float, nb_change_percent: int, change_to_random: bool):
        self.change_probability = change_probability
        self.nb_change_percent = nb_change_percent
        self.change_to_random = change_to_random
        self.days = 0 # Days since the individual was created
        self.state = np.ones(100, dtype=int)
     
    def change(self):
        """
        Change the individual to a new person, if the change_probability is met.
        """
        
        # we increase the days
        self.days += 1
        if random.random() < self.change_probability: # We check if the individual should change today
            indices = random.sample(range(100), self.nb_change_percent) 
            for index in indices:
                if self.change_to_random:
                    self.state[index] = random.randint(0,20) # we limit to 20 different type of individual
                else:
                    if self.state[index] == 0: 
                        self.state[index] = 1
                    else:
                        self.state[index] = 0
    
    def __getitem__(self,item):
        return self.state[item]
    
    def reset(self):
        """
        Reset the individual to its initial state
        """
        
        self.state = np.ones(100, dtype=int)
        self.days = 0
        

    def __repr__(self) -> str:
        return f"{self.state}"
if __name__ == '__main__':
    plt.ion()
    plt.figure()
    
    individual = Individual(0.1,1, True)
    print(individual.days)    
    while True:
        individual.change()
        individual.update_plot()
        if  all(x == individual.state[0] and x!= 0 for x in individual.state):
            break
        if all(x != 0 for x in individual.state):
            print(f"it took {individual.days} to fully change")
            break