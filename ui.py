from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime

# Colores
light_pink = "#bd9ea5"
dark_pink = "#986b70"

# Configuración de la aplicación
app = CTk(fg_color="#ffffff")
app.geometry("1200x700")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

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
frame_left = CTkFrame(master=tabview.tab("Certificado"), fg_color=dark_pink, border_color=dark_pink, border_width=10)
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

# Contenedor para Fecha
date_frame = CTkFrame(frame_left, fg_color="transparent")
date_frame.pack(pady=5, padx=10, fill="x")

# Fecha
date_label = CTkLabel(date_frame, text="Fecha:")
date_label.pack(side="left", padx=5)
date_picker = DateEntry(date_frame, date_pattern='yyyy-mm-dd', background=dark_pink, foreground="white", borderwidth=2, width=12)
date_picker.pack(side="left", padx=5)

# Marcador de casillas de dos opciones (Radiobuttons)
option_frame = CTkFrame(frame_left, fg_color="transparent")
option_frame.pack(pady=5, padx=10, fill="x")
selected_option = StringVar(value="Opción 1")
CTkRadioButton(option_frame, text="Opción 1", variable=selected_option, value="Opción 1").pack(side="left", padx=5)
CTkRadioButton(option_frame, text="Opción 2", variable=selected_option, value="Opción 2").pack(side="left", padx=5)

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
CTkCheckBox(signed_frame, text="Sí").pack(side="left", padx=5)
CTkCheckBox(signed_frame, text="No").pack(side="left", padx=5)

# Botón Generar
generate_button = CTkButton(frame_left, text="Generar")
generate_button.pack(pady=10)

# Marco derecho (Texto más estrecho)
frame_right = CTkFrame(master=tabview.tab("Certificado"), fg_color=light_pink, border_color=light_pink, border_width=10, width=400)
frame_right.pack(side="right", fill="y", padx=10, pady=10)

app.mainloop()
