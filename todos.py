import json
import time

class TodoList:
    def __init__(self):
        try:
            with open("todos.json", 'r') as file:
                json_data = file.read()
                self.data = json.loads(json_data)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def add(self):
        title = input("enter task title: ")
        if not title:
            print("empty title is invalid!")
            time.sleep(3)
            return
        try:
            completion = int(input("press 0 for 'not completed' and 1 for 'completed': "))

            if completion not in (0, 1):
                print("invalid status!")
                time.sleep(3)
                return

            # this will find the last todo and increment the id 
            if self.data:
                todo_id = self.data[-1]["ID"] + 1
            else:
                todo_id = 0

            temp = {'ID': todo_id, 'title': title, "completion": 'completed' if completion else 'not completed'}
            self.data.append(temp)

            # this will dump the datas into json files
            self.__dump_tasks()

            print("Successful!")
            time.sleep(3)
        except ValueError:
            print("invalid status!")
            time.sleep(3)
            return

    def view(self):
        if not self.data:
            print("empty todo list")
        else:
            print("ID       title                   completion")
            print("__       _____                   __________")

            for task in self.data:
                print(task["ID"], "      " , task["title"], "          ", task["completion"])
            
        time.sleep(5)

    def update(self, updating):
        # finds the index 
        index = self.__find_index()
        
        if index != -1:
            if updating == 1:
                new_title = input("enter the new title: ")
                if not new_title:
                    print("empty title is invalid!")
                    time.sleep(3)
                    return
                self.data[index]["title"] = new_title

            else:
                try:
                    completion_status = int(input("press 0 for 'not completed' and 1 for 'completed': "))
                    if completion_status not in (0, 1):
                        print("invalid status!")
                        time.sleep(3)
                        return 

                    self.data[index]["completion"] = "completed" if completion_status else "not completed"
                except ValueError:
                    print("invalid status!")
                    time.sleep(3)
                    return
            print("Successful!")
        
        else:
            print("invalid ID")            

        # this will dump the datas into json file
        self.__dump_tasks()
        time.sleep(3)

    def delete(self):
        index = self.__find_index()

        if index > -1:
            self.data.pop(index)
            print("Successful!")
        else:
            print("invalid input")

        self.__dump_tasks()
        time.sleep(3)

    # find indexs
    def __find_index(self):
        try:
            todo_id = int(input("enter the ID: "))
        except ValueError:
            return -1
        index = -1

        for i in range(len(self.data)):
            if self.data[i]["ID"] == todo_id:
                index = i
                break
        return index
    
    # dump the data to a file
    def __dump_tasks(self):
        with open("todos.json", "w") as file:
            json.dump(self.data, file, indent=2)

todo = TodoList()

isRunning = True

while isRunning:
    print("press 1 to add Todo ")
    print("press 2 to view Todo ")
    print("press 3 to update Todo ")
    print("press 4 to delete Todo ")
    print("press 5 to stop the program")

    choice = input('choice: ')

    match choice:
        case '1':
            todo.add()

        case '2':
            todo.view()

        case '3':
            print("press 1 for title")
            print("press 2 for completion status: ")

            try:
                updating = int(input("choice: "))

                if updating in (1, 2):
                    todo.update(updating)
                else:
                    raise ValueError
                
            except ValueError as e:
                print("input must be 1 or 2")

        case '4':
            todo.delete()
        case '5':
            isRunning = False
        case _:
            print("invalid input")