#import streamlit
streamlit.title("My Moms New Healthy Dinner")
streamlit.header("Breakfast Favourite")
streamlit.text(" 🥣Omega 3 and Bluberry Oatmeal")
streamlit.text("🥗Kale Spinach and Rocket Soothie")
streamlit.text("🐔Hard Boiled Free Range Egg")
streamlit.text("🥑 🍞Avacado Toast")
streamlit.header("🍌🍓Build Your Own Fruit Smoothie🥝🍇")

#import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),["Avocado","Banana"])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
import pandas as pd
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_row)

add_my_frruit = streamlit.text_input('Which fruit u like?','Kiwi')
streamlit.write('Thanks for adding  ', add_my_frruit)

my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')");
