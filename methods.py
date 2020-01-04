from plane import PassengerAgent

def random(model):
    """ Creates one boarding group """
    id = 1
    group = []
    for x in range(3, 19):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            group.append(agent)
    model.random.shuffle(group)
    model.boarding_queue.extend(group)


def back_to_front_gr(model):
    pass


def front_to_back_gr(model):
    pass


def back_to_front(model):
    pass


def back_to_front(model):
    pass


def win_mid_ais(model):
    pass


def steffen_perfect(model):
    pass


def steffen_modified(model):
    pass
