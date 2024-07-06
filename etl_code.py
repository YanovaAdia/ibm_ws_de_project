import glob
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET 
from datetime import datetime

log_file = "log_file.txt" 
target_file = "final_data.csv" 

def extract_from_csv(filename):
    df = pd.read_csv(filename)
    return df

def extract_from_json(filename):
    df = pd.read_json(filename, lines=True)
    return df

def extract_from_xml(filename):
    df = pd.DataFrame(columns=['name', 'height', 'weight'])
    tree = ET.parse(filename)
    root = tree.getroot()

    for person in root:
        name = person.find('name').text
        height = float(person.find('height').text)
        weight = float(person.find('weight').text)
        df.loc[len(df)] = {'name':name, 'height':height, 'weight':weight}
    
    return df

def extract():
    extracted_df = pd.DataFrame()

    for csv in glob.glob('/data_source/*.csv'):
        extracted_df = pd.concat([extracted_df, extract_from_csv(csv)], ignore_index=True)

    for json in glob.glob('/data_source/*.json'):
        extracted_df = pd.concat([extracted_df, extract_from_json(json)], ignore_index=True)
    

    for xml in glob.glob('/data_source/*.xml'):
        extracted_df = pd.concat([extracted_df, extract_from_xml(xml)], ignore_index=True)

    return extracted_df

def transform(data):
    data['height'] = np.round(data.height * 0.0254,2)
    data['weight'] = np.round(data.weight * 0.45359237,2)
    
    return data

def load_data(transformed_data):
    transformed_data.to_csv(target_file)

def logging_time(msg):
    time_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(time_format)
    with open(log_file, 'a') as log:
        log.write(f'{timestamp} : {msg} \n')