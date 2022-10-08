import streamlit as st

def main_page():
    st.header('Census Data 201.')
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Census_Data ")#github link
    st.header("Explaination")
    st.markdown("""The project is taken from API and the Census data has
     District_code,State_name,District_name,Population,Male,Female,Literate,Workers,Male_Workers,Female_Workers,Christians,
     Sikhs,Buddhists,Jains,Secondary_Education,Higher_Education,Graduate_Education,Age_Group_0_29,Age_Group_30_49,Age_Group_50.
     I have performed data preprocessing like\n
     1.groupby function\n
     2.add prefix and suffix to column name\n
     3.creating and deleting the column\n""")
    st.markdown("""using pandas library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the india census data according to state-wise
Need to analyse the data and find the unemployment in statewise  
\nData_Set link: 
''')
    
def page2():
    st.header("Sales insight")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Sales_Insight")#github link
    st.header("Explaination")
    st.markdown("""The project is taken from API and the Sales insight data which has
     Multiple csv with the column name of Order ID,Product,Quantity Ordered,Price Each,Order Date,Purchase Address.
     I have performed data cleaning process like\n
     1.merge the multiple csv to one csv file\n
     2.type casting the datatype\n
     3.use some visualization\n""")
    st.markdown("""using pandas and matplotlib library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the Sales according to every month 
Need to analyse the data and find how the sales is according to the price of the product \n
Data_Set link:
''')
    
    
def page3():
    st.header("Registration")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Assignment-1/blob/main/Assignment-1.ipynb")#github link
    st.header("Explaination")
    st.markdown("""This project is given by GUVI institution and it has to be done using python
     under the concept of File handling
     i have seprate the process like\n
     1.First user to register with username and password 
     (username and password want to check if it is valid or not with some criteria)
     then save it in the text file\n
     2.Login with the valid username and password and check whether the username and
      password are in the file or not if not go to the registration \n
     3.Forget password if the user click on forget pasword two thing to do\n
     A)Retrive the data with the username itself\n
     B)Provide new password and replace the new password with the 
     usernamme in the file """)
    st.markdown("""used python code and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
    The project is to create a registration form using python code 
    with a concept of file handling,The Jupyter notebook link 
    and full explaination is given in the main page''' )   
    
page_names_to_funcs = {
    "Census_data": main_page,
    "Sales_insight": page2,
    "Registeration_Python": page3,
}
st.sidebar.header("Data_Analyst Project")
selected_page = st.sidebar.selectbox("Select a Project", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() 
