/*Escribe un programa de una sola línea que haga que aparezca en la pantalla un
alert que diga “Hello World”..*/ 
alert("HOLA MUNDOOOOOO")

/*Escribe un programa de una sola línea que escriba en la pantalla un texto que
diga “Hello World” (document.write).*/
document.write("hello world")

/*Escribe un programa de una sola línea que escriba en la pantalla el resultado
de sumar 3 + 5.*/ 
document.write(3+5)
document.write("<br>")
/* Escribe un programa de dos líneas que pida el nombre del usuario con un
prompt y escriba un texto que diga “Hola nombreUsuario” */

var usuario = prompt("ingrese nombre y apellido", " ")
document.write("Hola "  + usuario)
document.write("<br>")
/*Escribe un programa de tres líneas que pida un número, pida otro número y
escriba el resultado de sumar estos dos números. */

var n1 = prompt("ingrese num", " ")
var n2 = prompt("ingrese num 2", " ")
document.write(Number.parseInt(n1)+Number.parseInt(n2))

/**Ejercicio extra (combinando .js, .css y .html): Crear una página que 
pida el nombre del usuario, dos valores y nos muestre las 4 
operaciones aritméticas. Todos los datos deberán aparecer en el 
documento, incorporar estilos. */
document.write("<div>")
document.write("SUMA: ")
document.write(Number.parseInt(n1)+Number.parseInt(n2))
document.write("<br>")
document.write("MULTIPLICACION: ")
document.write(Number.parseInt(n1)*Number.parseInt(n2))
document.write("<br>")
document.write("RESTA: ")
document.write(Number.parseInt(n1)-Number.parseInt(n2))
document.write("<br>")
document.write("DIVISIÓN: ")
document.write(Number.parseInt(n1)/Number.parseInt(n2))
document.write("</div>")