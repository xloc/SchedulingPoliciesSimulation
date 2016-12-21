import envi as e

clock = e.Clock()

tasks = [
    e.Task(0, 1),
    e.Task(1, 100),
    e.Task(2, 1),
    e.Task(3, 100),
]

ft = e.FutureTasks(tasks)

import scheduler_base as schb
sch = schb.FIFOScheduler()

clock.work(ft, sch)
