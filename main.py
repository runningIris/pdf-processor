from PyPDF2 import PdfFileWriter, PdfFileReader
import math

inputPdf = PdfFileReader('source/original.pdf')

pageSize = 60
pageLength = inputPdf.numPages
shareNum = math.ceil(pageLength / pageSize)

for i in range(shareNum):
  output = PdfFileWriter()

  for j in range(pageSize):
    curr = i * pageSize + j
    if curr == pageLength:
      break
    output.addPage(inputPdf.getPage(curr))
  with open('output\part ' + str(i + 1) + '.pdf', 'wb') as output_stream:
      output.write(output_stream)
