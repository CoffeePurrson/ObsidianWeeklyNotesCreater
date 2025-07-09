import datetime

def main():
    createFiles()


## Logik zum Erstellen der Markdown Files:
def createFiles():
    createDays()
    createCalenderweek()

def createDays():
    week = getListOfCurrentWeek()
    for i in range(len(week)):
        _ = open(week[i] + ".md", "x")

def createCalenderweek():
    week = getListOfCurrentWeek()
    weekFile = open(f"{getNumberOfCurrentWeek()}. Kalenderwoche.md", "w")
    for i in range(len(week)):
        weekFile.write(f"![[{week[i]}]]")
    weekFile.write("\n# Wochenaufgaben\n![[Offene Aufgaben]]")


# Logik zum Bekommen der Wochendaten:
def getListOfCurrentWeek():
    weekdays = []
    for i in range(7):
        day = getSpecificDayOfCurrentWeek(i+1)
        weekdays.append(parseDayFormat(day))
    return weekdays

def parseDayFormat(day):
    parsedDay = day.strftime("%d.%m.%Y")
    return parsedDay

def getSpecificDayOfCurrentWeek(numberOfDay):
    day = datetime.date.fromisocalendar(getNumberOfCurrentYear(), getNumberOfCurrentWeek(), numberOfDay)
    return day

def getNumberOfCurrentWeek():
    currentCalendarWeek = getCurrentDay().isocalendar().week
    return currentCalendarWeek

def getNumberOfCurrentYear():
    currentCalendarYear = getCurrentDay().isocalendar().year
    return currentCalendarYear

def getCurrentDay():
    today = datetime.date.today()
    return today


if __name__ == "__main__":
    main()