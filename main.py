# main.py
from States.Missouri import Missouri
from States.NewYork import NewYork


Missouri = Missouri("St.louis", "Geospatial")

NewYork = NewYork("Time Square", "")


print(Missouri.get_info())
print(NewYork.get_info())

