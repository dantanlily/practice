#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:02:34 2023

@author: dantan
"""

import requests
from bs4 import BeautifulSoup
import gensim
from summa.summarizer import summarize
import pandas as pd
#from gensim.summarization import summarize

# In[]
# Small example
# Request Website Specific Url
url = "https://www.reuters.com/markets/us/banking-woes-fed-keep-investors-edge-nervous-us-stock-market-2023-03-25/"
response = requests.get(url)

# Web content
soup = BeautifulSoup(response.content, "html.parser")
article_text = ""
for p in soup.find_all("p"):
    article_text += p.get_text().strip() + " "

# summary ratio is 0.1
summary = summarize(article_text, ratio=0.1,split=True)

for sentence in summary[:3]:
    print(sentence)

# In[]
'''
Example News from Reuters European Markets
"https://www.reuters.com/markets/europe/"
The content may change in real time based on live information.

'''
import requests
from bs4 import BeautifulSoup
import re
from summa.summarizer import summarize
import re
#Tokenization of DataFiles
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Define the main website URL
main_url = "https://www.reuters.com/markets/europe/"

# Send a request to the main URL
r = requests.get(main_url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(r.content, "html.parser")

# Find all the links to sub-pages on the main website
subpage_links = []
#r"{0}.+".format(main_url)
for link in soup.find_all("a", href=re.compile(r"/markets/europe/.+")):
    subpage_links.append(link.get("href"))

# Example subpage_url is https://www.reuters.com/markets/europe/european-stocks-rebound-banking-jitters-ease-2023-03-27/
# Visit each sub-page and extract relevant sentences
article_text={}
for subpage_link in subpage_links:
    # Construct the sub-page URL
    subpage_url = f"https://www.reuters.com{subpage_link}"
    
    # Send a request to the sub-page URL
    r = requests.get(subpage_url)
    
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(r.content, "html.parser")
    
    # Extract the article text which has percentage numbers
    for paragraph in soup.find_all("p"):
        text=paragraph.text
        #print(text)
        pattern = r'\d+(\.\d+)?%'
        matched_sentences = []
        matches = re.findall(pattern,text)
        # Add sentences to article text if there's a pattern match
        if matches:
            article_text[text]=subpage_url
        #article_text.append(text)
    
    df = pd.DataFrame.from_dict(article_text, orient='index')
    df.reset_index(drop=False,inplace=True)
    df.columns=['number sentences','url']
    df=df[['url','number sentences']]

    

df.to_excel('European_main_url_contents.xlsx',index=False)


# In[]
'''
Example News from Reuters All Markets - 
The content may change in real time based on live information.
"https://www.reuters.com/markets/"

'''
import requests
from bs4 import BeautifulSoup
import re
from summa.summarizer import summarize
import re
#Tokenization of DataFiles
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Define the main website URL
main_url = "https://www.reuters.com/markets/"

# Send a request to the main URL
r = requests.get(main_url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(r.content, "html.parser")

# Find all the links to sub-pages on the main website
subpage_links = []
#r"{0}.+".format(main_url)
for link in soup.find_all("a", href=re.compile(r"/markets/.+")):
    subpage_links.append(link.get("href"))

# Example subpage_url is https://www.reuters.com/markets/europe/european-stocks-rebound-banking-jitters-ease-2023-03-27/
# Visit each sub-page and extract relevant sentences
article_text={}
for subpage_link in subpage_links:
    # Construct the sub-page URL
    subpage_url = f"https://www.reuters.com{subpage_link}"
    
    # Send a request to the sub-page URL
    r = requests.get(subpage_url)
    
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(r.content, "html.parser")
    
    # Extract the article text which has percentage numbers
    for paragraph in soup.find_all("p"):
        text=paragraph.text
        #print(text)
        pattern = r'\d+(\.\d+)?%'
        matched_sentences = []
        matches = re.findall(pattern,text)
        # Add sentences to article text if there's a pattern match
        if matches:
            article_text[text]=subpage_url
        #article_text.append(text)
    
    df = pd.DataFrame.from_dict(article_text, orient='index')
    df.reset_index(drop=False,inplace=True)
    df.columns=['number sentences','url']
    df=df[['url','number sentences']]

    
df.to_excel('Markets_main_url_contents.xlsx',index=False)


# In[] Codes tried Archive

  # print(f"Sub-page URL: {subpage_url}")
  # print("Relevant sentences:")
  # for sentence in relevant_sentences:
  #     print(sentence)
  # print("\n")

# # To be updated Extract relevant sentences using NLP or machine learning
# sentences = re.findall(r"[A-Z][^\.!?]*\d+(?:\.\d+)?%", text)
# if len(sentences)!=0:
#     article_text.append(sentences)
# #article_text += paragraph.text


  
# relevant_sentences = []
# #for sentence in summarize(article_text).split("."):
    
# for sentence in article_text.split("."):
#     print(sentence)
#     if re.search(r"\d+\.\d+%", sentence) or re.search(r"\d+", sentence):
#         relevant_sentences.append(sentence.strip())
        

# relevant_sentences.append(main_interested_text(article_text))


# text='Healthcare stocks (.SXDP) were the top gainers in Europe, rising 1.9%.Novartis (NOVN.S) climbed 7.7% after the Swiss drugmaker said its Kisqali breast cancer drug had been shown to cut the risk of recurrence in women who were diagnosed at an early stage.European stocks are looking to end the first quarter of the year with gains, \
#     buoyed by signs of economic resilience and hopes that central banks are near the end of their tightening cycles. '

# def main_interested_text(text):
#     # Getting percentage change (for main underlyings)
#     sentences = sent_tokenize(text)
#     number_sentences = []
#     for sentence in sentences:
#         if re.search(r'\d+(\.\d+)?%', sentence) is not None:
#             number_sentences.append(sentence)
#         # main content 
#         main_content = []
#         for sentence in number_sentences:
#             main_content.append(re.sub(r'\d+(\.\d+)?%', '', sentence))
#          # print("numbers content：")
#          # for sentence in number_sentences:
#          #     print(sentence)
         
#          # print("main content：")
#          # for sentence in main_content:
#          #     print(sentence)
#     return main_content



# def main_number(text):
#     # Use NLTK to do tokenization
#     tokens = nltk.word_tokenize(text)
#     # Search pattern
#     pattern = r'\d+(\.\d+)?%'
#     matches = re.findall(pattern, text)
    
#     # Ouput matches and the most close vocabulary
#     for i, token in enumerate(tokens):
#         for match in matches:
#             if match in token:
#                 print(f"{token} {tokens[i+1]}")
       

# main_number(main_interested_text(text)[0])





