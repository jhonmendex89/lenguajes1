const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let palabra;
let vidas;
let letrasAdivinadas;
let letrasUsadas = [];

function mostrarEstado() {
    console.log(`\nPalabra: ${letrasAdivinadas.join(' ')}`);
    console.log(`Vidas restantes: ${vidas}`);
    console.log(`Letras usadas: ${letrasUsadas.join(', ')}`);
}

function preguntarLetra() {
    rl.question("Adivina una letra: ", (letra) => {
        letra = letra.toLowerCase();

        if (letrasUsadas.includes(letra)) {
            console.log("ya has usado essa letra, usa otra porfavor :");
            vidas--;
        } else if (palabra.includes(letra)) {
            for (let i = 0; i < palabra.length; i++) {
                if (palabra[i] === letra) {
                    letrasAdivinadas[i] = letra;
                }
            }
            console.log("¡Correcto!");
        } else {
            vidas--;
            console.log("Incorrecto.");
        }

        letrasUsadas.push(letra);
        mostrarEstado();

        if (letrasAdivinadas.join('') === palabra) {
            console.log("\nepaa esa era la palabra, muy bienn ");
            rl.close();
        } else if (vidas === 0) {
            console.log(`\nmuyyy mal La palabra era: ${palabra}`);
            rl.close();
        } else {
            preguntarLetra();
        }
    });
}

function iniciarJuego() {
    rl.question("Ingresa la palabra oculta: ", (input) => {
        palabra = input.toLowerCase();
        vidas = palabra.length;
        letrasAdivinadas = Array(palabra.length).fill('_');
        letrasUsadas = [];
        console.clear();
        mostrarEstado();
        preguntarLetra();
    });
}

iniciarJuego();