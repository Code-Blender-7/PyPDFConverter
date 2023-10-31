# Comvert images into PDF

import os, fitz, pathlib

doc = fitz.open()
imgDir = os.path.join(os.path.dirname(__file__))
dirList = os.listdir(pathlib.Path(__file__).parent.resolve()) # locate program directory
imgList = [items for items in dirList if os.path.splitext(items)[1] == ".jpeg"] #   
        
imgCount = len(imgList)
print(imgCount, imgList, os.path.dirname(__file__))

for file in enumerate(imgList): # Start from first item
    img = fitz.open(imgDir, file) # open pic as doc
    rect = img[0].rect # Get dimensions of image
    pdfbytes = img.convert_to_pdf()
    img.close()
    
    imgPDF = fitz.open("pdf", pdfbytes)
    page = doc.new_page(width = rect.width, height = rect.height) # Create PDF page with img dimensions
    page.show_pdf_page(rect, imgPDF, 0) # Fill page with image

    
doc.save(imgDir, "output_1.pdf")    
 