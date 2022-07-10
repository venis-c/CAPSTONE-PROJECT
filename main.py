import streamlit as st

import pickle
import numpy as np
import base64

#background Image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('mobile_image1.jpg')

# import the model
reg = pickle.load(open('reg.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

#title
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    color:Red;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font"><strong>Mobile Price Predictor</strong></p>', unsafe_allow_html=True)

#st.title('Mobile Price Predictor')

# battery
Battery_Power = st.selectbox('Battery_Power',df['Battery_Power'].unique())

# rom
ROM = st.selectbox('ROM',df['ROM'].unique())

#primary cam
Primary_Cam = st.selectbox('Primary_Cam',df['Primary_Cam'].unique())

#Selfi_Cam
Selfi_Cam = st.selectbox('Selfi_Cam',df['Selfi_Cam'].unique())

#ram
RAM = st.selectbox('RAM',df['RAM'].unique())

#size
Mobile_Size = st.selectbox('Mobile_Size',df['Mobile_Size'].unique())

if st.button('Predict Price'):

    # query
    query = np.array([Battery_Power,ROM,Primary_Cam,Selfi_Cam,RAM,Mobile_Size])

    query = query.reshape(1,6)
    st.title("The predicted price of this configuration is " + str(int(reg.predict(query)[0])))
