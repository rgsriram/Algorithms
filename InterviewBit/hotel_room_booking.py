class Interval(object):
    def __init__(self, st, end):
        self.start = st
        self.end = end


def hotel(arraivals, depatures, no_of_rooms):
    intervals = []

    for i in range(len(arraivals)):
        intervals.append(Interval(arraivals[i], depatures[i]))

    intervals = sorted(intervals, key=lambda interval: interval.start)

    for each in intervals:
        print each.start, each.end


    no_of_rooms_available = 0

    for i in range(1, len(intervals)-1):


        while j < i:

            if intervals[j].end > intervals[i].start:
                # print intervals[j].start, intervals[j].end, intervals[i].start, intervals[i].end
                no_of_rooms -= 1
                # print no_of_rooms
                break

            j += 1

        if not no_of_rooms:
            return False

    return True



def hotel_booking(arraivals, depatures, no_of_rooms):
    intervals = []

    for i in range(len(arraivals)):
        intervals.append(Interval(arraivals[i], depatures[i]))

    intervals = sorted(intervals, key=lambda interval: interval.start)

    days = [0] * (max(depatures) + 1)

    for interval in intervals:

        for i in range(interval.start, interval.end):
            days[i] += 1

            if days[i] > no_of_rooms:
                return False

    return True


A = [9, 47, 17, 39, 35, 35, 20, 18, 15, 34, 11, 2, 45, 46, 15, 33, 47, 47, 10, 11, 27 ]
B = [32, 82, 39, 86, 81, 58, 64, 53, 40, 76, 40, 46, 63, 88, 56, 52, 50, 72, 22, 19, 38 ]

A = [ 1, 2, 3, 4 ]
B = [ 10, 2, 6, 14 ]

print hotel_booking(A, B, 2)
