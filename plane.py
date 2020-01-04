from mesa import Model, Agent
from mesa.space import MultiGrid
import numpy as np


def baggage_normal():
    """ Generates a positive integer number from normal distribution """
    value = int(3 + np.random.normal())
    while value < 0:
        value = int(3 + np.random.normal())
    return value


class PassengerAgent(Agent):
    """ An agent with a fixed seat assigned """
    def __init__(self, unique_id, model, seat_pos):
        super().__init__(unique_id, model)
        self.seat_pos = seat_pos
        self.baggage = baggage_normal()

    def step(self):
        pass

    def __str__(self):
        return "ID {}\t: {}".format(self.unique_id, self.seat_pos)


class PlaneModel(Model):
    """ A model representing simple plane consisting of 16 rows of 6 seats (2 x 3) using a given boarding method """
    def __init__(self, method):
        self.grid = MultiGrid(21, 7, False)
        self.running = True
        self.method = method

        # Create agents and splitting them into separate boarding groups accordingly to a given method
        self.boarding_groups = []
        self.method(self)

    def step(self):
        pass
