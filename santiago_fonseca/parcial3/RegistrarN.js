function registrarUsuario() {
const fs = require('fs');
const readline = require('readline');

const datos = fs.readFileSync('usuarios.json', 'utf8');
const usuarios = JSON.parse(datos);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const nuevoUsuario = {};
const nuevaTarea = {};

function preguntaNombre() {
  rl.question('¿Cuál es tu nombre? ', (nombre) => {
    nuevoUsuario.usuario = nombre;


    preguntaTitulo();
  });
}

function preguntaTitulo() {
  rl.question('¿Cuál es tu título? ', (titulo) => {
    nuevoUsuario.titulo = titulo;
    preguntaDescripcion();
  });
}

function preguntaDescripcion() {
  rl.question('Ingresa la descripción: ', (descripcion) => {
    nuevoUsuario.descripcion = descripcion;
    preguntaTarea();
  });
}
function preguntaTarea() {
  rl.question('Agrega la tarea del usuario: ', (respuesta) => {
    nuevoUsuario.tareas = respuesta;
    preguntaEstado();
  });
}
function preguntaEstado() {
  rl.question('Ingresa el estado: ', (estado) => {
    nuevoUsuario.estado = estado;

    usuarios.push(nuevoUsuario);

    const nuevoContenido = JSON.stringify(usuarios, null, 2);
    fs.writeFileSync('usuarios.json', nuevoContenido);

    console.log('¡Usuario agregado correctamente!');
    rl.close();
  });
}

preguntaNombre();
}
exports.registrarUsuario = registrarUsuario;
