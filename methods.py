from plane import PassengerAgent


def random(model):
    """ Creates one boarding group """
    group = []
    for x in range(3, 19):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(16 * y + x, model, (x, y))
            group.append(agent)
    model.random.shuffle(group)
    model.boarding_groups.append(group)
