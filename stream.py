from turtle import color, width
import streamlit as st
import pandas as pd
from PIL import Image
from sklearn.preprocessing import StandardScaler as scaler
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

data = pd.read_csv('./last.csv')


st.markdown("<h1 style='text-align: center; color: blue;'>time to remember TITANIC!...</h1>", unsafe_allow_html=True)
img = Image.open("calorie.png")
st.image(img, width=600)


images = st.sidebar.radio('EDA and FE', options=('yes', 'no'))
if images == 'yes':

    # fig, ax = plt.subplots(figsize=(20,20))
    # ax = sns.heatmap(data.corr(),vmin=-1, vmax=1, annot=True)
    # st.write(fig)

    st.markdown("<h3 style='text-align: center; color: blue;'>The correlation between features!</h3>", unsafe_allow_html=True)
    img = Image.open("first.png")
    st.image(img, width=800)


    st.markdown("<h3 style='text-align: center; color: blue;'>The correlation between features!!ccccc</h3>", unsafe_allow_html=True)
    img5 = Image.open("second.png")
    st.image(img5, width=800)


    st.markdown("<h3 style='text-align: center; color: blue;'>The correlation between features!!!</h3>", unsafe_allow_html=True)
    img2 = Image.open('third.png')
    st.image(img2, width=800)
    
 



try: 
    user_input = st.sidebar.radio(
        label="Let's check your Burning calories while your doings!",
        options=("No",'Yes'))

    if user_input == 'Yes':

        weight = st.text_input("Enter your weight! (in kg) \n")

        height = st.text_input("height! (in sm) \n")
      
        predict1 = st.button("predict")
        #pred = models()
        pred = 'walking'
        if predict1:

            if pred == 'walking':
                # """"
                # Multiply your body weight in kilograms by 0.035. Eg. 0.035 x 60 = 2.1
                # Square your velocity (or speed) in metres per second by multiplying it by itself. Eg. 1.4 x 1.4 = 1.96
                # Divide the result by your height in metres. Eg.1.96 ÷ 1.6 = 1.225
                # Add your first answer and your second answer E.g. 2.1 + 1.225 = 3.325.
                # Multiply the result by 0.029. E.g. 3.325 x 0.029 = 0.096425
                # Multiply the result by your body weight. E.g. 0.096425 x 60 = 5.7855

                # """
                a = int(weight) * 0.035
                b = 100/int(height)
                c = a+b
                d = c*0.029
                e = d*int(weight)

                st.markdown(f"<h3 style='text-align: center; color: blue;'>You are wasting  {round(e, 2)} calories in per minute</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='text-align: center; color: blue;'>Please, stay at home!</h3>", unsafe_allow_html=True)

except ValueError:
    st.error('Please enter valid data type!')

about = st.sidebar.button("contributors")
if about:
    st.title("Fayyozjon Usmonov")
    st.markdown("<h1 style='text-align: center; color: blue;'>Thanks for your attention!</h1>", unsafe_allow_html=True)

