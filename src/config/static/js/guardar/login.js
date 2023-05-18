

function Guar_Clientes() {
    const personaN = document.getElementById('tipoPersona');
    const nombre = document.getElementById('nombre');
    const correo = document.getElementById('correo');
    const contraseña = document.getElementById('contraseña');
    const nomusario = document.getElementById('nomusario');
    const direc = document.getElementById('direc');
    const telefono = document.getElementById('telefono');

alert.log(personaN, nombre, correo, contraseña,nomusario,direc,telefono);
    axios.post('Guardar_Clientes', {
        Nombre: personaN.value,
        Apellido: nombre.value,
        Email: correo.value,
        password: contraseña.value,
        usuario: nomusario.value,
        telefono: direc.value,
        direccion: telefono.value
      

    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}