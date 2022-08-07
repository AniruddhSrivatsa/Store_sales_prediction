# Store_sales_prediction

Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast future client demand and adjust inventory management. 
In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. 
By mining the data store from the data warehouse, more anomalies and common patterns can be discovered. 
This work discusses how a retailer’s market data, can be used as a tool to improve profit.

# Approach

  Data Exploration :    Read the dataset using pandas and numpy to find null values, categorical columns from the given dataset
  
  Data Visualizations :  Performed Exploratory Data Analysis, to gain insights and learn the correlation of the columns with the output variable.
  
  Feature Engineering :  Removed missing values and created new features as per insights.
  
  Model Building :   Built simple Regression models to check base accuracy and Mean squared error.
  
  Model Building II :   Performed Hyperparameter tuning using GridSearchCV
  
  Deployment :   Using Streamlit built a webapp, to predict the Item_Outlet_Sales provided all necessary inpputs are provided
 
Link: https://store-sales-predict.herokuapp.com/
