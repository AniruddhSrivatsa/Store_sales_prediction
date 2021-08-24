import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px


new_title = '<p style="font-family:sans-serif; color:NAVY; font-size: 30px;">STORES SALES PREDICTION</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.subheader("Dataset:")
df=pd.read_csv("Train.csv")
st.dataframe(data=df)
st.write("\n")
st.subheader("Description:")
st.write("\n")
st.write(df.describe())
st.write("\n")
st.subheader("Null_Values:")
st.write("\n")
st.write(df.isna().sum())
st.write("\n")

columns=df.columns
num_vars=df.select_dtypes(include=["int64","float64"]).columns #selecting the int and float datatype columns
cat_vars=df.select_dtypes(include=["object"]).columns #selecting the object datatype column

#selecting multiple columns to be viewed simultaneously for better observation between them
st.write("\n")
st.subheader("Select multiple columns to view simultaneously:")
st.write("\n")
cb_selcol=st.multiselect("",list(df.columns))
if cb_selcol is not None:
    st.write(df[cb_selcol])
    st.write("\n")

#for discrete numerical features (selecting columns which has not more than 20 unique categories)
num_cat=[]
for i in list(num_vars):
    if (len(df[i].unique())<=20): 
        num_cat.append(i)  # now num_cat contains discrete numerical features.

num_obj=[]
for i in list(cat_vars):
    if (len(df[i].unique())<=20): 
        num_obj.append(i)  # now num_obj contains columns with finite categories.


num_cat=num_cat+num_obj #now it contains all the columns which have not more than 20 unique categories

#finding unique categories
st.write("\n")

st.subheader("Unique categories and Value counts:")
st.write("\n")
if st.checkbox("Click the checkbox for finding unique categories and valuecounts"):
  st.write("\n")
  if num_cat is not None:
   for i in num_cat:
     if (len(df[i].unique())>20):

       st.write(i,"Column is not shown because it has more than 20 unique categories")
       st.markdown("**-------------------------------------------------------------------------------------------------**")
       pass
     else:
       st.write("Unique categories in ",i,"column:",df[i].unique())
       st.write("\n","\n")
       st.write("Value counts for unique categories in ",i,"column:")
       st.write(df[i].value_counts())

       st.markdown("**-------------------------------------------------------------------------------------------------**")



# features for histogram
num_feas_cat=list(num_vars)+num_cat  

# as histogram can take both continous values and categorical values
#and plots it with the no of occurences (count)
 
st.write("\n")
st.markdown("**-------------------------------------------------------------------------------------------------**")
st.write("\n")

st.header("Visualizations")
st.write("\n")
#container 1

viz1= st.beta_expander("Click here for Histogram, Box-plot, Violin-plot Visualisations")
cont1=viz1.beta_container()
cont1.write("Histogram plotting")
selection1 = cont1.selectbox("",options =list(set(num_feas_cat)))
hist = px.histogram(df, x=selection1)
cont1.plotly_chart(hist)
cont1.write("\n")

cont1.write("Box_Plot")
selection_x=cont1.selectbox("Select x coordinate (finite_categorical):",options=num_cat)
selection_y=cont1.selectbox("Select y coordinate (continuous_numerical):",options=list(set(list(num_vars)).difference(num_cat)))

box=px.box(df,x=selection_x,y=selection_y)
cont1.plotly_chart(box)


cont1.write("\n")

cont1.write("Violin_Plot")
selection_x1=cont1.selectbox("Select x1 coordinate (finite_categorical):",options=num_cat)
selection_y1=cont1.selectbox("Select y1 coordinate (continuous_numerical):",options=list(set(list(num_vars)).difference(num_cat)))
violin=px.violin(df,x=selection_x1,y=selection_y1,points="all")
cont1.plotly_chart(violin)

st.write("\n")

#container 2

viz2= st.beta_expander("Click here for Pie Chart and Heat-Map Visualisations")
cont2=viz2.beta_container()
cont2.write("Pie chart plotting")
selection2 = cont2.selectbox("",options =num_cat)
pie = px.pie(df, names=selection2)
cont2.plotly_chart(pie)
cont2.write("\n")

cont2.write("Heat Map")
hmap = px.imshow(df.corr())
cont2.plotly_chart(hmap)

st.write("\n")


#container 3

viz3= st.beta_expander("Click here for Scatter Visualisations")
cont3=viz3.beta_container()
cont3.write("Scatter plotting")
selection_x2=cont3.selectbox("Select x2 coordinate (numerical):",options=list(set(list(num_vars)).difference(num_cat)))
selection_y2=cont3.selectbox("Select y2 coordinate (numerical):",options=list(set(list(num_vars)).difference(num_cat)))
none=[None]
colors3=cont3.selectbox("Select the features for hue:",options=none+num_cat)

try:
    scat=px.scatter(df,x=selection_x2,y=selection_y2,color=colors3)
    cont3.plotly_chart(scat)
except KeyError:
    st.error("This column hue cannot be displayed because it contains NaN values")
st.write("\n")
st.markdown("**-------------------------------------------------------------------------------------------------**")
st.write("\n")

#---------------------------------------------------------------
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 30px;">User Inputs for outlet sales prediction</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.write("\n")



new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Item Weight:</p>'
st.markdown(new_title, unsafe_allow_html=True)
wei=st.number_input("",value=2.0)
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Fat Type:</p>'
st.markdown(new_title, unsafe_allow_html=True)
fat=st.selectbox("",["Low Fat","Regular"])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed   ; font-size: 20px;">Visibility of the brand:</p>'
st.markdown(new_title, unsafe_allow_html=True)
visible= st.slider("",min_value=0.0,max_value=1.0,value=0.1)
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Item Categories</p>'
st.markdown(new_title, unsafe_allow_html=True)
types=st.radio("",['Fruits and Vegetables', 'Snack Foods', 'Household', 'Frozen Foods', 'Dairy', 'Canned', 'Baking Goods', 'Health and Hygiene', 'Soft Drinks', 'Meat', 'Breads', 'Hard Drinks', 'Others', 'Starchy Foods', 'Breakfast', 'Seafood'])
st.write("\n")


new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">MRP of the item:</p>'
st.markdown(new_title, unsafe_allow_html=True)
mrp=st.number_input("",value=1.0)
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed ; font-size: 20px;">Outlet Identifier code:</p>'
st.markdown(new_title, unsafe_allow_html=True)
out_id=st.selectbox("",['OUT027', 'OUT013', 'OUT046', 'OUT049', 'OUT035', 'OUT045', 'OUT018', 'OUT017', 'OUT010', 'OUT019'])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed   ; font-size: 20px;">Outlet Est. Year:</p>'
st.markdown(new_title, unsafe_allow_html=True)
year_1=st.slider("",value=(1970,2020))
year=2021-year_1
st.write("\n")


new_title = '<p style="font-family:sans-serif; color:DarkRed   ; font-size: 20px;">Outlet type (size of export):</p>'
st.markdown(new_title, unsafe_allow_html=True)
ot=st.selectbox("",['Small','Medium','High'])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Output Location Type</p>'
st.markdown(new_title, unsafe_allow_html=True)
oloc=st.radio("",['Tier 1', 'Tier 2', 'Tier 3'])
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:DarkRed  ; font-size: 20px;">Store Type</p>'
st.markdown(new_title, unsafe_allow_html=True)
os=st.selectbox("",['Supermarket Type1', 'Grocery Store', 'Supermarket Type3', 'Supermarket Type2'])
st.write("\n")

means=[12.813419570574444,0, 0.06613202877895127,0, 140.9927819781768,0, 23.168133286401503,0,0,0]
stds=[4.226992409024986,0, 0.05159479525696192,0, 62.271413051361094,0, 8.37126926612472,0,0,0]

# 0 in means and stds list are appended only for easier understanding when used in for loop below

dic={'Baking Goods': 6,
 'Breads': 10,
 'Breakfast': 14,
 'Canned': 5,
 'Dairy': 4,
 'Frozen Foods': 3,
 'Fruits and Vegetables': 0,
 'Grocery Store': 1,
 'Hard Drinks': 11,
 'Health and Hygiene': 7,
 'High': 2,
 'Household': 2,
 'Low Fat': 0,
 'Meat': 9,
 'Medium': 0,
 'OUT010': 8,
 'OUT013': 1,
 'OUT017': 7,
 'OUT018': 6,
 'OUT019': 9,
 'OUT027': 0,
 'OUT035': 3,
 'OUT045': 5,
 'OUT046': 4,
 'OUT049': 2,
 'Others': 12,
 'Regular': 1,
 'Seafood': 15,
 'Small': 1,
 'Snack Foods': 1,
 'Soft Drinks': 8,
 'Starchy Foods': 13,
 'Supermarket Type1': 0,
 'Supermarket Type2': 3,
 'Supermarket Type3': 2,
 'Tier 1': 2,
 'Tier 2': 1,
 'Tier 3': 0}

trees=pickle.load(open("treex.pkl","rb"))
par=[wei,fat,visible,types,mrp,out_id,year,ot,oloc,os] # parameters for the model

for i in range(len(par)): #label encoding and scaling the parameters
  if i in [0,2,4,6]:
    par[i]=(par[i]-means[i])/stds[i]

  else:
    par[i]=dic[par[i]]
st.write("\n")

new_title = '<p style="font-family:sans-serif; color:GREEN; font-size: 30px;">PREDICT THE SALES</p>'
st.markdown(new_title, unsafe_allow_html=True)
if st.button("Predict"):
    pred=trees.predict([par])
    
    st.write("The Outlet Sales Value is:",pred[0])

