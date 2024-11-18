from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

def make_receipt(data, out_file_name):
    """Generates a PDF receipt with the given data."""
    pdf = SimpleDocTemplate(out_file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1
    title = Paragraph("Dessert Shop Receipt", title_style)

    # Add the table data and styles
    table_data = [["Name", "Item Cost", "Tax Amount"]] + data
    style = TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ])

    table = Table(table_data, style=style)
    pdf.build([title, table])