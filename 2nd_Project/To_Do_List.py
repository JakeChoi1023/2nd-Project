list = []
completed_list = []


while True:

    task = input('''
    exit      = quit
    delete    = remove list
    type task = add list 
    complete  = mark as complete
    show      = display current list
    Type your command: ''')
    if task == "exit":
        break
    elif task == "delete":
        remove = input('Which task? ')
        try:
            list.remove(remove)
            print(remove, 'is deleted from the list \n')
            print('- Current List -')
            for el in list:
             print(el)
            continue
        except:
            print('error')
            continue
    elif task == "complete":
        complete = input('Which task? ')
        try:
            list.remove(complete)
            completed_list.append(complete)
            for el in list:
                    print(el)
        except:
            print('error')
            continue
    elif task == "show":
        print('- Current List -')
        for el in list:
            print(el)
        print()
        print('- Completed list -')
        for el2 in completed_list:
                print(el2)
    else:
        list.append(task)
        for el in list:
            print(el)
        continue
