import streamlit as st
import pandas as pd
#import numpy as np
import plost
from PIL import Image
import streamlit as st
import streamlit_authenticator as stauth
import requests
from bs4 import BeautifulSoup
import re


st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

names = ['Yasrizal','ANALYST JAMBI']
usernames = ['yz','AJ']
passwords = ['38','38']

hashed_passwords = stauth.Hasher(passwords).generate()
basewidth = 150


#st.image('D:/image_web/siber.png')

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('ANALYST SIBER POLDA JAMBI\nWELCOME TO YZ SYSTEM')


if authentication_status:
    
    st.write('Welcome *%s*' % (name))
    #st.title('Some content')

    authenticator.logout('Logout')
    st.write('''
    Copyright by © YZ Tech.''')



    menu = ["HOME", "FIND CELL ID"] #menu
    choice = st.sidebar.selectbox("Menu", menu) #sidebar menu

    if choice == "FIND CELL ID":
        MCC = st.number_input("MCC", 510)
        MNC = st.number_input("MNC", 10)
        LAC = st.number_input("LAC", 99)
        CID = st.number_input("CID", 99)
        mcc = MCC
        mnc = MNC
        lac = LAC
        cid = CID
        ceklok = st.button("FIND LOCATION")
        if ceklok:
            with st.spinner('Wait for it...'):
                MCC = str(MCC)
                MNC = str(MNC)
                LAC = str(LAC)
                CID = str(CID)
                url = "https://us1.unwiredlabs.com/v2/process.php"
                payload = ('{"token": "pk.512e5a933431dbd79715f44aaeffb03e","radio": "gsm","mcc": ') + MCC + (',"mnc": ') + MNC + (',"cells": [{"lac": ') + LAC + (',\"cid\": ') + CID + ('}],\"address\": 1}')
                response = requests.request("POST", url, data=payload)
                data = response.text

                a = response.text
                b = str(a)
                lat = re.findall(r"lat.+?,",a)
                long = re.findall(r"lon.+?,",a)
                gab = lat + long
                gab = str(gab)
                gab = gab.replace('lat','')
                gab = gab.replace('":','')
                gab = gab.replace("['","")
                gab = gab.replace("', 'lon","")
                gab = gab.replace(",']","")
                gab = 'https://www.google.com/maps/place/' + gab
                gab = 'Location Base On Cell Track = ' + gab
                osint = '\nOpen Source (OSINT) from yz SIBER POLDA JAMBI'
                b = b.replace('status','')
                b = b.replace('{','LIMIT QUOTE = ')
                b = b.replace(':','')
                b = b.replace(',','')

                b = b.replace('""','')
                b = b.replace('"okbalance"','')
                b = b.replace('"balance"','')
                b = b.replace('"lat"','\nLatitude : ')
                b = b.replace('"lon"','\nlongitude : ')

                b = b.replace('"accuracy"','\nAccuracy : ')
                b = b.replace('status','')
                b = b.replace('"address',' Meters\nAddress : ')

                 
                c = str(a)
                c = c.replace('lat":','Position Base ON Cell Track = https://www.google.com/maps/place/')
                c = c.replace(',"lon":',',')
                c = c.replace(',"','\n')
                c = c.replace('{"status":"ok"','')
                c = c.replace('balance":','LIMIT QUOTE : ')
                c = c.replace('accuracy":','Accuracy/M : ')
                c = c.replace('address":"','Address : ')
                c = c.replace('"}','')

                data = '\nDatabase From Locator Base Tower\n'

                hasil = '\n' + data + b + gab + osint
                #print(data)
                #hasil = 
                #print(b)
                #print(gab)
                #print(osint)

                st.success(f"Yz System Information\n {hasil}")
        
        elif authentication_status == False:
            st.error('Username/password is incorrect')
# Page setting



# Row A
#a1, a2, a3 = st.columns(3)
#a1.image(Image.open('D:/btsdf/yz.png'))
#a2.image(Image.open('D:/image_web/anb.png'))
#a3.image(Image.open('D:/image_web/Maltego2.png'))

# Row B
#b1, b2, b3, b4 = st.columns(4)
#b1.image(Image.open('D:/image_web/ibm.png'))
#b2.image(Image.open('D:/image_web/django.png'))
#b3.image(Image.open('D:/image_web/python.png'))
#b4.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))

