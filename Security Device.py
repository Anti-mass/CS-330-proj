import random
import time


def lock_mechanism(entry):
    unlock = [6,0,8,0,4,1]
    lock =   [6,0,8,0,4,4]
        
    if entry[-1] == 1:
        for i in range(5):
            if entry[i] != unlock[i]:
                return False
        print("unlocked")
        return True

    if entry[-1] == 4:
        for i in range(5):
            if entry[i] != lock[i]:
                return False
        print("locked")
        return False
     

def lock_interactive():
    first_input = input('Please enter the first value of the passcode\n')
    input_buffer = []
    try:
        if isinstance(int(first_input[0]), int):
            input_buffer.append(int(first_input[0]))
    except ValueError:
        pass

    while(True):
        try:
            if len(input_buffer) > 5:
                lock_mechanism(input_buffer[-6:])
            num = input("Enter next value: ")
            if num == 'quit':
                print('Interactive closed')
                break
            if  isinstance(int(num[0]), int):
                input_buffer.append(int(num[0]))
        except ValueError:
            continue


def rand_lock_test():
    rand = random.randint(0,9)
    input_buffer = []
    lock_status = False
    time.perf_counter()
    inputs = 5
    while(True):
        input_buffer.append(rand)
        if len(input_buffer) > 5:
            lock_status = lock_mechanism(input_buffer[-6:])
            inputs += 1
            if lock_status:
                
                print("lock cracked in: "+ '{:,}'.format(round(time.perf_counter())) + ' seconds and took '+  '{:,}'.format(inputs) +' inputs' )
                break
        rand = random.randint(0,9)


def rand_lock_test_average(runs):
    rand = random.randint(0,9)
    input_buffer = []
    lock_status = False
    time.perf_counter()
    attempts = 0
    average_runtime = 0
    runtime = 0
    for i in range(runs):    
        while(True):
            input_buffer.append(rand)
            if len(input_buffer) > 5:
                lock_status = lock_mechanism(input_buffer[-6:])
                attempts += 1
                if lock_status:
                    
                    runtime = round(time.perf_counter()) + attempts
                    print("lock cracked in: "+ '{:,}'.format(runtime) + ' seconds and took '+  '{:,}'.format(attempts) +' attempts' )
                    break
            rand = random.randint(0,9)
        average_runtime += runtime
    print('Average runtime: '+ '{:,}'.format(average_runtime//runs)+' seconds')

while(True):
    choice = input("Please enter an option: \n"+
    "1: Interactive lock simulation\n"+ 
    "2: Test time to crack lock once using random inputs\n"+
    "3: Test Average time to crack over a given number of runs\n"+   
    "quit: to quit the application\n")
    try:
        if choice.lower() == 'quit':
            print('closing application')
            break
        elif int(choice[0]) == 1:
            lock_interactive()
        elif int(choice[0]) == 2:
            rand_lock_test()
        elif int(choice[0]) == 3:
            runs = input("How many instances would you like to test?\n")     
            rand_lock_test_average(int(runs))
        else:
            print("!! Please Enter A Valid Input !!")
    except ValueError:
        print("!!! Please Enter A Valid Input !!!")

