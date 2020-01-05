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


def front_to_back_gr(model):
    final_group = []
    id = 1
    sub_group = []
    for x in range(19, 15, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(15, 11, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 2)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(11, 7, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(7, 3, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    model.boarding_queue.extend(final_group)


def back_to_front_gr(model):
    final_group = []
    id = 1
    sub_group = []
    for x in range(6, 2, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(10, 6, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(14, 10, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 2)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(18, 14, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)

    model.boarding_queue.extend(final_group)


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
