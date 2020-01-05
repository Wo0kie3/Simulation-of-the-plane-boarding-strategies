from plane import PlaneModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import methods

def passenger_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "Color": "grey",
                 "r": 0.9}
    if agent.group == 1:
        portrayal["Color"] = "blue"
    elif agent.group == 2:
        portrayal["Color"] = "cyan"
    elif agent.group == 3:
        portrayal["Color"] = "purple"
    elif agent.group == 4:
        portrayal["Color"] = "magenta"
    elif agent.group == 5:
        portrayal["Color"] = "orange"
    elif agent.group == 6:
        portrayal["Color"] = "yellow"

    if agent.state == "FINISHED":
        portrayal["Layer"] = 0
    elif agent.state == "BAGGAGE":
        portrayal["Color"] = "brown"

    return portrayal


grid = CanvasGrid(passenger_portrayal, 21, 7, 840, 310)
server = ModularServer(PlaneModel,
                       [grid],
                       "Boarding Simulation",
                       {"method": methods.steffen_perfect})
server.port = 8521 # The default
server.launch()
