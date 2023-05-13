from config.db import db, app, ma


class Repartidor(db.Model):
    __tablename__ = "tblrepartior"

    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(200))
    Apellido = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    usuario = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
   

    def __init__(self, Nombre,Apellido, Email, password, usuario, telefono):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Email = Email
        self.password = password
        self.usuario = usuario
        self.telefono = telefono

        with app.app_context():
            db.create_all()


class RepartidorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Nmobre','Apellido', 'Email', 'password',
                  'usuario','telefono')