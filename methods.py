from plane import PassengerAgent

def random(model):
    """ Creates one boarding group """
    group = []
    for x in range(3, 19):
        for y in (0, 1, 2, 4, 5, 6):
            agent = PassengerAgent(16 * y + x, model, (x, y), 1)
            group.append(agent)
    model.random.shuffle(group)
    model.boarding_groups.append(group)

def back_to_front_gr(model):
    pass
def front_to_back_gr(model):
    None

def back_to_front(model):
    None

def back_to_front(model):
    None

def win_mid_ais(model):
    None

def steffen_perfect(model):
    None

def steffen_modified(model):
    None

