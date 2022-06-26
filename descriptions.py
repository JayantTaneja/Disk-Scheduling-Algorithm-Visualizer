DESCRIPTIONS = {
    'FCFS': '''
### Details :
 
FCFS is the simplest disk scheduling algorithm. 

As the name suggests, this algorithm entertains requests in the order 
they arrive in the disk queue. The algorithm looks very fair and there is 
no starvation (all requests are serviced sequentially) but generally, it 
does not provide the fastest service.

### Algorithm 

Following is the FCFS algorithm

1. Start at the initial head position
2. Traverse to the sectors as the arrive
3. Traverse to the sector closest to the current sector
4. Maintain currently travelled distance as
$$
    |Current \ Sector - Previous \ Sector|
$$
5. Repeat until all sectors have been serviced
The total head movement will be sum of all the travelled distances''',

#----------------------------SSTF--------------------------------


    'SSTF': ''' ### Details : \n
    The SSTF algorithm selects the request having the minimum distance
    from the current head position. Since distance increases with the
    number of cylinders traversed by the head, SSTF chooses the pending 
    request closest to the current head position.

    ### Algorithm
    Following is the SSTF algorithm

    1. Sort all the sector requests
    2. Start at the initial head position
    3. Traverse to the sector closest to the current sector
    4. Maintain currently travelled distance as
    $$
    |Current \ Sector - Previous \ Sector|
    $$
    5. Repeat until all sectors have been serviced
    The total head movement will be sum of all the travelled distances
    ''',
#-----------------------------SCAN-----------------------------------
    'SCAN' : ''' ### Details : \n
    SCAN algorithm works similar to elevators wherein we start servicing the \
    requests in a particular direction, reach the boundary of disk, \
    switch direction and service the remaining sectors travelling in \
    the opposite direction.
    
    ### Algorithm
    1. Maintain a list of sectors before the current sector and \
        after the current sector
    2. Based on initial scan direction
        1. Scan the previous sectors till sector 0 is reached or
        2. Scan the later sectors till last disk sector is reached
    3. Switch direction and traverse the remaining sectors
    ''',
#----------------------------CSCAN--------------------------
    'CSCAN' : ''' ### Details : \n
    CSCAN or Circular SCAN is a variant of SCAN wherein once we reach a boundary\
    we travel to opposite boundary and service the remaining sectors without changing
    direction
    ''',
#----------------------------LOOK----------------------------
    'LOOK' : ''' ### Details : \n
    LOOK is a modification of SCAN where we traverse only to the last extreme sector \
        in queue rather than last disk sector before switching direction
        ''',
#--------------------------CLOOK------------------------------------
    'CLOOK' : ''' ### Details : \n
    CLOOK or Circular LOOK is a modification of CSCAN where we traverse only to\
        opposite extreme sector in queue rather than opposite disk boundary'''
}