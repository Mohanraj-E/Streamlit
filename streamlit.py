import streamlit as st

# Data Analysis function
def Census_Data():
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
    
def Sales_insight():
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
    
def DataBase_Management():
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
    
def Registration():
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
    
def Netflix_data():
    st.header("Netflix data")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Netflix_Dataset ")#github link
    st.header("Explaination")
    st.markdown("""The project I have taken from API and the Netflix data has
     Show_Id,Category,Title,Director,Cast,Country,Release_Date,Rating,Duration,Type,Description 
     I have performed data cleaning process like\n
     1. Handling the missing value\n
     2. Duplicate handling\n
     3. Datetime function\n""")
    st.markdown("""using pandas library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the Netflix data according to username
Need to analyse the data and find how many people are subscribed ''')
    
def College_Data():
    st.header("College Data")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/College%20Data")#github link
    st.header("Explaination")
    st.markdown("""This project given to me by Guvi Institution as an assessment. 
    In this project the following process are done:\n
     1. Merging Two DataFrame into Single DataFrame.\n
     2. Creating Different CSV file to the data which classified Based on their scores.\n
     3. Department wise codekata performenc - Data Visualization\n
     4. Department wise toppers - Data Visualization\n""")

def Student_Data_Insight():
    st.header("Student Data Insight")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Mongodb%20Case%20Study/Student%20Data%20Insight")#github link
    st.header("Explaination")
    st.markdown("""This project given to me by Guvi Institution as an assessment. 
    In this task I perform various quries using:\n
     1.Unwind.\n
     2.Aggregate.\n
     3.Projection\n""")
    
    
    
    
# Machine Learning Function
def E_Mail():
    st.header("E-Mail Verification")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/E-Mail%20Verification")
    st.header("Explaination")
    st.markdown("""In this project I created and train the Machine learning Model to verify the incoming Mail 
                    i.e in this case an user input and report whether it is Spam or Not-Spam.
     I have performed data preprocessing like\n
     1.Created a column using one hot encoding\n
     2.Split the data into Train and Test datasets\n
     3.Using MultinomialNB model form sklearn.naive_bayes for prediction \n
     4.Creating a model which Accepts user input and determine wether it is Spam or Not Spam""")
    
def Credit_Card():
    st.header("Credit Card Fraud Detection")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/Credit%20Card%20Fraud%20Detection")
    st.header("Explaination")
    st.markdown("""In this project I created and train the Machine learning Model for Credit Card Fraud Detection using Logistic Regression
     I have performed data preprocessing like\n
     1.Split the data into Train and Test datasets\n
     2.Using RandomUnderSampler from imblearn.under_sampling
     3.Using Logistic Regression model form sklearn.linear_model for prediction \n""")

def Oil_Price():
    st.header("Oil Price Prediction")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/Oil%20Price%20Prediction")
    st.header("Explaination")
    st.markdown("""In this project I created and train the Machine learning Model for Oil Price Prediction using Linear Regression
     I have performed data preprocessing like\n
     1.Split the data into Train and Test datasets\n
     2.Using Linear Regression model form sklearn.linear_model for prediction\n""")
    
    
# Selecting the Data Analysis Project    
Data_analysis_funcs = {
    "Census_data": Census_Data,
    "Sales_insight": Sales_insight,
    "DataBase Management": DataBase_Management,
    "Registeration_Python": Registration,
    "Netflix_data" : Netflix_data,
    "College_Data" : College_Data,
    "Student Data Insight" : Student_Data_Insight,
}

def Data_analysis():
    st.sidebar.header("Data Analysis Project") 
    Choice = st.sidebar.selectbox("Select the Project", Data_analysis_funcs.keys())
    Data_analysis_funcs[Choice]()
 



# Selecting the Machine Learning Project
Machine_learnings_funcs = {
    "E-Mail Verification": E_Mail,
    "Credit Card Fraud Detection": Credit_Card,
    "Oil Price Prediction": Oil_Price,
}

def Machine_learning():
    st.sidebar.header("Machine Learning Project") 
    Ml_Choice = st.sidebar.selectbox("Select the Project", Machine_learnings_funcs.keys())
    Machine_learnings_funcs[Ml_Choice]()
    

    
# Selecting the Topic
datascience={
    "Data analysis" : Data_analysis,
    "Machine Learning" : Machine_learning,
    }
st.sidebar.header("Data Science Project")
selected_page = st.sidebar.selectbox("Select the topic",datascience.keys())
datascience[selected_page]() 
