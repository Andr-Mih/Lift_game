import random

def start_game():
    travel_list = []
    n = random.randint(5,21)
    for i in range(0,n+1,1):
        flow_list =[]
        k = random.randint(1,11)
        for i in range(0, k,  1):
            flow_list.append(random.randint(1,n))
        travel_list.append(flow_list)
    lift = [-1, -1, -1 ,-1, -1]

    return n, lift, travel_list

def start_lift(lift, travel_list):
    for i in range(0,5):
        if lift[i] == -1:
            if len(travel_list[0]) >= 1:
                lift[i] = travel_list[0][0]
                del travel_list[0][0]
            else:
                break
    return lift, travel_list


def exit_lift(flow, lift, travel_list):
    for i in range(5):
        if lift[i] == -1:
            if len(travel_list[flow]) >= 1:
                lift[i] = travel_list[flow][0]
                del travel_list[flow][0]
            else :
                break
        if lift[i]== flow:
            lift[i] = -1
            k = random.randint(0,len(travel_list)-1)
            travel_list[flow].append(k)
                
    return lift, travel_list

def line_floor_up(flow, travel_list):
    line =[]
    for fl in travel_list[flow]:
        if fl > flow:
            line.append(fl) 
    return line

def line_floor_down(flow, travel_list):
    line =[]
    for fl in travel_list[flow]:
        if fl < flow:
            line.append(fl) 
    return line


def enter_lift(func, flow, lift, travel_list):
    a = func(flow, travel_list)
    for i in range(0,5):
        if lift[i] == -1:
            if len(a) >=1:
                lift[i] = a[0]
                travel_list[flow].remove(a[0])
                del a[0]
                
            #else:
               # break
                    #k +=1

    return lift, travel_list
    

def plot(flow, lift, travel_list):
    #print(f'Current flow: {flow}')
    print('{:^12}'.format('lift'),'|' '{:^12}'.format('floor line'))
    print(f'| {lift[0]} {lift[1]} {lift[2]} {lift[3]} {lift[4]} |{travel_list[flow]}')

def plot_flow(flow, direction):
    print('{:*^30}'.format(direction))
    print(f'Current flow :{flow}')

def move(func_1, func_2, func_3, *args):
    #print('Passengers exit from lift :')
    func_1(*args)
    plot(*args)
    #print('Passengers enter in lift :')
    func_2(func_3,*args)
    plot(*args)

def main():
    game = start_game()
    n = game[0]
    lift = game[1]
    travel_list = game[2]
    print(n, travel_list)
    current_flow = 0
    start_lift(lift, travel_list)
    print(lift)
    while True:
        if max(lift) > current_flow:
            current_flow +=1
            plot_flow(current_flow,'Lift move UP')
            move(exit_lift, enter_lift, line_floor_up, current_flow, lift, travel_list)
            inp = input('Press any key to move the next floor or "exit": ')
            if inp == 'exit':
                break
        if max(lift) < current_flow or current_flow == n:
            current_flow -=1
            plot_flow(current_flow,'Lift move DOWN')
            move(exit_lift, enter_lift, line_floor_down, current_flow, lift, travel_list)
            inp = input('Press any key to move the next floor or "exit": ')
            if inp == 'exit':
                break
        if max(lift) == current_flow:
            current_flow +=1
    




if __name__ == '__main__':
    main()