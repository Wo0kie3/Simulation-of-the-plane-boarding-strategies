from plane import PlaneModel
import methods

model = PlaneModel(methods.random)
for agent in model.boarding_queue:
    print(agent)
