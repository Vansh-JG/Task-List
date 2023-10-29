from task import Task
class Tasklist:
    def __init__(self):
        self.tasklist = []
        file = open('tasklist.txt', 'r')
        for element in file:
            x = element.split(",")
            taskobj = Task(x[0], x[1], x[2])
            self.tasklist.append(taskobj)
            self.tasklist.sort(key=lambda task: (task.date, task.time, task.description))
        print()


    def add_task(self, desc, date, time):
        self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort(key=lambda task: (task.date, task.time, task.description))
        return self.tasklist



    def mark_complete(self):
        return self.tasklist.pop(0)


    def save_file(self):
        file = open("tasklist.txt", "w")
        if len(self.tasklist) > 0:
            for i in self.tasklist:
                file.write(Task.__repr__(i))
        file.close()


    def __getitem__(self, index):
        return self.tasklist[index]


    def __len__(self):
        return len(self.tasklist)





