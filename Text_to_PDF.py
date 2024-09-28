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

    # Adding the file name as header
     pdf.set_font(family="Times", style="B", size=12)
     pdf.cell(w=50, h= 8,txt=filename, ln=1)

     #Adding the content of files using multi-cells
     with open(filepath, 'r') as file:
          content = file.read()
     pdf.set_font(family= "Times", size=8)
     # content = pd.read_csv
     pdf.multi_cell(w=0, h=6, txt = content)


pdf.output("Text_to_PDF/output.pdf")