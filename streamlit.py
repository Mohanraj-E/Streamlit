import streamlit as st
st.set_page_config(page_title="Mohanraj.E Data Science Project")

# Data Analysis function
def Census_Data():
    st.header('Census Data Insight')
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Census_Data ")#github link
    st.header("Explanation")
    st.markdown("""This project is given by GUVI institution.\n
     I have performed data preprocessing like\n
        1. Data cleaning process using python library pandas.\n
        2. Census data with various feature.\n
        3. Data importing.\n
        4. Pandas groupby,agg,max,min,mean,mode,median.\n
        5. Walkthrough some Mongodb concept.""")

    
def Sales_insight():
    st.header("Sales insight")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Sales_Insight")#github link
    st.header("Explanation")
    st.markdown("""In this project I taken some Sales data and provide insight on those data.\n
     I have performed data cleaning process like\n
     1. Merge the multiple csv to one csv file\n
     2. Used some visualization technique\n""")

    
def DataBase_Management():
    st.header("DataBase Management")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/DataBase%20Management")#github link
    st.header("Explanation")
    st.markdown("""I have performed data management process like\n
     1.Creating a new database in MySQL server and adding data file\n
     2.Creating a new database in NoSQL(MongoDB) server and add data file\n
     3.Retrive the data from the NoSQL(MongoDB) server and adding it into a MySQL server\n""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The process describe the creating new database , tabels , collections , coverting into dataframe and converting into dictionary.
''')
    
def Registration():
    st.header("Registration")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Registration")#github link
    st.header("Explanation")
    st.markdown("""This project given to me by Guvi Institution as an assessment.\n
     In This task I Define three Main function:\n
     1. Registeration.\n
     2. Log In\Off.\n
     3. Forget Passsword.""")

def Netflix_data():
    st.header("Netflix Data Insight")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Netflix_Dataset ")#github link
    st.header("Explanation")
    st.markdown("""In this project I have taken some Netflix data and did some insight.\n
     I have performed data cleaning process like\n
     1. Handling the missing value\n
     2. Duplicate handling\n
     3. Datetime function\n""")

    
def College_Data():
    st.header("College Data Insight")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/College%20Data")#github link
    st.header("Explanation")
    st.markdown("""This project given to me by Guvi Institution as an assessment.\n
    In this project the following process are done:\n
     1. Merging Two DataFrame into Single DataFrame.\n
     2. Creating Different CSV file to the data which classified Based on their scores.\n
     3. Department wise codekata performenc - Data Visualization\n
     4. Department wise toppers - Data Visualization\n""")

def Student_Data_Insight():
    st.header("Student Data Insight")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Data%20Analysis/Mongodb%20Case%20Study/Student%20Data%20Insight")#github link
    st.header("Explanation")
    st.markdown("""This project given to me by Guvi Institution as an assessment.\n
    In this task I perform various quries using:\n
     1.Unwind.\n
     2.Aggregate.\n
     3.Projection\n""")
    
    
    
    
# Machine Learning Function
def E_Mail():
    st.header("E-Mail Verification")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/E-Mail%20Verification")
    st.header("Explanation")
    st.markdown("""In this project I created and train the Machine learning Model for verifying E-Mail .\n
     I have performed these data preprocessing as follows:\n
     2.Split the data into Train and Test datasets\n
     3.Using MultinomialNB model form sklearn.naive_bayes for prediction \n
     4.Creating a model which Accepts user input and determine wether it is Spam or Not Spam""")
    
def Credit_Card():
    st.header("Credit Card Fraud Detection")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/Credit%20Card%20Fraud%20Detection")
    st.header("Explanation")
    st.markdown("""In this project I created and train the Machine learning Model for Credit Card Fraud Detection using Logistic Regression.\n
    I have performed these data preprocessing as follows:\n
     1.Split the data into Train and Test datasets.\n
     2.Using RandomUnderSampler from imblearn.under_sampling.\n
     3.Using Logistic Regression model form sklearn.linear_model for prediction.\n""")

def Oil_Price():
    st.header("Oil Price Prediction")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/Oil%20Price%20Prediction")
    st.header("Explanation")
    st.markdown("""In this project I created and train the Machine learning Model for Oil Price Prediction using Linear Regression.\n
     I have performed these data preprocessing as follows:\n
     1.Split the data into Train and Test datasets\n
     2.Using Linear Regression model form sklearn.linear_model for prediction\n""")
    
def Bitcoin_Prediction():
    st.header("Bitcoin Price Prediction")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/Bitcoin%20Price%20Predictions")
    st.header("Explanation")
    st.markdown("""This Following process are all done in this project:\n
                    1. Reading, Cleaning and Converting the Data into more Understandable Way.\n
                    2. Splitting the dataset and Trainning the splitted data into the Linear Regression Model.\n
                    3. Calculating K-Fold Cross_Val_Score to check wether the model Works Perfectly.\n""")
    
def Twitter_Sentiment_Analysis():
    st.header("Twitter Sentiment Analysis")
    st.subheader('Github link')
    st.write("https://github.com/Mohanraj-E/Data-Science-Projects/tree/main/Machine%20Learning/TWITTER_SENTIMENT_ANALYSIS")
    st.header("Explanation")
    st.markdown("""The following project is about analyzing the sentiments of tweets on social networking website ‘Twitter’.\n
    The dataset for this project is scraped from Twitter. It contains 1,600,000 tweets extracted using Twitter API. 
    It is a labeled dataset with tweets annotated with the sentiment (0 = negative, 2 = neutral, 4 = positive).\n
    It contains the following 6 fields:\n
        target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive).\n
        ids: The id of the tweet.\n
        date: The date of the tweet (Sat May 16 23:58:44 UTC 2009).\n
        flag: The query. If there is no query, then this value is NO_QUERY.\n
        user: The user that tweeted.\n
        text: The text of the tweet.\n
    Designed a classification model that correctly predicts the polarity of the tweets provided in the dataset..\n""")
    
# Selecting the Data Analysis Project    
Data_analysis_funcs = {
    "College_Data" : College_Data,
    "DataBase Management": DataBase_Management,
    "Student Data Insight" : Student_Data_Insight,
    "Registeration_Python": Registration,
    "Census_data": Census_Data,
    "Sales_insight": Sales_insight,
    "Netflix_data" : Netflix_data,
}

def Data_analysis():
    st.sidebar.header("Data Analysis Project") 
    Choice = st.sidebar.selectbox("Select the Project", Data_analysis_funcs.keys())
    Data_analysis_funcs[Choice]()
 



# Selecting the Machine Learning Project
Machine_learnings_funcs = {
    "Twitter Sentiment Analysis": Twitter_Sentiment_Analysis,
    "Oil Price Prediction": Oil_Price,
    "Bitcoin Price Prediction": Bitcoin_Prediction,
    "E-Mail Verification": E_Mail,
    "Credit Card Fraud Detection": Credit_Card
    
}

def Machine_learning():
    st.sidebar.header("Machine Learning Project") 
    Ml_Choice = st.sidebar.selectbox("Select the Project", Machine_learnings_funcs.keys())
    Machine_learnings_funcs[Ml_Choice]()
    

    
# Selecting the Topic
datascience={
    "Data analysis" : Data_analysis,
    "Machine Learning" : Machine_learning,
    "Natural language Processing" : NLP
    }
st.sidebar.header("PORTFOLIO")
st.sidebar.markdown("""Hello, This is Mohanraj E Aspirant to be an Data Scientist.\n
                    Seeking to advance my career in the Booming field of Data Science. 
                    Have a strong analytical, programming and communication skills to succeed in this field.\n
                    These are some of the project I have done to hone my skills.""")
st.sidebar.subheader('Data Science Project')
selected_page = st.sidebar.selectbox("Select the topic",datascience.keys())
datascience[selected_page]() 
