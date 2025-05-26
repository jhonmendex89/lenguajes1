const readline = require('readline');
const { registrarUsuario } = require('./RegistrarN');
const { leerArchivo } = require('./Leer');

function mostrarMenu() {
  console.log('\n=== MENÚ ===');
  console.log('1. Registrar usuario');
  console.log('2. Buscar usuario');
  console.log('3. Salir');
}

function iniciarMenu() {
  mostrarMenu();

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question('Elige una opción: ', (opcion) => {
    rl.close();

    switch (opcion) {
      case '1':
        registrarUsuario();
        break;
      case '2':
        leerArchivo();
        break;
      case '3':
        console.log('Saliendo...');
        break;
      default:
        console.log('Opción no válida.');
        iniciarMenu();
    }
  });
}

iniciarMenu();
