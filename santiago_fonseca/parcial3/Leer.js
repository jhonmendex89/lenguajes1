function leerArchivo() {
const fs = require('fs');
const readline = require('readline');

const datos = fs.readFileSync('usuarios.json', 'utf8');
const buscar = JSON.parse(datos); 

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.question('Ingresa el nombre a buscar: ', (nombre) => {
  const item = buscar.find(encontrar => encontrar.usuario === nombre);

  if (item) {
    console.log(`Usuario encontrado es: ${item.usuario}`);
    console.log(`Título: ${item.titulo}`);
    console.log(`Descripción: ${item.descripcion}`);
        console.log(`tarea: ${item.tareas}`);
    console.log(`Estado: ${item.estado}`);
  } else {
    console.log('Usuario no existe');
  }

  rl.close();
});
}
exports.leerArchivo = leerArchivo;