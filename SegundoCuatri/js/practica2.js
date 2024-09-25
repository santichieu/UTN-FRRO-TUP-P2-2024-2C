/*6. Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.*/

var n1 = prompt("ingrese num 1", " ")
var n2 = prompt("ingrese num 2", " ")
var n3 = prompt("ingrese num 3", " ")

if (Number.parseInt(n1)>Number.parseInt(n2)){
    document.write(n1)
} else {
    document.write(n2)
}
document.write("<br>")
/*7. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.*/
document.write("<br>")
if (Number.parseInt(n1)>Number.parseInt(n2)){
    if(Number.parseInt(n1)>Number.parseInt(n3)){
        document.write("Numero 1: ")
        document.write(n1)
    }
} else if(Number.parseInt(n2)>Number.parseInt(n3)){
    document.write("Numero 2: ")
    document.write(n2)
    
}else{
    document.write("Numero 3: ")
        document.write(n3)
}


/*8. Escribe un programa que pida un número y diga si es divisible por 2 */

document.write("<br>")
document.write("<br>")
if (Number.parseInt(n1)%2===0){
    document.write("Numero divisible por 2")
}else{
    document.write("Numero no divisible por 2")
}

document.write("<br>")
document.write("<br>")

/*9. Escribe un programa que pida una frase y escriba cuantas veces aparece la
letra a */


let frase = prompt("Introduce una frase:")
let contador=0

for (let i=0; i < frase.length; i++){
    if(frase[i].toLowerCase()==='a')
    contador++
}

document.write("La letra a aparece: " + contador + " veces")

/*10. Escribe un programa que pida una frase y escriba las vocales que aparecen*/
document.write("<br>")
document.write("<br>")
let frase2 = prompt("Introduce otra frase:")
let contador2=0

for (let i=0; i < frase2.length; i++){
    if(frase2[i].toLowerCase()==='a')
    if(frase2[i].toLowerCase()==='e')       /*no funca otro dia lo arreglo*/
    if(frase2[i].toLowerCase()==='i')
    if(frase2[i].toLowerCase()==='o')
    if(frase2[i].toLowerCase()==='u')
    contador2++
}

document.write("La vocales aparecen: " + contador2 + " veces")