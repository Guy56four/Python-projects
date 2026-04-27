tasks  =  ['Buy groceries','Call mom', 'learn python']
def add_task (tasks,task):
    tasks.append(task)
    print(f'Task added: {task}')

def view_tasks (tasks):
    for i, task in  enumerate(tasks, 1):
        print(f'{i}.{task}')

def delete_tasks(tasks,number):
    if number  < 1 or number > len(tasks):
        print('Invalid number!')
        
    else:
        removed = tasks.pop(number -1)
        print(f'"{removed}" deleted')
        

while True:
    print('\nTo-do list')
    print('1. Add task')
    print('2. View tasks') 
    print('3. Delete task')
    print('4. Exit')

    Choise = input ('Choise option:')

    if Choise == '1':
        task = input ('Enter task:')
        add_task(tasks, task)
    elif Choise =='2':
        view_tasks(tasks)
    
    elif Choise =='3':
            number = int (input('Which task to delete:'))
            delete_tasks(tasks, number)
    elif Choise =='4':
        break
