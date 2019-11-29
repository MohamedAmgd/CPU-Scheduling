from Process import process
from collections import OrderedDict


'''
Iterate over all the key value pairs in dictionary and call the given
callback function() on each pair. Items for which callback() returns True,
add them to the new dictionary. In the end return the new dictionary.
'''


def filterTheDict(dic, time):
    newDict = dict()
    # Iterate over all the items in dictionary and filter items which has even keys
    for (key, value) in dic.items():
        # Check if key is even then add pair to new dictionary
        if value.getArrival() <= time:
            newDict[key] = value
    return newDict


def filterFinshedProcesses(dic):
    newDict = dict()
    # Iterate over all the items in dictionary and filter items which has even keys
    for (key, value) in dic.items():
        # Check if key is even then add pair to new dictionary
        if value.getRemaining() > 0:
            newDict[key] = value
    return newDict


def avgTurnAround(dic):
    sum = 0
    for i in dic:
        sum += dic[i].getTurnaround()
    return sum / len(dic)


def avgWaiting(dic):
    sum = 0
    for i in dic:
        sum += dic[i].getWaiting()
    return sum / len(dic)


def printAlgo(dic):
    for i in dic:
        print("{0}: arrival = {1} brust = {2}  w = {3} t = {4}".format(i, dic[i].getArrival(), dic[i].getBrust(),
                                                                       dic[i].getWaiting(), dic[i].getTurnaround()))
    print("avg Waiting = {0} , avg Turn Around = {1}".format(
        avgWaiting(dic), avgTurnAround(dic)))


def FCFS(processes_dic):
    time = processes_dic[next(iter(processes_dic))].getArrival()
    for i in processes_dic:
        if (processes_dic[i].getArrival() > time):
            time = processes_dic[i].getArrival()
        processes_dic[i].setWaiting(time - processes_dic[i].getArrival())
        time += processes_dic[i].getBrust()
    for i in processes_dic:
        processes_dic[i].setTurnaround(
            processes_dic[i].getBrust() + processes_dic[i].getWaiting())
    return processes_dic


def SJF(processes_dic):
    time = processes_dic[next(iter(processes_dic))].getArrival()
    remaing_processes = dict(processes_dic)
    while len(remaing_processes) > 0:
        first_key = next(iter(remaing_processes))
        if (remaing_processes[first_key].getArrival() > time):
            time = remaing_processes[first_key].getArrival()
        waiting_dic = OrderedDict(
            sorted(filterTheDict(remaing_processes, time).items(), key=lambda x: x[1].getBrust()))
        min_brust = next(iter(waiting_dic))
        processes_dic[min_brust].setWaiting(
            time - processes_dic[min_brust].getArrival())
        time += processes_dic[min_brust].getBrust()
        remaing_processes.pop(min_brust)
    for i in processes_dic:
        processes_dic[i].setTurnaround(
            processes_dic[i].getBrust() + processes_dic[i].getWaiting())

    return processes_dic


def SRTF(processes_dic):
    time = processes_dic[next(iter(processes_dic))].getArrival()
    remaining_processes = dict(processes_dic)
    while len(remaining_processes) > 0:
        first_key = next(iter(remaining_processes))
        if (remaining_processes[first_key].getArrival() > time):
            time = remaining_processes[first_key].getArrival()
        waiting_dic = OrderedDict(
            sorted(filterTheDict(remaining_processes, time).items(), key=lambda x: x[1].getRemaining()))
        min_remaining = next(iter(waiting_dic))
        processes_dic[min_remaining].setRemaining(
            processes_dic[min_remaining].getRemaining() - 1)
        time += 1
        if processes_dic[min_remaining].getRemaining() == 0:
            remaining_processes.pop(min_remaining)
            processes_dic[min_remaining].setExitTime(time)
    for i in processes_dic:
        processes_dic[i].setTurnaround(
            processes_dic[i].getExitTime() - processes_dic[i].getArrival())
        processes_dic[i].setWaiting(
            processes_dic[i].getTurnaround() - processes_dic[i].getBrust())
    return processes_dic


def RR(processes_dic, q):
    time = processes_dic[next(iter(processes_dic))].getArrival()
    remaining_processes = dict(processes_dic)
    waiting_dic = OrderedDict()
    while len(remaining_processes) > 0:
        waiting_dic = OrderedDict(
            sorted(filterTheDict(remaining_processes, time).items(), key=lambda x: x[1].getWaitingArrival()))
        if len(waiting_dic) == 0:
            time = remaining_processes[next(
                iter(remaining_processes))].getArrival()
            continue
        current_process_key = next(iter(waiting_dic))
        current_process_value = waiting_dic[current_process_key]
        if current_process_value.getRemaining() > q:
            time += q
            current_process_value.setRemaining(
                current_process_value.getRemaining() - q)
            current_process_value.setWaitingArrival(time+0.5)
            remaining_processes[current_process_key] = current_process_value
        else:
            new_q = current_process_value.getRemaining()
            time += new_q
            current_process_value.setRemaining(0)
            remaining_processes.pop(current_process_key)
            processes_dic[current_process_key].setExitTime(time)
    for i in processes_dic:
        processes_dic[i].setTurnaround(
            processes_dic[i].getExitTime() - processes_dic[i].getArrival())
        processes_dic[i].setWaiting(
            processes_dic[i].getTurnaround() - processes_dic[i].getBrust())

    return processes_dic


'''
def RR(processes_dic, q):
    time = 0
    remaing_processes = dict(processes_dic)
    while len(remaing_processes) > 0:
        remaing_processes = OrderedDict(
            sorted(remaing_processes.items(), key=lambda x: x[1].getArrival()))
        current_process_key = next(iter(remaing_processes))
        remaing_processes[current_process_key].setRemaining(
            remaing_processes[current_process_key].getRemaining() - q)
        current_process_value = remaing_processes[current_process_key]
        remaing_processes.pop(current_process_key)
        waiting_dic = filterTheDict(remaing_processes, time)
        for i in waiting_dic:
            processes_dic[i].setWaiting(processes_dic[i].getWaiting() + q)
        time += q
        if current_process_value.getRemaining() > 0:
            current_process_value.setArrival(time)
            remaing_processes[current_process_key] = current_process_value
        else:
            time += current_process_value.getRemaining()
            for i in waiting_dic:
                processes_dic[i].setWaiting(
                    processes_dic[i].getWaiting() + current_process_value.getRemaining())
    for i in processes_dic:
        processes_dic[i].setTurnaround(
            processes_dic[i].getBrust() + processes_dic[i].getWaiting())
    return processes_dic
'''


def start():
    while True:
        print("Menu:")
        print("1) FCFS ")
        print("2) SJF ")
        print("3) SRTF ")
        print("4) RR ")
        print("5) all of them")
        print("0) quit ")
        choice = ""
        while not isinstance(choice, int):
            choice = input("enter your choice:")
            try:
                choice = int(choice)
                if choice < 0 or choice > 5:
                    choice = ""
            except:
                choice = ""
        if choice == 0:
            break
        input_FCFS = dict()
        input_SJF = dict()
        input_SRTF = dict()
        input_RR = dict()
        num = ""
        while not isinstance(num, int):
            num = input("enter the number of processes :")
            try:
                num = int(num)
                if num <= 0:
                    num = ""
            except:
                num = ""
        for i in range(int(num)):
            arrival = ""
            brust = ""
            while not isinstance(arrival, int):
                arrival = input(
                    "enter process {0} (P{0}) arrival time:".format(i+1))
                try:
                    arrival = int(arrival)
                    if arrival < 0:
                        arrival = ""
                except:
                    arrival = ""
            while not isinstance(brust, int):
                brust = input(
                    "enter process {0} (P{0}) brust time:".format(i+1))
                try:
                    brust = int(brust)
                    if brust <= 0:
                        brust = ""
                except:
                    brust = ""
            input_FCFS["P" + str(i+1)] = process(int(arrival), int(brust))
            input_SJF["P" + str(i+1)] = process(int(arrival), int(brust))
            input_SRTF["P" + str(i+1)] = process(int(arrival), int(brust))
            input_RR["P" + str(i+1)] = process(int(arrival), int(brust))
        if choice == 1:
            print("FCFS :")
            printAlgo(
                FCFS(dict(sorted(input_FCFS.items(), key=lambda x: x[1].getArrival()))))
        elif choice == 2:
            print("SJF :")
            printAlgo(
                SJF(dict(sorted(input_SJF.items(), key=lambda x: x[1].getArrival()))))
        elif choice == 3:
            print("SRTF :")
            printAlgo(
                SRTF(dict(sorted(input_SRTF.items(), key=lambda x: x[1].getArrival()))))
        elif choice == 4:
            q = ""
            while not isinstance(q, int):
                q = input("enter Q :")
                try:
                    q = int(q)
                    if q <= 0:
                        q = ""
                except:
                    q = ""
            print("RR , Q = {0}:".format(q))
            printAlgo(
                RR(dict(sorted(input_RR.items(), key=lambda x: x[1].getArrival())), q))
        elif choice == 5:
            q = ""
            while not isinstance(q, int):
                q = input("enter Q for RR :")
                try:
                    q = int(q)
                    if q <= 0:
                        q = ""
                except:
                    q = ""
            print("FCFS :")
            printAlgo(
                FCFS(dict(sorted(input_FCFS.items(), key=lambda x: x[1].getArrival()))))
            print("SJF :")
            printAlgo(
                SJF(dict(sorted(input_SJF.items(), key=lambda x: x[1].getArrival()))))
            print("SRTF :")
            printAlgo(
                SRTF(dict(sorted(input_SRTF.items(), key=lambda x: x[1].getArrival()))))
            print("RR , Q = {0}:".format(q))
            printAlgo(
                RR(dict(sorted(input_RR.items(), key=lambda x: x[1].getArrival())), q))


start()