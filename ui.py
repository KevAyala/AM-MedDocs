from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime


# Colores
light_pink = "#bd9ea5"
dark_pink = "#986b70"
glass_pink_light = "#f0d7dd"  # Pink muy claro para efecto vidrio
glass_pink_dark = "#e5c6ce" 

# Configuración de la aplicación
app = CTk(fg_color="#ffffff")
app.geometry("1200x700")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.title("AM MedDocs")

default_font = CTkFont(family="Montserrat", size=14)

# Tabview
tabview = CTkTabview(
    master=app, width=1200, height=700, corner_radius=10, fg_color="transparent",
    anchor="nw", bg_color="transparent", segmented_button_fg_color=light_pink,
    segmented_button_unselected_color=light_pink, segmented_button_selected_color=dark_pink,
    segmented_button_selected_hover_color=dark_pink, segmented_button_unselected_hover_color=light_pink
)
tabview.grid(row=0, column=0, sticky="nsew")

# Agregar pestañas
tabview.add("Certificado")
tabview.add("Comunicados")

# Marco izquierdo (Formulario)
frame_left = CTkFrame(
    master=tabview.tab("Certificado"), 
    fg_color=glass_pink_dark,        # Color claro semi-transparente
    corner_radius=20,                 # Bordes más redondeados
    border_color="#ffffff",           # Borde blanco sutil
    border_width=1                    # Borde fino
)
frame_left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Contenedor para Nombre y Fecha
name_date_frame = CTkFrame(frame_left, fg_color="transparent")
name_date_frame.pack(pady=5, padx=10, fill="x")

# Nombre
name_label = CTkLabel(name_date_frame, text="Nombre:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = CTkEntry(name_date_frame, width=300)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Edad
age_label = CTkLabel(name_date_frame, text="Edad:")
age_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
age_entry = CTkEntry(name_date_frame, width=80)
age_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
age_label_years = CTkLabel(name_date_frame, text="años")
age_label_years.grid(row=0, column=4, padx=0, pady=5, sticky="w")

# Contenedor para Fecha
date_frame = CTkFrame(frame_left, fg_color="transparent")
date_frame.pack(pady=5, padx=10, fill="x")

# Fecha
date_label = CTkLabel(date_frame, text="Fecha:")
date_label.pack(side="left", padx=5)
date_picker = DateEntry(date_frame, date_pattern='yyyy-mm-dd', background=dark_pink, foreground="white", borderwidth=2, width=12)
date_picker.pack(side="left", padx=5)

# Parrafo Inicial
paragraph_frame = CTkFrame(frame_left, fg_color="transparent")
paragraph_frame.pack(pady=5, padx=10, fill="x")
paragraph_label = CTkLabel(paragraph_frame, text="Párrafo Inicial:")
paragraph_label.pack(side="left", padx=5)
selected_paragraph = StringVar(value="Sí")
CTkRadioButton(paragraph_frame, text="Sí", variable=selected_paragraph, value="Sí").pack(side="left", padx=5)
CTkRadioButton(paragraph_frame, text="No", variable=selected_paragraph, value="No").pack(side="left", padx=5)

# Etiqueta para el cuerpo del documento
body_label = CTkLabel(frame_left, text="Cuerpo del documento:")
body_label.pack(pady=5, padx=10, anchor="w")

# Entrada de texto más grande scrolleable
text_area = CTkTextbox(frame_left, height=100)
text_area.pack(pady=5, padx=10, fill="both", expand=True)

# Contenedor para Firmado
signed_frame = CTkFrame(frame_left, fg_color="transparent")
signed_frame.pack(pady=5, padx=10, fill="x")

# Etiqueta Firmado
signed_label = CTkLabel(signed_frame, text="Firmado:")
signed_label.pack(side="left", padx=5)
signed_option = StringVar(value="No")
CTkRadioButton(signed_frame, text="Sí", variable=signed_option, value="Sí").pack(side="left", padx=5)
CTkRadioButton(signed_frame, text="No", variable=signed_option, value="No").pack(side="left", padx=5)

# Número de teléfono
phone_frame = CTkFrame(frame_left, fg_color="transparent")
phone_frame.pack(pady=5, padx=10, fill="x")
phone_label = CTkLabel(phone_frame, text="Teléfono:")
phone_label.pack(side="left", padx=5)
phone_entry = CTkEntry(phone_frame, width=200)
phone_entry.pack(side="left", padx=5)

# Botón Generar
generate_button = CTkButton(frame_left, text="Generar")
generate_button.pack(pady=10)

# Marco derecho (Texto más estrecho)
frame_right = CTkFrame(master=tabview.tab("Certificado"), fg_color=light_pink, border_color=light_pink, border_width=10, width=400, corner_radius=20)
frame_right.pack(side="right", fill="y", padx=10, pady=10)

def apply_font_to_all_widgets(parent, font):
    """
    Aplica la fuente especificada a todos los widgets hijos de manera recursiva.
    
    Args:
        parent: El widget padre desde donde empezar.
        font: Objeto CTkFont a aplicar.
    """
    for child in parent.winfo_children():
        widget_class = child.__class__.__name__
        
        # Verificar si es un widget que acepta la propiedad font
        if widget_class in ["CTkLabel", "CTkButton", "CTkEntry", "CTkRadioButton", 
                           "CTkCheckBox", "CTkComboBox", "CTkTextbox", "CTkOptionMenu"]:
            try:
                child.configure(font=font)
            except Exception:
                # Algunos widgets pueden no aceptar la propiedad font
                pass
        
        # Para DateEntry, necesitamos una configuración especial ya que es un widget de tkcalendar
        if widget_class == "DateEntry":
            try:
                child.configure(font=("Montserrat", 12))
            except Exception:
                pass
                
        # Recursivamente aplicar a los hijos de este widget
        apply_font_to_all_widgets(child, font)

# Agregar esta línea justo antes de app.mainloop()
apply_font_to_all_widgets(app, default_font)

app.mainloop()
