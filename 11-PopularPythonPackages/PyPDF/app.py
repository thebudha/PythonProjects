import PyPDF2 as pypdf2

with open(first_pdf, 'rb') as file:
    reader = pypdf2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = pypdf2.PdfFileWriter()
    writer.addPage(page)
    with open('rotated.pdf', 'wb') as output:
        writer.write(output)
