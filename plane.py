from mesa import Model, Agent
from mesa.space import MultiGrid
import queue
import methods
import numpy as np


def baggage_normal():
    """ Generates a positive integer number from normal distribution """
    value = int(7 + np.random.normal() * 3)
    while value < 0:
        value = int(7 + np.random.normal() * 3)
    return value


class PassengerAgent(Agent):
    """ An agent with a fixed seat assigned """
    def __init__(self, unique_id, model, seat_pos, group):
        super().__init__(unique_id, model)
        self.seat_pos = seat_pos
        self.group = group
        self.state = 'INACTIVE'
        self.shuffle_dist = 0
        if self.model.shuffle_enable:
            self.shuffle = True
        else:
            self.shuffle = False

        if self.model.common_bags == 'normal':
            self.baggage = baggage_normal()
        else:
            self.baggage = self.model.common_bags


    def step(self):
        if self.state == 'GOING' and self.model.get_patch((self.pos[0] + 1, self.pos[1])).state == 'FREE' and self.model.get_patch((self.pos[0] + 1, self.pos[1])).shuffle == 0:
            if self.model.get_patch((self.pos[0] + 1, self.pos[1])).back == 0 or self.model.get_patch((self.pos[0] + 1, self.pos[1])).allow_shuffle is True:
                self.model.get_patch((self.pos[0] + 1, self.pos[1])).allow_shuffle = False
                self.move(1, 0)
                if self.shuffle:
                    if self.pos[0] + 1 == self.seat_pos[0]:
                        self.state = 'SHUFFLE CHECK'
                if self.pos[0] == self.seat_pos[0]:
                    if self.baggage > 0:
                        self.state = 'BAGGAGE'
                    else:
                        self.state = 'SEATING'

        elif self.state == 'SHUFFLE':
            if self.pos[1] == 3 and self.model.get_patch((self.pos[0] + 1, self.pos[1])).state == 'FREE':
                if self.pos[0] == self.seat_pos[0]:
                    self.shuffle_dist = self.model.get_patch((self.pos[0], self.pos[1])).shuffle
                    self.model.get_patch((self.pos[0], self.pos[1])).shuffle -= 1
                self.move(1, 0)
                self.shuffle_dist -= 1
                if self.shuffle_dist == 0:
                    self.state = 'BACK'
                    if self.pos[0] - self.seat_pos[0] == 2:
                        self.model.schedule.safe_remove_priority(self)
                        self.model.schedule.add_priority(self)
            else:
                if self.pos[1] > 3 and self.model.get_patch((self.pos[0], self.pos[1] - 1)).state == 'FREE':
                    self.move(0, -1)
                elif self.pos[1] < 3 and self.model.get_patch((self.pos[0], self.pos[1] + 1)).state == 'FREE':
                    self.move(0, 1)

        elif self.state == 'BACK' and self.model.get_patch((self.pos[0] - 1, self.pos[1])).state == 'FREE' and self.model.get_patch((self.pos[0] - 1, self.pos[1])).allow_shuffle is False:
            self.move(-1, 0)
            if self.pos[0] == self.seat_pos[0]:
                self.state = 'SEATING'
                self.model.get_patch((self.pos[0], self.pos[1])).back -= 1
                if self.model.get_patch((self.pos[0], self.pos[1])).back == 0:
                    self.model.get_patch((self.pos[0], self.pos[1])).ongoing_shuffle = False

        elif self.state == 'BAGGAGE':
            if self.baggage > 1:
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
                self.model.schedule.safe_remove(self)
                self.model.schedule.safe_remove_priority(self)

        if self.state == 'SHUFFLE CHECK' and self.model.get_patch((self.pos[0] + 1, self.pos[1])).state == 'FREE' and self.model.get_patch((self.pos[0] + 1, self.pos[1])).ongoing_shuffle == False:
            try:
                shuffle_agents = []
                if self.seat_pos[1] in (0, 1):
                    for y in range(2, self.seat_pos[1], -1):
                        local_agent = self.model.get_passenger((self.seat_pos[0], y))
                        if local_agent is not None:
                            if local_agent.state != 'FINISHED':
                                raise Exception()
                            shuffle_agents.append(local_agent)
                elif self.seat_pos[1] in (5, 6):
                    for y in range(4, self.seat_pos[1]):
                        local_agent = self.model.get_passenger((self.seat_pos[0], y))
                        if local_agent is not None:
                            if local_agent.state != 'FINISHED':
                                raise Exception()
                            shuffle_agents.append(local_agent)
                shuffle_count = len(shuffle_agents)
                if shuffle_count != 0:
                    self.model.get_patch((self.seat_pos[0], 3)).shuffle = shuffle_count
                    self.model.get_patch((self.seat_pos[0], 3)).back = shuffle_count
                    self.model.get_patch((self.seat_pos[0], 3)).allow_shuffle = True
                    self.model.get_patch((self.pos[0] + 1, self.pos[1])).ongoing_shuffle = True
                    for local_agent in shuffle_agents:
                        local_agent.state = 'SHUFFLE'
                        self.model.schedule.safe_remove(local_agent)
                        self.model.schedule.add_priority(local_agent)
                self.state = 'GOING'
            except Exception:
                pass

    def move(self, m_x, m_y):
        self.model.get_patch((self.pos[0], self.pos[1])).state = 'FREE'
        self.model.grid.move_agent(self, (self.pos[0] + m_x, self.pos[1] + m_y))
        self.model.get_patch((self.pos[0], self.pos[1])).state = 'TAKEN'

    def store_luggage(self):
        # storing luggage and stopping queue
        pass

    def __str__(self):
        return "ID {}\t: {}".format(self.unique_id, self.seat_pos)


class PatchAgent(Agent):
    def __init__(self, unique_id, model, patch_type, state=None):
        super().__init__(unique_id, model)
        self.type = patch_type
        self.state = state
        self.shuffle = 0
        self.back = 0
        self.allow_shuffle = False
        self.ongoing_shuffle = False

    def step(self):
        pass


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

    def __init__(self, method, shuffle_enable=True, common_bags='normal'):
        self.grid = MultiGrid(21, 7, False)
        self.running = True
        self.schedule = queue.QueueActivation(self)
        self.method = self.method_types[method]
        self.entry_free = True
        self.shuffle_enable = shuffle_enable
        self.common_bags = common_bags
        # Create agents and splitting them into separate boarding groups accordingly to a given method
        self.boarding_queue = []
        self.method(self)

        # Create patches representing corridor, seats and walls
        id = 97
        for row in (0, 1, 2, 4, 5, 6):
            for col in (0, 1, 2):
                patch = PatchAgent(id, self, 'WALL')
                self.grid.place_agent(patch, (col, row))
                id += 1
            for col in range(3, 19):
                patch = PatchAgent(id, self, 'SEAT')
                self.grid.place_agent(patch, (col, row))
                id += 1
            for col in (19, 20):
                patch = PatchAgent(id, self, 'WALL')
                self.grid.place_agent(patch, (col, row))
                id += 1
        for col in range(21):
            patch = PatchAgent(id, self, 'CORRIDOR', 'FREE')
            self.grid.place_agent(patch, (col, 3))
            id += 1

    def step(self):
        self.schedule.step()

        if len(self.grid.get_cell_list_contents((0, 3))) == 1:
            self.get_patch((0, 3)).state = 'FREE'

        if self.get_patch((0, 3)).state == 'FREE' and len(self.boarding_queue) > 0:
            a = self.boarding_queue.pop()
            a.state = 'GOING'
            self.schedule.add(a)
            self.grid.place_agent(a, (0, 3))
            self.get_patch((0, 3)).state = 'TAKEN'

        if self.schedule.get_agent_count() == 0:
            self.running = False

    def get_patch(self, pos):
        agents = self.grid.get_cell_list_contents(pos)
        for agent in agents:
            if isinstance(agent, PatchAgent):
                return agent
        return None

    def get_passenger(self, pos):
        agents = self.grid.get_cell_list_contents(pos)
        for agent in agents:
            if isinstance(agent, PassengerAgent):
                return agent
        return None
