import PyPDF2
import sys

main_file = sys.argv[1]
watermark_file = sys.argv[2]

template = PyPDF2.PdfReader(open(main_file, 'rb'))
watermark = PyPDF2.PdfReader(open(watermark_file, 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('watermarked.pdf', 'wb') as file:
        output.write(file)
