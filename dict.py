import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict2 = dict(name = "John", age = 36, country = "Norway")


#
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  st.write("Yes, 'model' is one of the keys in the thisdict dictionary") 



#

st.write(thisdict)

st.write(thisdict2)
# Help: st.write(type(thisdict))
# Show number of entries: st.write(len(thisdict))
