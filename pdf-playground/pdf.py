# Created 7/19/2022

# from PyPDF2 import PdfWriter, PdfReader
# import PyPDF2
# import sys


# inputs = sys.argv[1:]

from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader

# with open('dummy.pdf', "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(f'Reading in {pdf}.')
#         merger.append(pdf)
#         print(f'Finished reading in {pdf}. It has been merged.')
#     merger.write('super.pdf')

# pdf_combiner(inputs)


def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    reader_stamp = PdfReader(stamp_pdf)
    image_page = reader_stamp.pages[0]

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)

watermark("./super.pdf", "./wtr.pdf", "watermark_final.pdf")