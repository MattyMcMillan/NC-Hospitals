#IMPORT PACKAGES 
import geopandas as gpd
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

nc_medical_facilities = gpd.read_file(r'C:\Users\mmcmillan\OneDrive - PulteGroup\Documents\Web Application\Layers\NC Medical Facilties\Medical_Facilities.shp')
print(nc_medical_facilities.columns)

ers = nc_medical_facilities.loc[nc_medical_facilities['STYPE'] == 'Hospital']

ers = ers[['FACILITY','FCITY','FCOUNTY','LICENSEE','STYPE','geometry']]

ers = ers.rename(columns ={'FACILITY':'Facility', 'FCITY':'City', 'FCOUNTY':'County','LICENSEE':'Licensee','STYPE':'Category'})

ers.to_file(r'C:\Users\mmcmillan\OneDrive - PulteGroup\Documents\Web Application\Layers\NC Medical Facilties\NC Hospitals.shp')