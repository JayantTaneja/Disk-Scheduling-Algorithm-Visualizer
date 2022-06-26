#--------------------------------FCFS------------------------------

def fcfs(request, initial_head_pos=53):
    '''
    First Come First Serve Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken=[initial_head_pos]

    for sector in request:
        
        path_taken.append(sector)
        thm += abs(sector-curr_head_pos)

        curr_head_pos = sector

    return thm, path_taken

#--------------------------------SSTF------------------------------

def sstf(request:list, initial_head_pos=53):
    '''
    Shortest Seek Time Forst Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]


    for i in range(len(request)):
        next_sector = min(request, key=lambda x:abs(x-curr_head_pos))
        request.remove(next_sector)
        path_taken.append(next_sector)
        thm+=abs(curr_head_pos-next_sector)

        curr_head_pos = next_sector
    
    return thm, path_taken

#--------------------------------SCAN------------------------------

def rscan(request:list, initial_head_pos=53, disk_size = 200):
    '''
    Right Direction Utility for SCAN Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort()
    smaller.sort(reverse=True)

    # Traverse all the sectors ahead of initial head position
    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    # Travel To Boundary and Change Direction
    next_sector=disk_size-1
    path_taken.append(next_sector)
    thm+=abs(next_sector-curr_head_pos)
    curr_head_pos = next_sector


    # Traverse all the sectors behind initial head position
    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector
    
    return thm, path_taken

def lscan(request:list, initial_head_pos=53, disk_size = 200):
    '''
    Left Direction Utility for SCAN Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort()
    smaller.sort(reverse=True)

    # Traverse all the sectors behind initial head position
    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    # Travel To Boundary and Change Direction
    next_sector=0
    path_taken.append(next_sector)
    thm+=abs(next_sector-curr_head_pos)
    curr_head_pos = next_sector

    # Traverse all the sectors ahead of initial head position
    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector


    
    return thm, path_taken



def scan(request:list, initial_head_pos=53, direction='right', disk_size = 200):
    '''
    SCAN Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - direction : inital traveling direction of head
    - disk_size : Total no of sectors in disk
    '''
    
    if direction.lower()=='right':
        return rscan(request, initial_head_pos, disk_size)

    else:
        return lscan(request, initial_head_pos, disk_size)



#--------------------------------C SCAN----------------------------

def rcscan(request:list, initial_head_pos=53, disk_size = 200):
    '''
    Right Direction Utility for C SCAN Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort()
    smaller.sort()

    if len(greater)!=0:

        # Traverse all the sectors ahead of initial head position
        for sector in greater:
            next_sector = sector
            path_taken.append(next_sector)
            thm+=abs(next_sector-curr_head_pos)
            curr_head_pos = next_sector

        if len(smaller)==0:
            return thm, path_taken

        # Travel To Last Sector

        next_sector=disk_size-1
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    # Travel to Sector 0

    next_sector=0
    path_taken.append(next_sector)
    thm+=abs(next_sector-curr_head_pos)
    curr_head_pos = next_sector

    # Traverse all the sectors behind the initial head position

    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector
    
    return thm, path_taken

def lcscan(request:list, initial_head_pos=53, disk_size = 200):
    '''
    Left Direction Utility for SCAN Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort(reverse=True)
    smaller.sort(reverse=True)

    # Traverse all the sectors behind the initial head position
    if len(smaller)!=0:
        for sector in smaller:
            next_sector = sector
            path_taken.append(next_sector)
            thm+=abs(next_sector-curr_head_pos)
            curr_head_pos = next_sector

        # Travel to Sector 0
        next_sector=0
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    if len(greater)==0:
        return thm, path_taken

    # Travel To Last Sector
    next_sector=disk_size-1
    path_taken.append(next_sector)
    thm+=abs(next_sector-curr_head_pos)
    curr_head_pos = next_sector

    # Traverse all the sectors ahead of initial head position
    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector


    
    return thm, path_taken


def cscan(request:list, initial_head_pos=53, direction='right', disk_size = 200):
    '''
    C SCAN Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - direction : direction of head when movement begins
    - disk_size : Total no of sectors in disk
    '''
    if direction.lower()=='right':
        return rcscan(request, initial_head_pos, disk_size)

    else:
        return lcscan(request, initial_head_pos, disk_size)

#--------------------------------LOOK------------------------------

def rlook(request:list, initial_head_pos=53, disk_size=200):
    '''
    Right Direction Utility for LOOK Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort()
    smaller.sort(reverse=True)

    # Traverse all the sectors ahead of the inital head position
    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    # Traverse all the sectors behind the initial head position
    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector
    
    return thm, path_taken

def llook(request:list, initial_head_pos=53, disk_size=200):
    '''
    Left Direction Utility for LOOK Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort()
    smaller.sort(reverse=True)

    # Traverse all the sectors behind the initial head position

    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)

        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector


    # Traverse all the sectors ahead of the initial head postition
    
    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    
    return thm, path_taken


def look(request:list, initial_head_pos=53, direction='right', disk_size=200):
    '''
    LOOK Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - direction : initial direction of the head movement
    - disk_size : Total no of sectors in disk
    '''
    
    if direction.lower()=='right':
        return rlook(request, initial_head_pos, disk_size)

    else:
        return llook(request, initial_head_pos, disk_size)




#--------------------------------C LOOK----------------------------
def rclook(request:list, initial_head_pos=53, disk_size = 200):
    '''
    Right Direction Utility for C LOOK Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort()
    smaller.sort()

    # Traverse all the sectors ahead of the initial head position
    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    # Traverse all the sectors behind the inital head position
    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector
    
    return thm, path_taken

def lclook(request:list, initial_head_pos=53, disk_size = 200):
    '''
    Left Direction Utility for C LOOK Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - disk_size : Total no of sectors in disk
    '''
    thm = 0
    curr_head_pos = initial_head_pos
    path_taken = [initial_head_pos]

    greater = [sector for sector in request if sector>initial_head_pos]
    smaller = [sector for sector in request if sector<=initial_head_pos]

    greater.sort(reverse=True)
    smaller.sort(reverse=True)

    # Traverse All the Sectors behind the inital head position

    for sector in smaller:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector

    # Traverse all the Sectors Ahead of the initial head position

    for sector in greater:
        next_sector = sector
        path_taken.append(next_sector)
        thm+=abs(next_sector-curr_head_pos)
        curr_head_pos = next_sector
    
    return thm, path_taken



def clook(request:list, initial_head_pos=53, direction='right', disk_size=200):
    '''
    C LOOK Scheduling

    ### Returns:
    - thm : Total Head Movement [Int]
    - path_taken : Path Taken [Array of ints]

    ### Params:
    - request : Array of sectors
    - inital_head_pos : Inital Sector Location Of Head
    - direction : direction of the head movement
    - disk_size : Total no of sectors in disk
    '''
    
    if direction.lower() == 'right':
        return rclook(request, initial_head_pos, disk_size)
    else:
        return lclook(request, initial_head_pos, disk_size)
