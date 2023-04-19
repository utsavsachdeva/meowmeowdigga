import streamlit as st
m=0
n1 = int(st.number_input('Insert first number',min_value=1, max_value=1000000, value=5, step=1))
n2=int(st.number_input('Insert second number',min_value=1, max_value=1000000, value=5, step=1))
n3=int(st.number_input('Insert third number',min_value=1, max_value=1000000, value=5, step=1))
if n1>=n2 and n1>=n3:
    m=n1
elif n2>=n1 and n2>=n3:
    m=n2
elif n3>=n1 and n3>=n2:
    m=n3
if st.button('Find largest number'):
    st.write('The largest number among the three is',m)        
    
