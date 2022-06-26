import streamlit as st
from algos import fcfs, sstf, scan, cscan, look, clook
from algo_test import validate_request
from chart import animater
from descriptions import DESCRIPTIONS

algorithms_functions_dict = {
    'FCFS' : fcfs,
    'SSTF' : sstf,
    'SCAN' : scan,
    'CSCAN': cscan,
    'LOOK' : look,
    'CLOOK': clook,
}

def show_visualizer():
    '''
    Function to render the visualizer page'''


    '''
    --------------------------------UI------------------------------
    '''

    st.write('''
    ## Enter Details For Visualization 
    ''')

    speed = st.select_slider(
        label="Animation Speed", 
        value="||", 
        options=["Slow", '|', '||', '|||',"Fast"], 
        help="Choose the Speed Of Animation"
    )

    requests = st.text_input(label="Enter the request queue (, separated)", value = "13, 47, 168, 52, 67, 22, 45, 68, 95")

    columns = st.columns(2)
    with columns[0]:
        disk = st.number_input(label="Enter disk size", min_value=0, value=200)
    with columns[1]:
        initial_head = st.number_input(
            label="Enter initial position of the head", 
            min_value=0, 
            max_value=int(disk-1)
            )
    
    with columns[0]:        
        algorithm = st.selectbox(
            'Select Algorithm',
            (
                'FCFS',
                'SSTF',
                'SCAN',
                'CSCAN',
                'LOOK',
                'CLOOK',
            ),
            index=0,
            help="Algorithm defines the path the disk will \
                take while navigating the requests"
        )
    
    head_direction=None
    if algorithm=='SCAN' or algorithm=='CSCAN' or algorithm=='LOOK' or algorithm=='CLOOK':
        with columns[1]:
            head_direction = st.selectbox(
                label="Select the scanning direction", 
                options=["Left", "Right"], 
                index=1)
    
    animate = st.button(label="Animate")

    '''
    ---------------------------Logic-----------------------------------
    '''

    requests = [int(i) for i in requests.split(',')]

    if not validate_request(requests, disk):
        st.error("Invalid requests")
        st.stop()

    if head_direction:# For algorithms with initial head direction i.e. SCAN, CSCAN, LOOK, CLOOK
        thm, path_taken = algorithms_functions_dict[algorithm](
            requests, 
            initial_head_pos=initial_head, 
            direction = head_direction.lower()
            )
    else:
        thm, path_taken = algorithms_functions_dict[algorithm](
            requests, 
            initial_head_pos=initial_head
            )

    if animate:
        animater(path_taken, waiting_time = time_from_speed(speed))
        st.metric(label="THM", value=thm)
    
    
    st.markdown(DESCRIPTIONS[algorithm])

def time_from_speed(speed:str):
    '''
    Utility function to return time delay corresponding to animation speed
    
    ## Returns
    - Time delay in seconds
    '''
    if speed.lower()=="slow":
        return 1
    elif speed.lower()=="|":
        return 0.9
    elif speed.lower()=="||":
        return 0.75
    elif speed.lower()=="|||":
        return 0.5
    else:
        return 0.25