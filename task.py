class Task:

    def __init__(self, desc, date, time):
        self.description = desc
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.description} - Due: {self.date} at {self.time}"

    def __lt__(self, other):
        date1 = self.date.split("/")
        time1 = self.time.split(":")
        date2 = other.date.split("/")
        time2 = other.time.split(":")
        year1, month1, day1 = int(date1[2]), int(date1[0]), int(date1[1])
        year2, month2, day2 = int(date2[2]), int(date2[0]), int(date2[1])
        hour1, minute1 = int(time1[0]), int(time1[1])
        hour2, minute2 = int(time2[0]), int(time2[1])
        if year1 < year2:
            return True
        elif year1 > year2:
            return False
        else:
            if month1 < month2:
                return True
            elif month1 > month2:
                return False
            else:
                if day1 < day2:
                    return True
                elif day1 > day2:
                    return False
                else:
                    if hour1 < hour2:
                        return True
                    elif hour1 > hour2:
                        return False
                    else:
                        if minute1 < minute2:
                            return True
                        elif minute1 > minute2:
                            return False
                        else:
                            self.description.lower()
                            other.description.lower()
                            return self.description < other.description


    def __repr__(self):
        return self.description + ", " + self.date + ", " + self.time




