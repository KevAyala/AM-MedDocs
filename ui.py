import pdf_generator
import whats_app

class API:
    def generate_pdf(self, datos):
        print("Generando PDF con los siguientes datos:", datos)
        pdf_generator.create_pdf(datos)  # Pasar los datos a la función de generación
        return "PDF generado con éxito"

    def generate_img(self):
        print("Generando imagen desde Python...")
        return "Imagen generada con éxito"
    
    def send_pdf(self, numero):
        print("Enviando PDF desde Python...")
        whats_app.send_pdf(numero)
        return "PDF enviado con éxito"