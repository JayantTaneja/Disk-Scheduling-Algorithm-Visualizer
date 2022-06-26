import streamlit as st
from algos import fcfs, sstf, scan, cscan, look, clook
from chart import comparison_chart

def show_comparison(initial=53):
    
    requests = st.text_input(label="Enter the request queue (, separated)", value = "13, 47, 168, 52, 67, 22, 45, 68, 95")
    request = [int(i) for i in requests.split(',')]
    columns = st.columns(2)
    with columns[0]:
        disk_size = st.number_input(label="Enter disk size", min_value=1, value=200)
    with columns[1]:
        initial = st.number_input(label="Enter initial position of head", value=0, min_value=0)
    
    thms = {}
    thms["fcfs"], _ = fcfs(list(request), initial)
    thms["sstf"], _ = sstf(list(request), initial)
    thms["scan"], _ = scan(list(request), initial)
    thms["cscan"],_ = cscan(request, initial)
    thms["look"], _ = look(request, initial)
    thms["clook"],_ = clook(request, initial)

    comparison_chart(thms)
