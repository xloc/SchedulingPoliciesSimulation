import envi as e
import scheduler_base as schb


# Initialize Simulation
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


# Initialize Scheduler

# sch = schb.FIFOScheduler()
sch = schb.SJFScheduler()


# Run Simulation
clock.work(ft, sch)


# Print Report
print "-" * 50
worktime = sum([t.actual_rt for t in tasks])
for t in tasks:
    time_pattern = list(' ' * worktime)
    for st, ed in t.timeline:
        time_pattern[st:ed] = '-'*(ed-st)
    time_pattern = ''.join(time_pattern)

    print str(t), '|', time_pattern, '| %5d | %.2f' % (t.turnover, t.weighted_turnover)
