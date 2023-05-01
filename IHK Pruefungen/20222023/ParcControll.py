import datetime 
import calendar

class Datum:
    def __init__(self, Date:str) :
        self.Datum = datetime.datetime.strptime(Date, '%Y-%m-%d %H:%M')

    def getDay(self):
        return self.Datum.strftime("%d")
    
    def getHour(self):
        return self.Datum.strftime("%H")

    def getDaysOfMonth(self):
        jahr = (int)(self.Datum.strftime("%Y"))
        monat = (int)(self.Datum.strftime("%m"))
        return calendar.monthrange(jahr, monat)[1]
        

class ComLeave(object):
    def __init__(self, datum:Datum, cio:int, no:int):
        self.Date = datum
        self.comeInOut = cio
        self.noPeople = no

    def getDate(self):
        return self.Date

    def getComeInOut(self):
        return self.comeInOut
    
    def getNoPeople(self):
        return self.noPeople    
    

d1 = Datum("2023-05-23 09:00")
d2 = Datum("2023-05-23 09:00")
d3 = Datum("2023-05-23 09:01")
d4 = Datum("2023-05-23 12:00")
d5 = Datum("2023-05-23 12:01")
d6 = Datum("2023-05-23 12:02")

a = ComLeave(d1, 0, 1)
b = ComLeave(d2, 0, 2)
c = ComLeave(d3, 0, 30)
d = ComLeave(d4, 1, 1)
e = ComLeave(d5, 0, 2)
f = ComLeave(d6, 1, 1)


#Sort of Array from ComLeave-Objects named 
comLeaves = []
comLeaves.append(a)
comLeaves.append(b)
comLeaves.append(c)
comLeaves.append(d)
comLeaves.append(e)
comLeaves.append(f)

def countLeaves(entry:ComLeave):
    countEntry = len(entry)
    rows = 31 #int(input())
    cols = 10 #int(input())
    visitors = []

    #Faking two dim-Array in Python
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(0)
        visitors.append(row)    
    
    #FEHLER: Nicht -1 bei countEntry, zweiter Parameter ist exklusive
    for i in range(0, countEntry):
        day = entry[i].getDate().getDay()
        hour = entry[i].getDate().getHour()
        index_row = (int)(day) - 1 
        index_column = (int)(hour) - 9

        if entry[i].getComeInOut() == 0:
            #FEHLER: muss bis 10 sein, weil 9 exklusiver Parameter 
            for j in range(index_column, 10): #läuft immer vom Eintrittsuhrtzeit nach vorne
                #[index_row] = Day, [j]=Hour
                visitors[index_row][j] = visitors[index_row][j] + entry[i].getNoPeople()
                print("Aktuell im Park: " + str(visitors[index_row][j]) + " - Plus(inklusiv bereits): " +   str(entry[i].getNoPeople()))

        else:
            for j in range((index_column + 1),10):
                #FEHLER: Müssten dies hier nicht - entry[i].getNoPeople() sein
                visitors[index_row][j] = visitors[index_row][j] -  entry[i].getNoPeople()
                print("Im nächsten Zeitabschnitt im Park: " + str(visitors[index_row][j]) + " - Minus(inklusiv bereits): " +   str(entry[i].getNoPeople()))
                #VORHERIGE LÖSUNG: visitors[index_row][j] = visitors[index_row][j] - 1  
    return visitors

result = countLeaves(comLeaves)
print(result)
