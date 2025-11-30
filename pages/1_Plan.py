import streamlit as st
import os

st.title(":violet[Plan for today]")
st.write("")
head_1 = """ 
<p style="color : #E0115F; font-size: 35px; font-weight: bold">
        We are gonna figure out today's plan together. I have a basic layout but we will decide the specifics together.
</p>
"""
message_1 = """ 
<p style="color : #f25aa1; font-size: 24px">
        I am going to have fried chicken but we don't know what you want to have. So lets figure that out together
</p>
<p style="color : #f25aa1; font-size: 24px">
        What options do we have for you here?
</p>
"""

message_2 = """ 
<p style="color : #f25aa1; font-size: 24px">
        Now that we are done selecting and ordering the food lets find a movie that we can watch together.
</p>
<p style="color : #f25aa1; font-size: 24px">
        The movie selection might be a little biased because I want to watch a Hindi movie
</p>
"""

message_3 = """ 
<p style="color : #f25aa1; font-size: 24px">
        Onno kichu dekhte chaile amke bole diyoo hehe i dont mind watching anything with youu mwahh.
</p>
"""

message_4 = """ 
<p style="color : #f25aa1; font-size: 24px">
        This is optional because idk if we will have time. Mostly probably we will be too sleepy
</p>
<p style="color : #f25aa1; font-size: 24px">
        Games e we dont have many options I think.
</p>
<hr style="border: 1px solid #f25aa1; margin: 15px 0;">
<p style="color : #f25aa1; font-size: 24px">
        We can play:
</p>
"""

message_5 = """ 
<p style="color : #f25aa1; font-size: 24px">
        Oh no you ended the dayyyy. Now we need to sleeppp.
</p>
<p style="color : #f25aa1; font-size: 60px">
       GOOODDDD NIGHTT PAKHIIIII. MWAHHHHDUHWDHUW
<p>
"""


st.write(head_1, unsafe_allow_html = True)
tab1, tab2, tab3, tab4 = st.tabs(["Order food", "Movie to Watch", "Games", "Top Secret"])
with tab1:
    st.write(message_1, unsafe_allow_html = True)
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.image(os.path.join(os.getcwd(), "static", "gustosand.jpeg"))
        st.link_button(label= ":violet[Gustooo!!!!]",
                       url= "https://www.foodpanda.com.bd/restaurant/s1vj/gusto",
                       help= "Click me to order from FoodPanda")


    with col2:
        st.image(os.path.join(os.getcwd(), "static", "soup.jpeg"))
        st.link_button(label=":violet[Trouvailleeee!!!!]",
                       url= "https://www.foodpanda.com.bd/restaurant/s5im/trouvaille",
                       help="Click me to order from FoodPanda")

    with col3:
        st.image(os.path.join(os.getcwd(), "static", "pizza.jpeg"))
        st.link_button(label=":violet[Dominosssss!!!!]",
                       url="https://www.foodpanda.com.bd/restaurant/ksg0/dominos-pizza-uttara-6",
                       help="Click me to order from FoodPanda")

    with col4:
        st.image(os.path.join(os.getcwd(), "static", "food.jpeg"))
        st.link_button(label= ":violet[Something elsee waahhhh!!!!]",
                       url= "https://www.foodpanda.com.bd/restaurants/new/?lat=23.870271913367553&lng=90.39652691373803&vertical=restaurants&expedition=delivery",
                       help= "Click me to order from FoodPanda")

with tab2:
    st.write(message_2, unsafe_allow_html= True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(":violet[Piku]")
        st.image(os.path.join(os.getcwd(), "static", "piku.jpg"))
        st.link_button(label= ":violet[Dekhboooo!#$$!$##]",
                       url= "https://sflix.ps/watch-movie/free-piku-hd-15821.5354269",
                       help= "Click me to watch the movie")
        st.link_button(label= ":violet[Click me if the button above doesn't work]",
                       url= "https://www.dailymotion.com/video/x9jxr8e",
                       help= "Click me to watch the movie")

    with col2:
        st.subheader(":violet[Rocky aur Rani]")
        st.image(os.path.join(os.getcwd(), "static", "rocky_rani.jpeg"))
        st.link_button(label= ":violet[Dekhbo hehehehehe]",
                       url= "https://www.bilibili.tv/en/video/4791864103404032",
                       help= "Click me to watch the movie")
        st.button(":violet[If you want to watch on screenshare]", help= "Pressing the button wont do anything because ami nije screenshare korbo")

    with col3:
        st.subheader(":violet[Red White and Royal Blue]")
        st.image(os.path.join(os.getcwd(), "static", "rwb.png"))
        st.link_button(label= ":violet[Letsss gooooo dekhboowjdiwajiduhuae]",
                       url= "https://sflix.ps/watch-movie/free-red-white-royal-blue-hd-99163.9825649",
                       help= "Click me to watch the movie")
    st.write(message_3, unsafe_allow_html= True)


with tab3:
    st.write(message_4, unsafe_allow_html= True)
    st.write(":violet[Either we can play the code guessing game ]")
    st.write(":violet[Or we can play Murdle (Pleasee khelii I wanna playy 🥺) ]")
    st.write(":violet[Or we can play the guessing games we play on reels ]")
    st.subheader(":violet[If you have something else in mind then tell meeeeeeeee idiotttttttttttttttttttttttt!!!!!!!!!!!!!! ]")
    with st.container(border = True):
        st.header(":red[Note:]")
        st.subheader(":red[Go to the Top Secret Section only after going through the entire website]")

with tab4:
    st.header(":red[DO NOT PRESS THE BUTTON.]")
    st.header(":red[I REPEAT DO NOT PRESS THE BUTTON.]")
    if 'show_container' not in st.session_state:
        st.session_state['show_container'] = False
    def toggle_container():
        st.session_state['show_container'] = not st.session_state['show_container']
    button_label = ":red[Please do not press me]" if not st.session_state['show_container'] else ":violet[Oh noooooooo you pressed me]"
    st.button(button_label, on_click= toggle_container)
    if st.session_state['show_container']:
        with st.container(border = True):
            st.write(message_5, unsafe_allow_html= True)
