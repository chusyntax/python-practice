import PyPDF2
import sys

# with open('dummy.pdf', 'rb') as file: # Use rb for read binary

inputs = sys.argv[1:]  # Used so you can get everything after the given index


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)
