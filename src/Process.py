class process:
    waiting = 0
    turn_around = 0
    exit_time = 0

    def __init__(self, arrival, burst):
        self.arrival = arrival
        self.burst = burst
        self.waiting_arrival = arrival
        self.remaining = burst

    def getArrival(self):
        return self.arrival

    def setArrival(self, arrival):
        self.arrival = arrival

    def getBurst(self):
        return self.burst

    def setBurst(self, burst):
        self.burst = burst

    def getWaitingArrival(self):
        return self.waiting_arrival

    def setWaitingArrival(self, waiting_arrival):
        self.waiting_arrival = waiting_arrival

    def getRemaining(self):
        return self.remaining

    def setRemaining(self, remaining):
        self.remaining = remaining

    def getWaiting(self):
        return self.waiting

    def setWaiting(self, waiting):
        self.waiting = waiting

    def getTurnaround(self):
        return self.turn_around

    def setTurnaround(self, turn_around):
        self.turn_around = turn_around

    def getExitTime(self):
        return self.exit_time

    def setExitTime(self, exit_time):
        self.exit_time = exit_time
