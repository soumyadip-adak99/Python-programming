class student:
    def __init__(self,name,roll,department):
        self.name = name
        self.roll = roll
        self.department = department

    def getData(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Deparment: {self.department}")


if __name__ == "__main__":
    s = student("Soumya",355,"BCA")
    s.getData()
