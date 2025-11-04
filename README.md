Simula cómo trabaja una máquina que puede guardar números en una memoria y ejecutar operaciones matemáticas. Es como una calculadora con memoria y la capacidad de seguir un conjunto de instrucciones que el usuario define.

Al iniciar, el programa crea una memoria con 256 posiciones numeradas del 0 al 255, todas inicialmente con valor cero. Tiene un acumulador (ACC), donde el procesador guarda temporalmente el número con el que está trabajando, y un contador de programa (PC), que indica por cuál paso o instrucción va el sistema. Además, existe una variable que indica si el procesador está funcionando o detenido.

El programa puede ejecutar siete tipos de instrucciones diferentes:
LOAD carga el acumulador el valor que hay guardado en una dirección de memoria; ADD suma al valor que hay almacenado en una dirección; SUB resta ese número; MUL multiplica; DIV divide (y si el divisor es cero, el programa muestra un mensaje de error y no se detiene); STORE guarda en una dirección de memoria el valor que está; y HALT detiene la ejecución.

El usuario puede escribir estas instrucciones dentro del programa de manera interactiva. Por ejemplo, se pueden escribir “set 0 7” para guardar el número 7 en la posición 0 de la memoria, o “instr LOAD 0” para decirle que cargue el valor guardado en esa posición. Las instrucciones se van almacenando en una lista llamada “programa”, que luego se ejecuta con el comando “run”. Mientras se ejecuta, el emulador muestra en pantalla el número de instrucción por el que va (PC) y el valor que tiene (ACC).

El programa tiene además otros comandos: “status” muestra el estado actual del procesador, enseñando el valor del acumulador, el número de paso actual y los primeros valores de la memoria; “exit” sirve para salir del modo interactivo. Todo esto permite ver cómo cambian los valores de la memoria y del acumulador a medida que el “procesador” sigue las órdenes.

Cada instrucción se traduce a una forma interna mediante una estructura llamada enumeración (Enum), que asigna un número a cada operación. La función “execute” se encarga de realizar la operación indicada, actualizar el acumulador y avanzar al siguiente paso. El modo interactivo se mantiene en un bucle que lee los comandos del usuario y los interpreta según lo que quiera hacer.

En resumen, este programa representa de forma muy simple el comportamiento básico de un procesador: tiene memoria, puede realizar operaciones matemáticas, y sigue un conjunto de instrucciones.
