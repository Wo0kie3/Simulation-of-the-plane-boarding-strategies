import plane

def random(model):
    """ Creates one boarding group """
    id = 1
    group = []
    for x in range(3, 19):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 1)
            id += 1
            group.append(agent)
    model.random.shuffle(group)
    model.boarding_queue.extend(group)


def front_to_back_gr(model):
    final_group = []
    id = 1
    sub_group = []
    for x in range(18, 14, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 4)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(14, 10, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 3)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(10, 6, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 2)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(6, 2, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 1)
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
            agent = plane.PassengerAgent(id, model, (x, y), 4)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(10, 6, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 3)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(14, 10, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 2)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)
    sub_group = []
    for x in range(18, 14, -1):
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    for a in sub_group:
        final_group.append(a)

    model.boarding_queue.extend(final_group)


def front_to_back(model):

    final_group = []
    group_id = 16
    id = 1
    for x in range(18,2,-1):
        sub_group = []
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), group_id)
            id += 1
            sub_group.append(agent)
        model.random.shuffle(sub_group)
        final_group.extend(sub_group)
        group_id -= 1

    model.boarding_queue.extend(final_group)


def back_to_front(model):

    final_group = []
    group_id = 16
    id = 1
    for x in range(3, 19):
        sub_group = []
        for y in (0, 1, 2, 4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), group_id)
            id += 1
            sub_group.append(agent)
        model.random.shuffle(sub_group)
        final_group.extend(sub_group)
        group_id -= 1

    model.boarding_queue.extend(final_group)


def win_mid_ais(model):

    final_group = []
    id = 1
    sub_group = []
    for y in (2, 4):
        for x in range(3,19):
            agent = plane.PassengerAgent(id, model, (x, y), 3)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    final_group.extend(sub_group)

    sub_group = []
    for y in (1, 5):
        for x in range(3, 19):
            agent = plane.PassengerAgent(id, model, (x, y), 2)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    final_group.extend(sub_group)

    sub_group = []
    for y in (0, 6):
        for x in range(3,19):
            agent = plane.PassengerAgent(id, model, (x, y), 1)
            id += 1
            sub_group.append(agent)
    model.random.shuffle(sub_group)
    final_group.extend(sub_group)

    model.boarding_queue.extend(final_group)


def steffen_perfect(model):

    final_group = []
    id = 1
    for y in (2, 4):
        for x in range(3, 19, 2):
            agent = plane.PassengerAgent(id, model, (x, y), 6)
            id += 1
            final_group.append(agent)
    for y in (2, 4):
        for x in range(4, 19, 2):
            agent = plane.PassengerAgent(id, model, (x, y), 5)
            id += 1
            final_group.append(agent)
    for y in (1, 5):
        for x in range(3, 19, 2):
            agent = plane.PassengerAgent(id, model, (x, y), 4)
            id += 1
            final_group.append(agent)
    for y in (1, 5):
        for x in range(4, 19, 2):
            agent = plane.PassengerAgent(id, model, (x, y), 3)
            id += 1
            final_group.append(agent)
    for y in (0, 6):
        for x in range(3, 19, 2):
            agent = plane.PassengerAgent(id, model, (x, y), 2)
            id += 1
            final_group.append(agent)
    for y in (0, 6):
        for x in range(4, 19, 2):
            agent = plane.PassengerAgent(id, model, (x, y), 1)
            id += 1
            final_group.append(agent)

    model.boarding_queue.extend(final_group)


def steffen_modified(model):
    group = []
    id = 1
    for x in range(3, 19, 2):
        for y in (2, 1, 0):
            agent = plane.PassengerAgent(id, model, (x, y), 4)
            id += 1
            group.append(agent)
    # model.random.shuffle(group)
    model.boarding_queue.extend(group)
    group = []
    for x in range(3, 19, 2):
        for y in (4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 3)
            id += 1
            group.append(agent)
    # model.random.shuffle(group)
    model.boarding_queue.extend(group)
    group = []
    for x in range(4, 19, 2):
        for y in (2, 1, 0):
            agent = plane.PassengerAgent(id, model, (x, y), 2)
            id += 1
            group.append(agent)
    # model.random.shuffle(group)
    model.boarding_queue.extend(group)
    group = []
    for x in range(4, 19, 2):
        for y in (4, 5, 6):
            agent = plane.PassengerAgent(id, model, (x, y), 1)
            id += 1
            group.append(agent)
    # model.random.shuffle(group)
    model.boarding_queue.extend(group)
