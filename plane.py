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
    def __init__(self, unique_id, model, seat_pos, group):
        super().__init__(unique_id, model)
        self.seat_pos = seat_pos
        self.baggage = baggage_normal()
        self.x = seat_pos[0]
        self.y = seat_pos[1]
        self.group = group
        self.my_x = 0
        self.my_y = 3
    def step(self):
        if self.x != self.seat_pos:
            self.move()
        else:
            #self.store_luggage()
            pass

    def move(self):
        self.model.grid.move_agent(self, (self.x + 1, self.y))
        self.x += 1

    def store_luggage(self):
        #storing luggage and stoping queue
        pass

    def __str__(self):
        return "ID {}\t: {}".format(self.unique_id, self.seat_pos)


class PlaneModel(Model):
    """ A model representing simple plane consisting of 16 rows of 6 seats (2 x 3) using a given boarding method """
    def __init__(self, method):
        self.grid = MultiGrid(21, 7, False)
        self.running = True
        self.method = method
        self.entry_free = True
        self.plane_queue = QueueActivation(self)

        # Create agents and splitting them into separate boarding groups accordingly to a given method
        self.boarding_groups = []
        self.method(self)


    def step(self):
        self.plane_queue.step()
        self.entry_free = True
        if self.entry_free:
            a = self.boarding_groups.pop()
            self.plane_queue.add(a)
            self.grid.place_agent(a, (0, 3))
            self.entry_free = False
