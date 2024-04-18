#!/usr/bin/env python
# coding: utf-8

# In[4]:



# extractor.py
import re
from reader import read_pdf

class PDFExtractor:
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.line_item_pattern = re.compile(r'^line \d+\.\s+(\d+)$', re.IGNORECASE)

    def _extract_values_from_file(self, pdf):
        values = []
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                match = self.line_item_pattern.match(line)
                if match:
                    values.append(int(match.group(1)))
        return values

    def extract_and_sum_from_each_file(self):
        file_sums = {}
        for filepath in self.filepaths:
            pdf = read_pdf(filepath)
            if pdf:
                values = self._extract_values_from_file(pdf)
                file_sums[filepath] = sum(values)
                pdf.close()
        return file_sums


