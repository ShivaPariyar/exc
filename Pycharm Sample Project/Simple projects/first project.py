def get_event_date(event):
    return event

def current_users(events):
    events.sort(key = get_event_date)
    machines = {}
    for event in events:
        if event not in machines:
            machines[event] = set()
        if event == "login":
            machines[event].add(event)
        elif event == "logout":
            machines[event].remove(event)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}". format(machine, user_list))