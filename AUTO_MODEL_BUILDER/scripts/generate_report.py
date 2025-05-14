from fpdf import FPDF

class PDFReport:
    def __init__(self, title):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.pdf.ln(10)

    def add_section(self, title, content):
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.ln(5)

    def save(self, filename):
        self.pdf.output(filename)