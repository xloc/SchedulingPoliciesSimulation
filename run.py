import envi as e

clock = e.Clock()

e.Task.set_clock(clock)

tasks = [
    e.Task(0, 4, 4),
    e.Task(1, 3, 3),
    e.Task(2, 5, 5),
    e.Task(3, 2, 2),
    e.Task(4, 4, 4)
]

ft = e.FutureTasks(tasks)

import scheduler_base as schb
# sch = schb.FIFOScheduler()
sch = schb.SJFScheduler()

clock.work(ft, sch)
