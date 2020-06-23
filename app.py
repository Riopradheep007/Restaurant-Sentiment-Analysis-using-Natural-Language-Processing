#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:24:11 2020

@author: kpr
"""

import numpy as np
import pickle5
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer




pickle_in = open("restaurent_reviews.pkl","rb")
classifier=pickle5.load(pickle_in)

cv = pickle5.load(open('cv-transform.pkl','rb'))




def predict(sample_review):

  temp = cv.transform([sample_review]).toarray()
  return classifier.predict(temp)

        
        



def main():
   
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Restaurant Sentiment Analysis </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sample_review= st.text_area("please enter your reviews")

   
    if st.button("Predict"):
        
        if predict(sample_review):
            st.success("Hey you have a POSITIVE review")
        else:
            st.success("oops! you have a NEGATIVE review")
    if st.button("About"):
        st.text("by pradheep")
        st.text("Linked in:https://www.linkedin.com/in/pradheep-m-24510a173")
        st.text("github:https://github.com/Riopradheep007")
        st.text("Kaggle:https://www.kaggle.com/pradheeprio")
        
if __name__=='__main__':
    main()