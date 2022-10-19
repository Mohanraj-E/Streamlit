import streamlit as st

def page1():
    st.header('Census Data')
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Census_Data ")#github link
    st.header("Explaination")
    st.markdown("""The project is taken from API and the Census data has
     District_code,State_name,District_name,Population,Male,Female,Literate,Workers,Male_Workers,Female_Workers,Christians,
     Sikhs,Buddhists,Jains,Secondary_Education,Higher_Education,Graduate_Education,Age_Group_0_29,Age_Group_30_49,Age_Group_50.
     I have performed data preprocessing like\n
     1.groupby function\n
     2.add prefix and suffix to column name\n
     3.Creating and deleting the column\n
     4.Visualization using plotly""")
    st.markdown("""using pandas library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the india census data according to state-wise
Need to analyse the data and find the unemployment in statewise. 
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
Need to analyse the data and find how the sales is according to the price of the product.
''')
    
def page3():
    st.header("DataBase Management")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/DataBase%20Management")#github link
    st.header("Explaination")
    st.markdown("""I have performed data management process like\n
     1.Creating a new database in MySQL server and adding data file\n
     2.Creating a new database in NoSQL(MongoDB) server and add data file\n
     3.Retrive the data from the NoSQL(MongoDB) server and adding it into a MySQL server\n""")
    st.markdown("""using pandas and matplotlib library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The process describe the creating new database , tabels , collections , coverting into dataframe and converting into dictionary.
''')
    
    
def page4():
    st.header("Registration")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Registration")#github link
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

def E_Mail():
    st.header("E-Mail Verification")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/E-Mail%20Verification")
    
    
    
Data_analysis_funcs = {
    "Census_data": page1,
    "Sales_insight": page2,
    "DataBase Management": page3,
    "Registeration_Python": page4,
}

def Data_analysis():
    st.sidebar.header("Data Analysis Project") 
    Choice = st.sidebar.selectbox("Select a Project", Data_analysis_funcs.keys())
    Data_analysis_funcs[Choice]()
 
Machine_learnings_funcs = {
    "E-Mail Verification": E_Mail,
}

def Machine_learning():
    st.sidebar.header("Machine Learning Project") 
    Ml_Choice = st.sidebar.selectbox("Select a Project", Machine_learnings_funcs.keys())
    Machine_learnings_funcs[Ml_Choice]()
    

datascience={
    "Data analysis" : Data_analysis,
    "Machine Learning" : Machine_learning,
    }
def main_page():
    st.sidebar.header("Data Science Project")
    selected_page = st.sidebar.selectbox(datascience.keys())
    datascience[selected_page]() 

