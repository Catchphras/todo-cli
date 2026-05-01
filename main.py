from pathlib import Path
import json


contents = {}
l = []
completed_tasks = []

path = Path('tasks.json')
completed_tasks_path = Path('completed_tasks.json')

def json_loader():
    """Responsible for loading tasks stored in the tasks.json file"""
    raw_json = path.read_text()
    processed_json = json.loads(raw_json)
    return processed_json

def completed_tasks_json_loader():
    """Responsible for loading completed tasks stored in the completed_tasks.json file"""
    raw_json = completed_tasks_path.read_text()
    processed_json = json.loads(raw_json)
    return processed_json

def add_task():
    '''Adds tasks'''
    path = Path('tasks.json')
    if path.exists() == True:
        task = input("\nEnter the task: ")  #takes the user defined task and assigns it to the variable task

        processed_json = json_loader()

        for second_dict in processed_json.values():
            for l in second_dict.values():
                if task in l:
                    print("Task already exists or has been typed before.")
                else:
                    l.append(task)   # it then appends the task to a list called storage
                    print("Task added successfully")
    
    else:
        l = []
        path = Path('tasks.json')
        task = input("\nEnter the task: ")
        l.append(task)
        contents['tasks'] = l
        second_dict = contents

    return second_dict


def remove_task():
    '''Removes specified tasks'''
    task_to_remove = input("\nWhich task do you want to remove:(use the number attached to the task): ")
    
    processed_json = json_loader()

    for second_dict in processed_json.values():
        for l in second_dict.values():
                task_to_remove = int(task_to_remove)
                l=list(l)
                x = l.pop(task_to_remove)
                print(f"Task: '{x.title()}' with number: '{task_to_remove}' has been removed.")
                l_ist = l
                second_dict={'tasks':l_ist}  
                  
                
    return second_dict



def view_tasks():
    '''Views the stored tasks'''
    processed_json = json_loader()
    
    print("\nViewing tasks...")
    for second_dict in processed_json.values():
        for l in second_dict.values():
            for t in l:
                print(f"{l.index(t)}. {t.title()}")


def save_tasks():
    '''Saves tasks to a file'''
    # dict_to_save = second_dict
    dict_to_save = {'json_file': second_dict}
    content = json.dumps(dict_to_save)
    content = path.write_text(content)
    print("\nFile and tasks saved successfully.")


def mark_as_complete():
    """Marks a task as complete"""
    completed_task = input("\nMark which task as complete(Use the number attached to the task): ")
    # completed_task = completed_task.lower().strip()
    
    processed_json = json_loader()
    for second_dict in processed_json.values():
        for l in second_dict.values():
                completed_task = int(completed_task)
                l=list(l)
                x = l.pop(completed_task)
                completed_tasks.append(x)
                l_ist = l
                second_dict={'tasks':l_ist}
                print(f"{x.title()}: Marked as complete.")
       
    return second_dict,completed_tasks

def save_marked_as_complete():
    """Saves the tasks which are marked as completed"""
    dict_to_save = {'json_for_completed_tasks': completed_tasks}
    content = json.dumps(dict_to_save)
    content = completed_tasks_path.write_text(content)
    print("\nFile and tasks saved successfully.")



def view_completed_tasks():
    """Shows completed tasks"""
    print("\nViewing completed tasks...")

    processed_json = completed_tasks_json_loader()   
    for completed_tasks in processed_json.values():
        if completed_tasks==[]:
            print(f"\nThere are no completed tasks.")
        else:
            print()
            for completed_task in completed_tasks:
                print(f"{completed_tasks.index(completed_task)}. {completed_task.title()}")



while True:
    message = "\n1. Add task\n2. View tasks\n3. Remove task\n4. Mark a task as complete\n5. View completed tasks\n(Enter 'q' to quit)"
    response= input(f"\nEnter the number of an option you want.\n{message}\t:")
    if response.lower() == 'q':
        print("Quitting...")
        break
    if response == '1':
        second_dict = add_task()
        answer = input("Save the task(s) or changes made?(y/n): ")
        if answer.lower() == 'y':
            save_tasks()
                        
        if answer.lower() == 'n':
            print('Task(s) was not saved.')

    elif response == '2':
        view_tasks()
    elif response == '3':
        second_dict = remove_task()
        answer = input('Save changes?(y/n): ')
        if answer.lower() == 'y':
            save_tasks()
                        
        if answer.lower() == 'n':
            print('Changes were not saved.')
    elif response == '4':
       second_dict,completed_tasks = mark_as_complete()
       answer = input('Save changes?(y/n): ')
       if answer.lower() == 'y':
            save_tasks()
            save_marked_as_complete()
                        
       if answer.lower() == 'n':
            print('Changes were not saved.') 
    elif response == '5':
        view_completed_tasks()
    else:
        print("\nERROR: Please enter a valid option(1,2,3,4,5,q)")