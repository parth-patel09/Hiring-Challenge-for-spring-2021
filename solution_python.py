class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undoactions = []
        self.redoactions = []
 
    def add(self, num: int):
        self.redoactions.append({
            'operation': self.add,
            'to_perform': self.subtract,
            'value': num
        })
        self.value = self.value + num
        pass

    def subtract(self, num: int):
        self.redoactions.append({
            'operation': self.subtract,
            'to_perform': self.add,
            'value': num
        })
        self.value = self.value - num
        pass

    def undo(self):
        if len(self.redoactions) > 0:
            last_action = self.redoactions[-1]
            del self.redoactions[-1]
            last_action['to_perform'](last_action['value'])
            self.undoactions.append(last_action)
        pass

    def redo(self):
        if len(self.undoactions) > 0:
            last_action = self.undoactions[-1]
            last_action['operation'](last_action['value'])
            self.redoactions.append(last_action)
            del self.undoactions[0]
        pass

    def bulk_undo(self, steps: int):
        if steps <= len(self.redoactions):
            index = -1 * steps
            last_actions = self.redoactions[index:]
            for action in last_actions:
                action['to_perform'](action['value'])
        pass

    def bulk_redo(self, steps: int):
        index = -1 * steps
        last_actions = self.undoactions[index:]
        for action in last_actions:
            action['operation'](action['value'])
        pass
