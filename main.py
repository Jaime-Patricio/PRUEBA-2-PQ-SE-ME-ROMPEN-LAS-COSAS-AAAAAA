# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        Texto_Principal = request.form.get("textTop")
        Texto_Secundario = request.form.get("textBottom")
        Color_Selector = request.form.get("color-selector")
        

        # Asignación #3. Recepción del posicionamiento del texto
        

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image,
                               Texto_Principal=Texto_Principal,
                               Texto_Secundario=Texto_Secundario,
                               Color_Selector=Color_Selector

                               # Asignación #2. Visualización del texto
                               

                               #  Asignación #3. Visualización del color
                               
                               
                               # Asignación #3. Visualización de la posición del texto


                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
