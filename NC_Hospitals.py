#IMPORT PACKAGES 
import geopandas as gpd
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

nc_medical_facilities = gpd.read_file(r'file_location')
print(nc_medical_facilities.columns)

ers = nc_medical_facilities.loc[nc_medical_facilities['STYPE'] == 'Hospital']

ers = ers[['FACILITY','FCITY','FCOUNTY','LICENSEE','STYPE','geometry']]

ers = ers.rename(columns ={'FACILITY':'Facility', 'FCITY':'City', 'FCOUNTY':'County','LICENSEE':'Licensee','STYPE':'Category'})

ers.to_file(r'file location')