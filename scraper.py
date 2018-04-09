# Import necessary libraries.

import pandas as pd
import csv

# For instructions on installing and using the boilerpipe wrapper, look here: https://github.com/misja/python-boilerpipe

from boilerpipe.extract import Extractor
import ssl

# Import the csv of the URLs and place it into a Pandas dataframe.

df = pd.read_csv()

# Convert URLs dataframe into a list.

urls = df['URL'].tolist()

# Disables SSL certification requirements.

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Loop through the pages, download their HTML/text content, and write to file.

for url in urls:
    coumn
    try:
        extractor = Extractor(extractor='ArticleExtractor', url='http://www.' + url)
        extracted_text = extractor.getText()
    except:
        pass
    with open('websitestextarticle.txt', 'a') as webtextfile:
        webtextfile.write(extracted_text)
