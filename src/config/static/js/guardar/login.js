

function Guar_Clientes() {
    const tipoPersona = document.getElementById('tipoPersona');
    const nombre = document.getElementById('nombre');
    const correo = document.getElementById('correo');
    const contraseña = document.getElementById('contraseña');
    const nomusario = document.getElementById('nomusario');
    const direc = document.getElementById('direc');
    const telefono = document.getElementById('telefono');
    

    axios.post('fronted/Guardar_Clientes', {
        tipoPersona: tipoPersona.value,
        NombreC: nombre.value,
        Email: correo.value,
        password: contraseña.value,
        usuario: nomusario.value,
        telefono: telefono.value,
        direccion: tipoPersona.value === 'PersonaNormal' ? direc.value : ''
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        console.log("si")
        alert("si")
    })
    .catch((error) => {
        console.error(error)
        alert(error)
    })
}