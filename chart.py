#Module containing utility charting functions
import pandas as pd
import plotly.express as px
import streamlit as st
import time

def animater(path_taken, waiting_time = 0.5):
    '''
    Animates the plot of path taken vs iterations
    # Params
    - path_taken : list of ints representing the sectors
    '''

    x = path_taken
    y = [-i for i in range(len(x))]

    #Empty dataframe
    d = pd.DataFrame(
        {
            'DiskSector' : [],
            'Iteration' : []
        }
    )
    # Empty figure
    fig = px.line(
        d, 
        x="DiskSector", 
        y="Iteration", 
        text="DiskSector"
    )
    #Set ranges of x and y axes
    fig.update_xaxes(range=[-1, max(x)+10])
    fig.update_yaxes(range=[len(y)+1, 1])
    graph = st.plotly_chart(fig, use_container_width=True)

    #Containers for holding the temporary list slices
    data_x = []
    data_y = []

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(len(y)):

        progress=int((i+1)/len(y) *100)
        status_text.text("%i%% Complete" % progress)
        progress_bar.progress(progress)

        data_x.append(x[i])
        data_y.append(y[i])

        d2 = pd.DataFrame(
            {
                'DiskSector' : data_x,
                'Iteration' : data_y
            }
        )
        fig=px.line(
            d2,
            x = "DiskSector",
            y = "Iteration",
            text = "DiskSector"
        )
        fig.update_traces(textposition="bottom right")
        
        fig.update_xaxes(range=[-1, max(path_taken)+10], side="top")
        fig.update_yaxes(
            range=[-len(y)-1, 1],
            tickmode = "array",
            tickvals = data_y,
            ticktext = [str(-i) for i in data_y]
        )

        graph.plotly_chart(fig, use_container_width=True)
        time.sleep(waiting_time)

def comparison_chart(data, waiting_time = 0.1):
    '''
    Utility function for displaying comparision chart for all algorithms'''
    #Variables storing the thms of the algorithms
    algo1 = data["fcfs"]
    algo2 = data["sstf"]
    algo3 = data["scan"]
    algo4 = data["cscan"]
    algo5 = data["look"]
    algo6 = data["clook"]

    #Max thm
    max_thm = max(data.values())
    data_f = pd.DataFrame(
        {
            "FCFS" : [0, 0, 0, 0, 0, 0],
            "SSTF" : [0, 0, 0, 0, 0, 0],
            "SCAN" : [0, 0, 0, 0, 0, 0],
            "CSCAN": [0, 0, 0, 0, 0, 0],
            "LOOK" : [0, 0, 0, 0, 0, 0],
            "CLOOK": [0, 0, 0, 0, 0, 0],
        },
        index = ["FCFS", "SSTF" , "SCAN", "CSCAN", "LOOK", "CLOOK",]
    )
    #Empty Figure
    fig = px.bar(
        data_f,
        labels  = {
            "index" : "algorithm",
            "value" : "THM"
            }
    )
    
    chart = st.button(label = "show results")
    bar = st.plotly_chart(fig, use_container_width=True)
    
    if chart:
        for _ in range(10):
            # Incrementally increase the size of bars
            data_f["FCFS"][0] += algo1//10
            data_f["SSTF"][1] += algo2//10
            data_f["SCAN"][2] += algo3//10
            data_f["CSCAN"][3] += algo4//10
            data_f["LOOK"][4] += algo5//10
            data_f["CLOOK"][5] += algo6//10
        
            fig = px.bar(
                data_f,
                labels  = {
                "index" : "Algorithm",
                "value" : "THM"
                }
            )
        
            fig.update_yaxes(range=[0, max_thm+50])
            bar.plotly_chart(fig, use_container_width=True)
            time.sleep(0.02)
        
        data_f["FCFS"][0] = algo1
        data_f["SSTF"][1] = algo2
        data_f["SCAN"][2] = algo3
        data_f["CSCAN"][3] = algo4
        data_f["LOOK"][4] = algo5
        data_f["CLOOK"][5] = algo6
        
        fig = px.bar(
            data_f,
            labels  = {
            "index" : "Algorithm",
            "value" : "THM"
            }
        )
        fig.update_yaxes(range=[0, max_thm+50])
        bar.plotly_chart(fig, use_container_width=True)

        min_thm_algo = min(data, key=data.get)
        max_thm_algo = max(data, key=data.get)
        st.markdown(f'''### Results [For this sector request ]:
        \n#### Most efficient Algorithm : {min_thm_algo.upper()}
        \n#### Least Efficient Algorithm : {max_thm_algo.upper()}
        ''')
