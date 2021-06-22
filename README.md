# Restaurant-Sentiment-Analysis-using-Natural-Language-Processing

## Table of content
   - [Demo](#Demo)
   - [Overview](#Overview)
   - [Motivation](#Motivation)
   - [Technical Aspect](#Technical-Aspect)
   - [Installation](#Installation)
   - [Deployement On Heroku](#Deployement-On-Heroku)
   - [Run](#Run)
  
 
 ## Demo

 ####  Link:  https://restaurant-sentiment-analysis.herokuapp.com/

![streamlit-app-2020-06-27-17-06-81 webm](https://user-images.githubusercontent.com/46066018/85922403-94dcd500-b8a0-11ea-8fc5-2184a713b953.gif)

## Overview

   This is a Restaurant Sentiment Analysis Streamlit app this  was a machine learning model takes input as a text and predict output is a
**positive review** or  **negative review**

## Motivation
   What to do when you are at home due to this pandemic situation? I started to learn Machine Learning model to get most out of it. I came to know mathematics behind all supervised models. Finally it is important to work on application (real world application) to actually make a difference.

## Technical Aspect

This project is divided into two part:

 1. Training the model using machine learning.
       
 2. Building and hosting a Streamlit web app on Heroku
     - User have to enter their reviews in the text area.
     - After entered  the review displayed the output the review is Positive or Negative.
     
## Installation

The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command.


    pip install -r requirements.txt
    
## Deployement On Herouku

 Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.
 
 
[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

     
## Run 
   TO run this model In **Linux/Mac** open Terminal.If you are  **Windows user** open your command prompt.Run the command
   
    streamlit run app.py
 
