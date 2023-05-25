from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

# Crear el modelo:
class Contact(db.Model):
    # Campos de la DB:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    def serialize(self):
        # Vamos a crear una función para serializar los datos y convertirlos en un diccionario, por eso su estructura.
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
        }

with app.app_context():
    db.create_all()

# Rutas de la API:
@app.route('/contacts', methods=['GET'])
def get_contacts():
    # Esta es para obtener los contactos.
    contacts = Contact.query.all()  # Solicitamos todos los contactos de la DB
    return jsonify({'contacts': [contact.serialize() for contact in contacts]})  # Ahora usamos la función que hicimos para convertir los datos.

@app.route('/contacts', methods=['POST'])
def create_contacts():
    # Para crear contactos, no olvides poner las comas después de cada valor.
    data = request.get_json()  # Vamos a obtener un dato de tipo JSON y lo guardamos en la variable data.
    contact = Contact(name=data['name'], email=data['email'], phone=data['phone'])  # Guardamos los datos del JSON desfragmentados en la variable contact
    db.session.add(contact)  # Y lo guardamos en la DB
    db.session.commit()
    return jsonify({'message': 'contacto creado con éxito', 'contact': contact.serialize()}), 201
    # Este [return] es para que en la respuesta le aparezca al cliente ese mensaje tipado en formato JSON: Primero se le dice cuál es el mensaje, después le regresamos el contacto que se creó, el número al final es parte de los protocolos HTTP, el 201 indica que se creó con éxito.

# Obtener un solo contacto:
@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    # Esta es para obtener un solo contacto.
    contact = Contact.query.get(id)  # Solicitamos el contacto de la DB
    if not contact:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    return jsonify(contact.serialize())

# Editar contacto:
@app.route('/contacts', methods=['PUT', 'PATCH'])
def edit_contact():
    # Esta es para editar los contactos.
    data = request.get_json()
    contact = Contact.query.get_or_404(data['id'])

    if 'name' in data:
        contact.name = data['name']
    if 'email' in data:
        contact.email = data['email']
    if 'phone' in data:
        contact.phone = data['phone']
    db.session.commit()

    return jsonify({'message': 'Contacto actualizado con éxito', 'contact': contact.serialize()})

# Eliminar contacto:
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contacto eliminado con éxito'})

if __name__ == '__main__':
    app.run()
