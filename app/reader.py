#!/usr/bin/env python
# coding: utf-8

# # Creating the Python Library Files

# In[2]:


import pdfplumber

def read_pdf(path):
    """
    Open a PDF and convert it to a Python object using pdfplumber.
    
    Parameters:
        path (str): The path to the PDF file.
        
    Returns:
        pdfplumber.PDF: An object representing the opened PDF.
    """
    try:
        return pdfplumber.open(path)
    except Exception as e:
        print(f"Failed to read PDF: {str(e)}")
        return None


# In[ ]:





# In[ ]:





# In[ ]:




