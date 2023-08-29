class Degree:
    def count(self):
        h = (((self.hours % 12) + (self.minutes / 60)) / 12) * 360
        m = (self.minutes / 60) * 360
        if h > m:
            x = 360 - h + m
            print(str(x) + "°")
        elif h < m:
            x = m - h
            print(str(x) + "°")
        else:
            print(str(0) + "°")

Deg1 = Degree()
Deg1.hours = 3
Deg1.minutes = 0

Deg2 = Degree()
Deg2.hours = 0
Deg2.minutes = 15

Deg1.count()
Deg2.count()
