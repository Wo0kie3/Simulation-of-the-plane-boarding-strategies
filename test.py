from plane import PlaneModel
import methods

model = PlaneModel(methods.random)
for group in range(len(model.boarding_groups)):
    print("### GROUP {} ###".format(group + 1))
    for agent in model.boarding_groups[group]:
        print(agent)
