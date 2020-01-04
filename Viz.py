from PlaneModel import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def passenger_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0.2,
                 "Color": "grey",
                 "r": 0.9}
    return portrayal

grid = CanvasGrid(passenger_portrayal, 20, 7, 800, 280)
server = ModularServer(PlaneModel,
                       [grid],
                       "Money Model",
                       {"N":51, "width":17, "height":7})
server.port = 8521 # The default
server.launch()
