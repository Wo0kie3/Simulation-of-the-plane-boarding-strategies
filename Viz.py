from plane import PlaneModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import methods

def passenger_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0.2,
                 "Color": "grey",
                 "r": 0.9}
    return portrayal

grid = CanvasGrid(passenger_portrayal, 21, 7, 840, 310)
server = ModularServer(PlaneModel,
                       [grid],
                       "Boarding Simulation",
                       {"method": methods.random})
server.port = 8521 # The default
server.launch()
