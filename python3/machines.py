import math
from datetime import datetime
import time
from itertools import accumulate


class Machine:
    def __init__(self, type: int, time_fac: int):
        self.at_work = False
        self.type = type
        self.time_fac = time_fac
        self.cost = 2 if type == 1 else 5 if type == 2 else 0
        self.start_time = 0
    def start(self):
        self.at_work = True
        # keep start time in minutes rounded to full minute
        self.start_time = int(datetime.now().timestamp())
    def end(self):
        self.at_work = False
    def get_cost_iteration(self, last_calc_time: int, time_now: int):
        if self.at_work:
            #print("cost: ", self.cost, "time:", datetime.now().timestamp() - self.start_time)
            prev_time = last_calc_time
            if (self.start_time > prev_time):
                prev_time = self.start_time
            return (time_now - prev_time) / self.time_fac * self.cost
        else:
            return 0

class WebService:
    def __init__(self):
        self.machines = []
        self.last_calc_time = 0
        self.accumulated_cost = 0
    def add_machine(self, machine: Machine):
        self.machines.append(machine)
    def remove_machine(self, machine: Machine):
        if machine in self.machines:
            self.machines.remove(machine)
    def calc_cost(self):
        cost = 0
        time_now = int(datetime.now().timestamp())
        for d in self.machines:
            cost += d.get_cost_iteration(self.last_calc_time, time_now)
        self.last_calc_time = time_now
        self.accumulated_cost += cost
        return cost
    def reset_cost(self):
        self.accumulated_cost = 0



#-----------------------------------------------------------------------------------------

if __name__ == '__main__':

    service = WebService()
    sleep_time = 10 # change to 60 if you want minutes and not seconds...

# state 1 (time = 0)
    machine1 = Machine(1, sleep_time)
    machine2 = Machine(1, sleep_time)
    machine3 = Machine(1, sleep_time)
    machine4 = Machine(2, sleep_time)
    machine1.start()
    machine2.start()
    machine3.start()
    machine4.start()
    service.add_machine(machine1)
    service.add_machine(machine2)
    service.add_machine(machine3)
    service.add_machine(machine4)
    print("state 1")
    print("Cost:", service.calc_cost())
    time.sleep(sleep_time)

# state 2 (time = 1)
    machine5 = Machine(2, sleep_time)
    machine5.start()
    service.add_machine(machine5)
    print("state 2")
    print("Cost:", service.calc_cost())
    time.sleep(sleep_time)

# state 3 (time = 2)
    print("state 3")
    print("Cost:", service.calc_cost())
    machine2.end()
    time.sleep(sleep_time)

# state 4 (time = 3) - get current cost
    print("state 4")
    print("Cost:", service.calc_cost())

    print("accumulated cost until now:", service.accumulated_cost)
