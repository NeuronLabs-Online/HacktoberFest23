# import libraries

import pandas as pd
import streamlit as st
import altair as alt  # for writing bar chart
from PIL import Image

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/2961778.jpg");
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.write("""
 # DocNet's BioInformatics""")

# Page image
image = Image.open('dna-logo.jpeg')
st.image(image, use_column_width=True)

# Title
# one hash means h1, two means h2 and so on...
# *** is underline
st.write("""
 # DNA Nucleotide Count Web App

    This app counts the nucleotide composition of every DNA!

    ***
""")

# header
st.header("## Enter DNA sequence")

# Input
sequence_input = ">DNA Query\n"

# area for input, first parameter is label
sequence = st.text_area("Sequence input:", sequence_input,height=250)

# split lines into array of lines
sequence = sequence.splitlines()

# skip the first line as it is the title (>DNA Query)
sequence = sequence[1:]

# make it into a string
sequence = ''.join(sequence)

# another line
st.write("""
***
""")

# prints the input DNA sequence
st.header('# INPUT (DNA QUERY)')
sequence

# prints the DNA nucleotide count
st.header('# OUTPUT (DNA Nucleotide Count)')

# print dictionary
st.subheader('# Processing dictionary')

# a function for making the DNA nucleotide string into a dictionary
# key is letter, value is count of letters
def DNA_nucleotide_count(sequence):
    d = dict([
        ('A',sequence.count('A')),
        ('T',sequence.count('T')),
        ('G',sequence.count('G')),
        ('C',sequence.count('C'))
    ])

    return d

# calling the function
DNADict = DNA_nucleotide_count(sequence)

label = list(DNADict)
values = list(DNADict.values())

# outputs dictionary
DNADict

# print counts in sentences
st.subheader('# Processing text')
st.write('There are '+str(DNADict['A'])+' adenine (A)')
st.write('There are '+str(DNADict['T'])+' thymine (T)')
st.write('There are '+str(DNADict['G'])+' guanine (G)')
st.write('There are '+str(DNADict['C'])+' cytosine (C)')

# 3. Display dataframe
st.subheader('# Displaying dataframe')

# without renaming
df = pd.DataFrame.from_dict(DNADict, orient='index')

# after renaming ( first column )
df = df.rename({0:'count'},axis='columns')

# reset index column and add another index column at the left
df.reset_index(inplace=True)

# rename index to nucleotide
df = df.rename(columns={'index':'nucleotide'})

# output the table
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('# Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide', # x-axis
    y='count', # y-axis 
)

# edit width of bar chart
p = p.properties(
    width = alt.Step(80)
)

st.write(p)