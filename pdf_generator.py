from fpdf import FPDF
import os

def create_pdf(datos):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar título
    pdf.cell(200, 10, "Certificado Médico", ln=True, align="C")
    pdf.ln(10)

    # Agregar datos del formulario
    pdf.cell(200, 10, f"Nombre: {datos['nombre']}", ln=True)
    pdf.cell(200, 10, f"Edad: {datos['edad']} años", ln=True)
    pdf.cell(200, 10, f"Fecha: {datos['fecha']}", ln=True)
    pdf.ln(5)

    if datos['parrafo_inicial']:
        pdf.multi_cell(0, 10, "Este es el párrafo inicial del certificado médico.")

    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Cuerpo del documento:\n{datos['cuerpo']}")
    pdf.ln(5)

    if datos['firmado']:
        pdf.cell(200, 10, "Documento firmado electrónicamente.", ln=True)

    pdf.cell(200, 10, f"Teléfono de contacto: {datos['telefono']}", ln=True)

    # Guardar el PDF
    pdf.output(f"./assets/Certificados/{datos['nombre']}+{datos['fecha']}.pdf")
    print("PDF generado: certificado.pdf")
    print(f"El archivo se guardó en: {os.getcwd()}")
