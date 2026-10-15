
# =====================================
#  Proyecto ORM Simple
# =====================================

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# Configuracion de la aplicacion Flask.
app = Flask(__name__)

# Se define la URI de conexion a la base de datos.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tutorial.db"

# Desactiva el rastreo de modificaciones para optimizar el rendimiento.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ceamos un objeto para acceder a la BDD.
db = SQLAlchemy(app)

# ============================
# DEFINICION DEL MODELO
# ============================
# 2. Definicion del modelo User.
# ===========================
class Product(db.Model):
    __tablename__ = "product"
    
    # Definicion de campos de la tabla
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    
    # Para depurecion.
    # Representacio legible para consola.
    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"
    
# ==================================
# INICIALIZACION DE LA BASE DE DATOS
# ==================================
# 3. Funcion para crear las tablas.
# (MIGRACION)
# =================================
def init_db():
    with app.app_context():
        db.create_all()
        print('Base de datos y tabla "product" creada satisfactoriamente')


# ===============================
# OPERACIONES CRUD CON SQLAlchemy
# ===========================
# 3.1 Crear registros INSERT
# ===========================
def insert_products():
    with app.app_context():
        # Crear instancias del modelo User
        product1 = Product(name="Laptop", price =3500, stock=5)
        product2 = Product(name="Mouse Inalambrico", price =55, stock=30)
        product3 = Product(name="Teclado Mecanico", price =75, stock=15)

        # Agregar los objetos a la sesión de base de datos
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)

        # Guardar los cambios en la base de datos
        db.session.commit()
        print("Productos creados e insertados")


# ============================
# 3.2 Consultar registros (SELECT)
# =============================
def query_products():
    with app.app_context():
        print("Listado de Productos")

        # Consulta todos los registros de la tabla
        products = Product.query.all()
        for item in products:
            print(item)

        # Filtrar registros con condición (equivalente a WHERE)
        print("\nListado de registros filtrados")
        filtrados = Product.query.filter(Product.id >= 2).all()
        for item in filtrados:
            print(item)

        # Obtener un solo registro
        print("\nObtener un solo registro")
        product = Product.query.filter_by(id=1).first()
        if product:
            print(product)
        else:
            print("Producto no encontrado")


# ==================================
# 3.3 Actualizar registros (UPDATE)
# ================================

def update_product():
    with app.app_context():
        print("\nActualización de un registro")

        # Buscar el usuario con id=1
        product = Product.query.filter_by(id=1).first()
        if product:
            product.name = "Case CPU"
            product.price = 350
            product.stock = 5
            db.session.commit()
            print("Producto actualizado:", product)
        else:
            print("Producto no encontrado")



# ===========================
# 3.4 Eliminar registros (DELETE)
# ==========================
def delete_product():
    with app.app_context():
        print("\nEliminación de registros")
        
        
        product = Product.query.filter_by(id=3).first()
        if product:
            db.session.delete(product) # Eliminamos al producto con id=3
            db.session.commit()
            print("Producto eliminado satisfactoriamente")
        else:
            print("Producto no encontrado")



# Ejecucion del prpograma principal.
if __name__ == "__main__":
    # init_db()         # Crear la BDD y tabla.  
    # insert_products() # Insertar registros.
    # query_products()  # Consultar registros.
    # update_product()  # Actualizar un registro.
    delete_product()  # Eliminar un registro.


