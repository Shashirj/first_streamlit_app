import streamlit
streamlit.title("My Moms New Healthy Dinner")
streamlit.header("Breakfast Favourite")
streamlit.text(" 🥣Omega 3 and Bluberry Oatmeal")
streamlit.text("🥗Kale Spinach and Rocket Soothie")
streamlit.text("🐔Hard Boiled Free Range Egg")
streamlit.text("🥑 🍞Avacado Toast")
streamlit.header("🍌🍓Build Your Own Fruit Smoothie🥝🍇")

import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),["Avocado","Banana"])
streamlit.dataframe(my_fruit_list)
