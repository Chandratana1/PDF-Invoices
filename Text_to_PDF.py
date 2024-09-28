from  fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("Text_to_PDF/*.txt")
#print(filepaths)
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
     #df=pd.read_csv(filepath)

     pdf.add_page()

     filename= (Path(filepath).stem).title()


     pdf.set_font(family="Times", style="B", size=12)
     pdf.cell(w=50, h= 8,txt=filename)

pdf.output("Text_to_PDF/output.pdf")