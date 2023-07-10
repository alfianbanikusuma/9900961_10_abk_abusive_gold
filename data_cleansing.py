import re
import pandas as pd

abusive = pd.read_csv('C:/Users/Bani/binar-data-science/binar-data-science/Challenge Documents/abusive.csv', encoding='latin-1')
df_newkamusalay = pd.read_csv('C:/Users/Bani/binar-data-science/binar-data-science/Challenge Documents/new_kamusalay.csv', encoding='latin-1')

list_of_abusive = abusive['ABUSIVE'].tolist()

new_df_newkamusalay = {}
for k,v in df_newkamusalay.values:
    new_df_newkamusalay[k] = v


def processing_abusive_acronym(input_text):
    new_abusive_list = [] 
    new_new_abusive_list = [] 
    text = input_text.split(" ") 
    for word in text: 
        if word in list_of_abusive : 
            continue 
        else:
            new_abusive_list.append(word) 
   
    for word in new_abusive_list:
        new_word = new_df_newkamusalay.get(word, word)
        new_new_abusive_list.append(new_word)
    
    text = " ".join(new_new_abusive_list)
    return text


def text_cleaning_other(input_text):
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', 'EMAIL', input_text)
    text = text.lower() # jadikan lowercase semua
    text = re.sub(r'[^\w\s]', '', text) # hapus semua punctuation (tanda baca)
    text = text.replace(" 62"," 0")
    text = re.sub(r"\b\d{4}\s?\d{4}\s?\d{4}\b", "NOMOR_TELEPON", text) #ganti nomor telepon ke kata 'NOMOR_TELEPON'
    text = text.replace("user"," ")
    text = text.replace("url"," ")
    text = text.strip()
    text = re.sub(r'x[a-z{1}][0-9,{2}]', " ",text)
    text = re.sub(r'x[0-9,{2}][a-z{1}]', " ",text)
    text = re.sub(r'(.)\1+', r'\1', text)
    text = re.sub(r'(x98)|(x84)|(x86)|(x9xa[a-z])|(x82)|(x8[0-9])|(x9[0-9])|x|(dx9)|(xc[a-z])|(dxcexafxce)|(ð)', " ",text)
    text = processing_abusive_acronym(text)
    
    return(text)
