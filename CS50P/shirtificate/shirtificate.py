from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 15, 40, 180)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(50, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_text_color(255,255,255)
x = input("Name: ")
pdf.cell(200, 200, x , align = "C")
"""pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")"""
pdf.output("shirtificate.pdf")