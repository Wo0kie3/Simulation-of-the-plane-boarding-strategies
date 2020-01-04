from mesa.time import BaseScheduler


class QueueActivation(BaseScheduler):

    def step(self):
        for agent in self.agent_buffer():
            agent.step()
        self.time += 1

