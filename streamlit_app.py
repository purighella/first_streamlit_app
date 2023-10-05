import streamlit

streamlit.title('My Parents\' New Healthy Diner - it is a \'dosa place\' in Secunderabad')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗 Idli Sambar')
streamlit.text('🐔 Ghee dosa with onions') 
streamlit.text('🥑🍞Chutney, Potato masala curry and Sambar')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
