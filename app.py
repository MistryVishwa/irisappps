# import streamlit as st
# st.title("Iris Prediction")
# import pickle
# model=pickle.load(open("model_svm.pkl","rb"))
# sl=st.slider("Sl",2.0,10.0)
# sw=st.slider("Sw",2.0,10.0)
# pl=st.slider("pl",2.0,10.0)
# pw=st.slider("pw",2.0,10.0)
# if st.button("Predict"):
#     st.success(model.predict([[sl,sw,pl,pw]]))

import streamlit as st
import pickle

st.title("Iris Prediction")

model = pickle.load(open("model_svm.pkl", "rb"))

sl = st.slider("Sepal Length", 2.0, 10.0)
sw = st.slider("Sepal Width", 2.0, 10.0)
pl = st.slider("Petal Length", 2.0, 10.0)
pw = st.slider("Petal Width", 2.0, 10.0)

if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    st.success(f"Prediction: {prediction[0]}")
