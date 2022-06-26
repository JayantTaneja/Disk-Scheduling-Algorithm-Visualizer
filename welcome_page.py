#Welcome Page
import streamlit as st
from PIL import Image
def show_page1():

    st.write("## Welcome")

    image = Image.open("./images/marc-schulte-R4ntV8wKqrU-unsplash.jpg")

    st.image(image)
    st.markdown('''
    ### About this Web APP

    This web app aims to provide an easy and beginner friendly interface to visualize and understand
    some common **disk scheduling** algorithms used internally by Operating Systems


    ### Why build this?

    Operating Systems is an important topic commonly taught to Sophomore CS undergrads. While
    teachers do an excellent job at explaining the algorithms, there is something special about a cool
    animation to visualize them. Unfortunately if you search for Disk Scheduling Algorithm Visualizer, there are hardly any useful beginner friendly sites

    So I thought, "Why not build it myself?" 
    
    ### Steps To Use:
    - Select the page to display from the navigation panel on the side $\leftarrow$
    - Enter the details that the algorithm needs 
        - Sector requests [Basically a comma separated value list that represents disk sectors]
        - Disk Size [An integer]
        - Initial Head Pos [The starting point for the read write head]
    - Click On Animate Button
    - Enjoy !!
    

    ### About Me

    Hi there! I am Jayant Taneja, currently a Sophomore Computer Science Undergrad from India.

    I like to build not just software, but digital experiences.
    This web app was made as part of my 4th Sem Minor Project.
    ''')

