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

Conclusión

Este proyecto me hizo entender como funcionan (en parte) las redes sociales hoy día. Cosas tan comunes como esa, que no cuenta nos damos y ahora entiendo más del funcionamiento de las mismas.
