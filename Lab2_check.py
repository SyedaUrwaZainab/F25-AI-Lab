class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        if target == self.previous_mode:
            command = "No command"
        else:
            command = "Send command"
            self.previous_mode = target

        return target, command


agent = ClassroomAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]

for percept in percepts:
    previous = agent.previous_mode
    target, command = agent.act(percept[0], percept[1])

    print("Previous mode:", previous)
    print("Percept:", percept)
    print("Target mode:", target)
    print("Outcome:", command)
    print("--------------------")
