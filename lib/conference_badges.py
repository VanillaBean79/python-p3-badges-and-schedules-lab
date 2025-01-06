def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_names = []
    for name in names:
        badge_names.append(f"Hello, my name is {name}.")
    return badge_names
    # return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    # room_assignments = []
    # for index, name in enumerate(names):
    #     room_number = (index %8) + 1
    #     room_message = f"Hello, {name}! You'll be assigned to room {room_number}!"
    #     room_assignments.append(room_message)
    # return room_assignments
    return [
        f"Hello, {name}! You'll be assigned to room {(index %8) + 1}!"
        for index, name in enumerate(names)
    ]

def printer(names):
    # badge_messages = batch_badge_creator(names)
    # for message in badge_messages:
    #     print(message)
    #     room_assignments = assign_rooms(names)
    # for assignment in room_assignments:
    #     print(assignment)
    # return assignment
    [print(message) for message in batch_badge_creator(names)]
    [print(assignment) for assignment in assign_rooms(names)]