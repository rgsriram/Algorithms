__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Time Conversion
"""


def time_converter(hours, period):
    if period is 'PM':
        if hours == 12:
            return hours
        return hours + 12
    elif period is 'AM':
        return "0%s" % (hours % 12)


def main():
    time = raw_input().strip().upper().split(':')
    (hours, rest) = time[0], time[1:]
    rest = ':'.join(rest)
    period = 'AM' if 'AM' in rest else 'PM'
    hours = time_converter(int(hours), period)
    rest = rest.replace("AM", '').replace("PM", '')
    print "%s:%s" % (hours, rest)


if __name__ == '__main__':
    main()
