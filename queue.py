from mesa.time import BaseScheduler
from collections import OrderedDict


class QueueActivation(BaseScheduler):
    def __init__(self, model):
        super().__init__(model)
        self._priority_agents = OrderedDict()

    def step(self):
        for agent in self.agent_buffer():
            agent.step()
        self.time += 1
        self.steps += 1

    def add_priority(self, agent):
        self._priority_agents[agent.unique_id] = agent

    def remove_priority(self, agent):
        del self._priority_agents[agent.unique_id]

    def get_agent_count(self):
        return len(self._agents) + len(self._priority_agents)

    def agent_buffer(self, shuffled=False):
        for a in self.model.shuffle_cords:
            for agent in self.agent_buffer():
                if agent.seat_pos[0] == a[0] and agent.seat_pos[1] == a[1]:
                    agent.state = "SZUFLA"
                    self.add_priority(agent)

        for agent in self.agent_buffer():
            if agent.state == "BACK":
                self.add_priority(agent)
                
        self.model.shuffle_cords = []

        priority_keys = list(self._priority_agents.keys())
        if len(priority_keys) > 0:
            for key in priority_keys:
                if key in self._priority_agents:
                    yield self._priority_agents[key]
        else:
            agent_keys = list(self._agents.keys())
            for key in agent_keys:
                if key in self._agents:
                    yield self._agents[key]
