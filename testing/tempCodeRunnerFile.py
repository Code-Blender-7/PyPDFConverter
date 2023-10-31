for index, file in enumerate(imgList): # Start from first item
#     print("Adding image",index+1,"of",imgCount)
#     img = fitz.open(file) # open pic as doc
#     rect = img[0].rect # Get dimensions of image
#     pdfbytes = img.convert_to_pdf()
#     img.close()
    
#     imgPDF = fitz.open("pdf", pdfbytes)
#     page = doc.new_page(width = rect.width, height = rect.height) # Create PDF page with img dimensions
#     page.show_pdf_page(rect, imgPDF, 0) # Fill page with image
