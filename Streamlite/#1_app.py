import pandas as pd 

import streamlit as st 



##Title of the app

st.title("Mindlyst.ai")



##Taking the text input from the user



name=st.text_input("Please enter the name")


##wrting the some text 


if name :
    st.write(f"Hello {name}")
    st.write("Welcome to the Mindlyst.ai app  .This  is the revolutionary app that will help you to analyze  your mind based on some morphological movements of yours with direct physical interconvection. ")

  
##Sliders in the streamlit 


age=st.slider("Please enter the age",1,100)

if age>18:
    st.write("You are an adult")
    
else:
    st.write("You are a child")
    
    
    

##Selection box in the streamlit 

language=st.selectbox("Please select the language",["Python","Java","C++","C#","Ruby","R","Scala","Julia","Swift","Kotlin","Go","Rust","Perl","PHP","Javascript","Typescript","HTML","CSS","SQL","Dart","Haskell","Groovy","Shell","PowerShell","Objective-C","Matlab","Visual Basic","Assembly","Lua","Delphi","COBOL","Fortran","Ada","Lisp","Scheme","Prolog","F#","Erlang","Clojure","Racket","Smalltalk","Tcl","Verilog","VHDL","LabVIEW","ABAP","Apex","PL/SQL","Transact-SQL","PL/pgSQL","T-SQL","Pascal","Logo","Ada","D","Dylan","Eiffel","Elixir","Elm","Forth","Fantom","Factor","Falcon"])

if language:
    
    st.write(f"{name} ,Your selected language is {language} and you have proficiency in {language} language")
   

 
##Building the file uploader in the streamlit


upload=st.file_uploader("Please upload the file",type=['csv','txt','xls','xlsx'])

if upload:
    
    uploaded_file=pd.read_csv(upload)
    
    
    st.write(f"File {upload.name} has been uploaded successfully")
    
    st.write(uploaded_file)
    
    



st.write("Some data work ")




##Adding the some data and dataframes to the app 


data =pd.read_csv(r"C:\PROJECTS\Mindlyst\Mindlyst.ai\speech_data_cleaned_processed.csv")
st.write(data)




##Drawing the plots on the websites 

st.line_chart(data['tempo'])
st.bar_chart(data['tempo'])





