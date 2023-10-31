# Creating PDF from text

import fitz
doc = fitz.open()
page = doc.new_page()
paragraph = fitz.Point(50, 72)

text = ["Bun", 
        "Bread",
        "Carrot"]

TXT_INSERT_CONFIG = page.insert_text(paragraph,
                                     text,
                                     fontname = "helv",
                                     fontsize = 11,
                                     rotate = 0
                                     )

print("%i lines printed on page %i" % (TXT_INSERT_CONFIG, page.number))

doc.save("text.pdf")


# import fitz
# doc = fitz.open("testing/sample.pdf")
# out = open("output.txt", "wb")
# for page in doc:
#         text = page.get_text().encode("utf8")
#         print(text)


# # out.close()