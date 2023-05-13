from config.db import db, app, ma


class Users(db.Model):
    __tablename__ = "tblrgpersonas"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    usuario = db.Column(db.String(200))
    tipo = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200))
   

    def __init__(self, full_name, Email, telefono, tipo, jornada, id_roles, cedula, password):
        self.full_name = full_name
        self.Email = Email
        self.password = password
        self.usuario = usuario
        self.tipo = tipo
        self.telefono = telefono
        self.direccion = direccion        

        with app.app_context():
            db.create_all()


class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'Email', 'password',
                  'usuario','tipo','telefono','direccion')