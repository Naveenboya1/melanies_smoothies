# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie!:cup_with_straw:")
st.write(
    """Choose your Fruits you want in your custome Smoothie
    """
)



cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME',))
#st.dataframe(data=my_dataframe, use_container_width=True)


import streamlit as st
    
ingredients_list = st.multiselect(
    'choose upto to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)   


if  ingredients_list:
    ingredients_string=''
    
    
name_on_order = st.text_input("Name of Smoothie!")
st.write("Name of Smoothie will be", name_on_order)
    
    
        for fruit_choosan in ingredients_list:
           ingredients_string+=fruit_choosan +' '
           st.write(ingredients_string)



    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+ """')"""
    time_start_stmt=st.button('Sibmit order')
    
    
    if time_start_stmt:
        session.sql(my_insert_stmt).collect()
        st.success('Your smoothie is ready!')
   
    st.write(my_insert_stmt)
    st.stop()



    

      
        







    
