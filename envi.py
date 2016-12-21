from collections import deque


class FutureTasks:
    def __init__(self, tasks_list):
        # type: (list, Scheduler) -> None
        tasks_list.sort(key=lambda a:a.emerge_time)
        self.tasks = deque(tasks_list)

    def get_next_in_due(self):
        if len(self.tasks) == 0:
            return None
        else:
            return self.tasks[0]

    def pop_next_in_due(self):
        # type: () -> Task
        return self.tasks.popleft()


class Clock:
    def __init__(self):
        # type: (FutureTasks, Scheduler) -> None
        self.time = 0

    def _next_in_due(self, future_tasks, scheduler):
        future_next_task = future_tasks.get_next_in_due()
        running_task = scheduler.current_task

        if running_task is None:
            if future_next_task is None:
                return 'done'
            else:
                return 'future'
        else:
            if future_next_task is None:
                return 'current'
            else:
                if self.time + running_task.life_remain() <= future_next_task.emerge_time:
                    # running task is in due first
                    return 'current'
                else:
                    # future task is in due first
                    return 'future'

    def work(self, future_tasks, scheduler):
        while True:
            due = self._next_in_due(future_tasks, scheduler)
            if due is 'future':
                mushroom = future_tasks.pop_next_in_due()
                self.time = mushroom.emerge_time

                scheduler.new_arise(mushroom)

            elif due is 'current':
                dying = scheduler.current_task

                self.time += dying.life_remain()

                scheduler.current_finish()

            elif due is 'done':
                break


clock = Clock()


class Task:
    global clock
    clk = clock

    count = 0

    @classmethod
    def gen_id(cls):
        id = cls.count
        cls.count += 1
        return id

    def __init__(self, emerge_time, actual_rt, expected_rt=0):
        self.id = Task.gen_id()

        self.emerge_time = emerge_time
        self.expected_rt = expected_rt
        self.actual_rt = actual_rt
        self.runtime = 0

        self.__start_time = 0

    def life_remain(self):
        return self.actual_rt - self.runtime

    def start(self):
        print self, 'starts',
        print 'at %d' % Task.clk.time
        self.__start_time = Task.clk.time

    def pause(self):
        print self, 'working for %d and pauses' % (Task.clk.time - self.__start_time),
        print 'at %d' % Task.clk.time
        self.runtime += Task.clk.time - self.__start_time

    def finish(self):
        print self, 'finished',
        print 'at %d' % Task.clk.time
        pass

    def __str__(self):
        return '<Task id:%d>' % self.id
