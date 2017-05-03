# Get the epub from e.g. here https://play.google.com/store/books/details/Robin_Hanson_The_Age_of_Em?id=Un0oDAAAQBAJ
# (Or use the free high-level summary at ageofem.com)

import os


# Use Calibre's excellent ebook parser:
source = "em.txt"
os.system("ebook-convert em.epub " + source)



# 'Assumptions' are just claims without dependencies (within the text).
