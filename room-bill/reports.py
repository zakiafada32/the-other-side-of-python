import webbrowser
import os
from dotenv import load_dotenv
from filestack import Client
from fpdf import FPDF

load_dotenv()


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image(
            f"{os.getcwd()}/room-bill/files/house.png",
            w=30,
            h=30,
        )

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Change directory to files, generate and open the PDF
        os.chdir(f"{os.getcwd()}/room-bill/files/")
        pdf.output(self.filename)
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(f"{os.getcwd()}/{self.filename}", new=2)


class FileSharer:
    def __init__(self, filepath, api_key=os.getenv("FILESTACK_KEY")):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url