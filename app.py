import pandas as pd
import statistics
import streamlit as st
try:
    with st.form(key='my_form'):
        st.header('Network Prediction')
        d = st.number_input('Enter the phone number ',700000000,99999999999,key=1) 
        submit_button = st.form_submit_button(label='Submit')
        
    if submit_button ==1:           
        data = pd.read_csv('Book1.csv')
        phone = int (d)
        area = []
        callername = []
        callerid = []
        networkprovider = []
        callduration = []
        
        for i in range(len(data['caller_id'])):
            if phone == data['caller_id'][i]:
                st.text('Dear user your name is ')
                st.text(data['caller_name'][i])
                a = data['area'][i]
                area.append(a)
                b = statistics.mode(area)
                        
                
        for j in range(len(data['area'])):
            if b == data['area'][j]:
                networkprovider.append([data['network_provider'][j],data['call_duration'][j]])
        st.text("Network With Minimum Connectivity ") 
        st.text(min(networkprovider)[0])
    else :
        print("enter number ")    
        
except AttributeError:
      pass
