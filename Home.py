import streamlit as st

st.balloons()
st.title(":violet[Hiii Anushka !!!!]")

hbd = """ 
<p style="color : #E0115F; font-size: 35px; font-weight: bold">
        Happy Birthdayyyyyyy
</p>
"""
message1 = """ 
<p style="color : #f25aa1; font-size: 24px; font-weight: bold">
        I made this website without any experience so iktu ajob dekhte laagle maaf kore diyo 
        hehe.
        
</p>
"""
message2 = """ 
<p style="color : #f25aa1; font-size: 24px; font-weight: bold">
        Now to explore the site you can use the 2 arrow symbol on the top left hand side of your screen

</p>
"""

st.write(hbd, unsafe_allow_html = True)
st.write("")
st.write(message1, unsafe_allow_html = True)
st.write(message2, unsafe_allow_html = True)



