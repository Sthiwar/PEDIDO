function Guar_Clientes() {
    const tipoPersona = document.getElementById('tipoPersona');
    const nombre = document.getElementById('nombre');
    const correo = document.getElementById('correo');
    const contraseña = document.getElementById('contraseña');
    const nomusario = document.getElementById('nomusario');
    const direc = document.getElementById('direc');
    const telefono = document.getElementById('telefono');
    

    axios.post('/fronted/Guardar_Clientes', {
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
        alert("si")
        document.getElementById('tipoPersona').value = "Selecciona"
        document.getElementById('nombre').value = ""
        document.getElementById('correo').value = ""
        document.getElementById('contraseña').value = ""
        document.getElementById('nomusario').value = ""
        document.getElementById('direc').value = ""
        document.getElementById('telefono').value = ""
    })
    .catch((error) => {
        console.error(error)
        alert(error)
    })
}

function ingreso(){
    
    const tipoPersona = document.getElementById('tipoPersona');
    const Email = document.getElementById('email')
    const password = document.getElementById('pass');

    axios.post('validar_login', {
        tipoPersona: tipoPersona,
        Email: Email.value,
        password: password.value

    },).then((res) => {
        if(tipoPersona == 'PersonaNormal'){
            window.location.href='/fronted/productos';

        }else if(tipoPersona == 'Repartidor'){
            window.location.href='/fronted/repartidor';
        }
            console.log(res.data)
        })
        .catch((error) => {
            console.error(error)
            alert(error)
        })
}

function tipo() {
    // Obtenemos el valor del tipo de persona
    const tipoPersona = document.getElementById("tipoPersona").value;
  
    // Seleccionamos el elemento que queremos mostrar/ocultar
    const direccion = document.getElementById("direc");
  
    // Mostramos u ocultamos el elemento según el tipo de persona
    if (tipoPersona == 'Selecciona') {
      direccion.style.display = 'none';
    } else if (tipoPersona == 'Repartidor') {
      direccion.style.display = 'none';
    }else if (tipoPersona == 'PersonaNormal') {
      direccion.style.display = 'block';
    }
  }