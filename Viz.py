from plane import PlaneModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

colors = [
    'blue', 'cyan', 'orange', 'yellow', 'magenta', 'purple', '#103d3e', '#9fc86c',
    '#b4c2ed', '#31767d', '#31a5fa', '#ba96e0', '#fef3e4', '#6237ac', '#f9cacd', '#1e8123'
]

def passenger_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "Color": "grey",
                 "r": 0.9}

    portrayal['Color'] = colors[agent.group - 1]

    if agent.state == "FINISHED":
        portrayal["Layer"] = 0
    elif agent.state == "BAGGAGE":
        portrayal["Color"] = "brown"

    return portrayal


grid = CanvasGrid(passenger_portrayal, 21, 7, 840, 310)

method_choice = UserSettableParameter('choice', 'Boarding method', value='Random',
                                                choices=list(PlaneModel.method_types.keys()))

server = ModularServer(PlaneModel,
                       [grid],
                       "Boarding Simulation",
                       {"method": method_choice})
server.port = 8521 # The default
server.launch()
