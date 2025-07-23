🧠 Proyecto de Chat con Sockets (Challenge 4)

Este proyecto es un chat por terminal hecho a puro pulmón con sockets, select y threading. Lo hice como parte del Challenge 4 del curso, donde la idea era entender cómo funcionan los web sockets sin usar ninguna biblioteca externa ni frameworks mágicos.

🚀 ¿Para qué sirve?

Sirve para que varios usuarios se conecten al servidor y puedan mandarse mensajes en tiempo real. Cada cliente ve lo que escriben los demás. Es como un grupo de WhatsApp, pero en consola y más "vieja escuela".

🧱 ¿Qué usé?

socket: para manejar las conexiones de red.

select: para que el servidor pueda escuchar a muchos clientes sin trabarse.

threading: para que cada cliente pueda enviar y recibir al mismo tiempo.

⚠️ Lo más jodido

Entender cómo funcionan los hilos del cliente fue lo que más me costó. El código es corto, pero el concepto de que algo "escuche" en segundo plano mientras vos escribís no fue tan directo. Me rompí la cabeza con eso.

💡 ¿Qué aprendí?

Cómo funciona select para escuchar muchos sockets a la vez.

Cómo usar threading para que el cliente pueda escribir y recibir mensajes en paralelo.

Cómo detectar cuando un cliente se desconecta y cerrar todo sin que explote.

Cómo hacer que un chat funcione sin depender de nada externo.

🛡️ ¿Qué tan bueno está?

Resiste desconexiones sin romperse.

No se cae si un cliente se va o se cierra mal.

Funciona fluido, en tiempo real.

Lo probé con varios clientes y aguanta bien.

💬 ¿Quién sos después de este reto?
Después de este proyecto, siento que entiendo mucho mejor cómo se comunican las computadoras entre sí. Ya no veo los chats o juegos online como algo mágico: ahora sé que por detrás hay sockets, mensajes, hilos y muchas cosas que pueden romperse si no las manejás bien.

Me di cuenta que no hace falta usar cosas pesadas como Flask o bibliotecas externas para que algo funcione bien. Con lo básico y con cabeza se puede construir algo real.

⚙️ ¿Cómo sobrevivió tu aplicación?
Sobrevivió porque la pensé simple pero sólida. El servidor usa select, así que no se traba cuando hay muchos clientes. Los clientes usan threading, así que podés escribir y recibir mensajes al mismo tiempo sin bloquear nada.

También puse control de errores, así que si un cliente se desconecta, el servidor no se cae. Y si pasa algo raro, se cierra todo limpio.
