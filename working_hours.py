from datetime import time


class Client:

    def __init__(self, name):
        self.__name = name
        self.__shifts = []
        self.shift = self.Shift

    def new_shift(self, day, start, end):
        self.__shifts.append(self.Shift(day, start, end))

    def __str__(self):
        ret = "Name: " + self.__name + "\nShifts:\n"
        for s in self.__shifts:
            ret += s.__str__()
        return ret

    class Shift:

        # The method initializes a new Shift object
        # The date (datetime), starting and ending time (string)
        # are given as parameters
        def __init__(self, day, start, end):
            assert 0 <= int(start[0:2]) <= 23, "Not valid starting hour!"
            assert 0 <= int(end[0:2]) <= 23, "Not valid ending hour!"
            assert 0 <= int(start[3:5]) <= 59, "Not valid starting minutes!"
            assert 0 <= int(end[3:5]) <= 59, "Not valid ending minutes!"
            assert time.fromisoformat(start) < time.fromisoformat(end), "Starting time has to be before ending time"
            assert ((int(end[0:2]) * 60 + int(end[3:5])) - (int(start[0:2]) * 60 + int(start[3:5]))) <= 16*60, \
                "Too long shift"
            self.__date = day
            self.__start = time.fromisoformat(start)
            self.__end = time.fromisoformat(end)

        def get_start_minutes(self):
            return self.__start.hour * 60 + self.__start.minute

        def get_end_minutes(self):
            return self.__end.hour * 60 + self.__end.minute

        # The method returns the hours (in decimal) of this shift
        def get_hours(self):
            return (self.get_end_minutes() - self.get_start_minutes()) / 60.0

        # The method returns a string representation of the information
        # of the shift
        def __str__(self):
            info = "Date: {} \n".format(self.__date)
            info += "Time: {} - {}\n".format(self.__start, self.__end)
            info += "Hours worked: {:.2f}\n".format(self.get_hours())
            return info
