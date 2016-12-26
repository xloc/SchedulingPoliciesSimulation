class Scheduler:
    def __init__(self):
        self.current_task = None
        self.ready_tasks = []

    def new_arise(self, task):
        self.ready_tasks.append(task)
        self.switch()

    def current_finish(self):
        self.current_task.finish()
        self.current_task = None
        if len(self.ready_tasks) > 0:
            self.switch()

    def set_current(self, new_current):
        if self.current_task is None:
            self.current_task = new_current
            self.current_task.start()
        else:
            self.current_task.pause()
            self.ready_tasks.append(self.current_task)
            self.current_task = new_current
            self.current_task.start()

    def switch(self):
        # Find the task switching to
        # Deque from the ready list
        # And use self.set_current(task) to switch
        pass


def maxi(iterable, key):
    mx = -10000000
    idx = 0

    for i, item in enumerate(iterable):
        if key(item) > mx:
            mx = key(item)
            idx = i

    return idx, mx


class FIFOScheduler(Scheduler):
    def __init__(self):
        Scheduler.__init__(self)
        self.is_first_arise = True

    def new_arise(self, task):
        self.ready_tasks.append(task)

        if self.is_first_arise:
            self.is_first_arise = False
            self.switch()

    def switch(self):

        # i, choice = maxi(self.ready_tasks, key=lambda a: a.emerge_time)
        choice = min(self.ready_tasks, key=lambda a: a.emerge_time)
        self.ready_tasks.remove(choice)

        self.set_current(choice)


class SJFScheduler(Scheduler):
    def __init__(self):
        Scheduler.__init__(self)
        self.is_first_arise = True

    def new_arise(self, task):
        self.ready_tasks.append(task)

        if self.is_first_arise:
            self.is_first_arise = False
            self.switch()

    def switch(self):
        choice = min(self.ready_tasks, key=lambda a: a.expected_rt)
        self.ready_tasks.remove(choice)

        self.set_current(choice)
