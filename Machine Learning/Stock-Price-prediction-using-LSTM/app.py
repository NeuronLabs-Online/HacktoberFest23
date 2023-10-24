import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import yfinance as df #importing the dataset
from pandas_datareader import data as pdr 
import streamlit as st



st.title('Stock Prediction using LSTM')

user_input = st.text_input('Enter Stock Ticker', 'PG')

df.pdr_override()

df = pdr.get_data_yahoo(user_input, start='2010-1-1')

# describing data
st.subheader('Data from 2010 - 2023')
st.write (df.describe())

# visualisations 

st.subheader('Closing Price vs Time chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100, 'g')
plt.plot(ma200, 'b')
plt.plot(df.Close, 'r')
st.pyplot(fig)

# splitting data into training and testing

from sklearn.model_selection import train_test_split
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70) : int(len(df))])

print(data_training.shape)
print(data_testing.shape)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)



#Load my model
model = load_model('keras_model.h5')

#Testing Part
past_100_days = data_testing.tail(100)

final_df = pd.concat([past_100_days,data_testing], ignore_index=True)

input_data = scaler.fit_transform(final_df)

x_test =[]
y_test =[]

for i in range(100,input_data.shape[0]):
  x_test.append(input_data[i-100: i])
  y_test.append(input_data[i, 0])

x_test,y_test = np.array(x_test),np.array(y_test)
y_predicted = model.predict(x_test)

scaler = scaler.scale_

scale_factor = 1/scaler[0]
y_predicted = y_predicted*scale_factor
y_test = y_test*scale_factor

st.subheader('Predictions vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)


