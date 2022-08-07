#STORES SALES PREDICTION
Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast future client demand and adjust inventory management. In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. By mining the data store from the data warehouse, more anomalies and common patterns can be discovered. This work discusses how a retailer’s market data, can be used as a tool to improve profit.

Approach
Data Exploration : Read the dataset using pandas and numpy to find null values, categorical columns from the given dataset
Data Visualizations : Performed Exploratory Data Analysis, to gain insights and learn the correlation of the columns with the output variable.
Feature Engineering : Removed missing values and created new features as per insights.
Model Building : Built simple Regression models to check base accuracy and Mean squared error.
Model Building II : Performed Hyperparameter tuning using GridSearchCV
Deployment - Using Streamlit built a webapp, to predict the Item_Outlet_Sales provided all necessary inpputs are provided
Proposed Solution
The solution proposed by our team is a ML model that has been trained to take as input multiple parameters, which are,

Item_Identifier -
Item_Weight
Item_Fat_Content
Item_Visibility
Item_Type
Item_MRP
Outlet_Identifier
Outlet_Establishment_Year
Outlet_Size
Outlet_Location_Type
Outlet_Type
Output:

Item_Outlet_Sales
Techonlogies used:
Python Programming Language
SKlearn Machine Learning Library
Pandas library
Numpy library
Matplotlib & Seaborn libraries for plotting graphs
Streamlit
Heroku deployment platform
Jupyter Notebooks
