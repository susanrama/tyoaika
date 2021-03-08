from working_hours import Client
from datetime import date


def main():
    client1 = Client("Maija")
    client1.new_shift(date(2019,12,4), "08:00", "15:00")
    client1.new_shift(date(2019, 9, 8), "00:15", "10:02")
    #client1.new_shift(date(2019, 9, 7), "00:15", "20:59") #gives assertion error, too long shift
    #client1.new_shift(date(2019, 7, 4), "18:15", "25:02") #not valid time
    #client1.new_shift(date(2019, 6, 5), "10:15", "08:02") #Starting time has to be before ending time
    print(client1)


main()