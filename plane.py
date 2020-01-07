from mesa import Model, Agent
from mesa.space import MultiGrid
import queue
import methods
import numpy as np


def baggage_normal():
    """ Generates a positive integer number from normal distribution """
    value = int(4 + np.random.normal() * 4/3)
    while value < 0:
        value = int(4 + np.random.normal())
    return value


class PassengerAgent(Agent):
    """ An agent with a fixed seat assigned """
    def __init__(self, unique_id, model, seat_pos, group):
        super().__init__(unique_id, model)
        self.seat_pos = seat_pos
        self.baggage = baggage_normal()
        self.group = group
        self.state = 'INACTIVE'

    def step(self):
        if self.state == 'GOING' and self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1])):
            self.move(1, 0)

        elif self.pos[0] + 1 == self.seat_pos[0]:
            self.state = "WAIT"
            for k in (0, 1):
                if self.seat_pos[1] == k:
                    if self.model.grid.is_cell_empty(self.seat_pos[0], k):
                        self.model.shuffle_cords.append(self.seat_pos[0], k)
            for k in (4, 5):
                if self.seat_pos[1] == k:
                    if self.model.grid.is_cell_empty(self.seat_pos[0], k):
                        self.model.shuffle_cords.append(self.seat_pos[0], k)

        elif self.state == "WAIT":
            if self.seat_pos[1] == 0:
                if self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1] - 1)) and self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1] - 2)):
                    self.state = "GOING"
            if self.seat_pos[1] == 1:
                if self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1] - 1)):
                    self.state = "GOING"
            if self.seat_pos[1] == 6:
                if self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1] + 1)) and self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1] + 2)):
                    self.state = "GOING"
            if self.seat_pos[1] == 5:
                if self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1] + 1)):
                    self.state = "GOING"

        elif self.state == "SZUFLA":
            if self.seat_pos[1] in (1, 2):
                if self.seat_pos[0] != 3:
                    self.move(0, -1)
            elif self.seat_pos[1] in (4, 5):
                if self.seat_pos[0] != 3:
                    self.move(0, 1)
            elif self.seat_pos[0] == 3:
                if self.seat_pos[1] in (1, 5):
                    self.move(0, 2)
                    self.state = "BACK"
                else:
                    self.move(0, 1)
                    self.state = "BACK"

        elif self.state == "BACK" and self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1])):
            self.move(-1, 0)

        elif self.state == "BACK" and self.seat_pos[1] in (1, 2):
            if self.model.grid.is_cell_empty((self.pos[0], self.pos[1] - 1)):
                self.move(0, -1)

        elif self.state == "BACK" and self.seat_pos[1] in (4, 5):
            if self.model.grid.is_cell_empty((self.pos[0], self.pos[1] + 1)):
                self.move(0, -1)

        elif self.state == "BACK" and self.seat_pos[1] == self.pos[1] and self.seat_pos[0] == self.pos[0]:
            self.state = 'FINISHED'
            for cord in self.model.shuffle_cords:
                if self.pos[0] == cord[0] and self.pos[1] == cord[1]:
                    self.model.shuffle_cords.remove(cord)

        elif self.pos[0] == self.seat_pos[0]:
                self.state = 'BAGGAGE'
                if self.baggage > 0:
                    self.baggage -= 1
                else:
                    self.state = 'SEATING'

        elif self.state == 'SEATING':
            if self.seat_pos[1] in (0, 1, 2):
                self.move(0, -1)
            else:
                self.move(0, 1)
            if self.pos[1] == self.seat_pos[1]:
                self.state = 'FINISHED'
                #self.model.schedule.remove(self)


    def move(self, m_x, m_y):
        self.model.grid.move_agent(self, (self.pos[0] + m_x, self.pos[1] + m_y))

    def __str__(self):
        return "ID {}\t: {}".format(self.unique_id, self.seat_pos)


class PlaneModel(Model):
    """ A model representing simple plane consisting of 16 rows of 6 seats (2 x 3) using a given boarding method """

    method_types = {
        'Random': methods.random,
        'Front-to-back': methods.front_to_back,
        'Front-to-back (4 groups)': methods.front_to_back_gr,
        'Back-to-front': methods.back_to_front,
        'Back-to-front (4 groups)': methods.back_to_front_gr,
        'Window-Middle-Aisle': methods.win_mid_ais,
        'Steffen Perfect': methods.steffen_perfect,
        'Steffen Modified': methods.steffen_modified
    }

    def __init__(self, method):
        self.grid = MultiGrid(21, 7, False)
        self.running = True
        self.schedule = queue.QueueActivation(self)
        self.method = self.method_types[method]
        self.entry_free = True

        self.shuffle_cords = []
        # Create agents and splitting them into separate boarding groups accordingly to a given method
        self.boarding_queue = []
        self.method(self)

    def step(self):
        self.schedule.step()

        if self.grid.is_cell_empty((0, 3)):
            self.entry_free = True

        if self.entry_free and len(self.boarding_queue) > 0:
            a = self.boarding_queue.pop()
            a.state = 'GOING'
            self.schedule.add(a)
            self.grid.place_agent(a, (0, 3))
            self.entry_free = False

        if self.schedule.get_agent_count() == 0:
            self.running = False
