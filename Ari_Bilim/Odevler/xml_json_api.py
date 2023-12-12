import requests
import streamlit as st
from urllib.request import urlopen
import xml.etree.ElementTree as et


url = "https://www.tcmb.gov.tr/kurlar/today.xml"

data = et.ElementTree(file=urlopen(url))

root = data.getroot()

for kur in root:
  isim = kur[1].text
  fiyat = float(kur[3].text)
  kurlar[isim] = fiyat
