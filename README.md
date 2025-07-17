# WebSocket# 🧠 Challenge 4 – Comunicación en Tiempo Real con Sockets

Este proyecto fue desarrollado como parte del Challenge 4, cuyo objetivo era diseñar una aplicación de chat funcional, estable y en tiempo real utilizando únicamente sockets, sin frameworks ni bibliotecas externas.

El desafío consistía en reconstruir un sistema de comunicación desde cero, emulando un escenario donde las redes modernas han colapsado y solo quedan las herramientas más esenciales: terminal, sockets y código limpio.

---

## ¿Quién soy después de este reto?

Después de este desafío, me considero un desarrollador más consciente de las bases reales de la comunicación en red. Pude experimentar de primera mano cómo funcionan las conexiones TCP/IP, cómo interactúan múltiples clientes en un entorno concurrente y cómo garantizar estabilidad sin depender de herramientas externas.

Este proyecto me permitió fortalecer mis habilidades en:

- Programación de red con `socket` y `select`
- Concurrencia y comunicación bidireccional con `threading`
- Diseño de aplicaciones resilientes que manejan errores de forma proactiva
- Arquitectura basada en terminal, con enfoque en funcionalidad por encima de presentación

---

## ¿Cómo sobrevivió mi aplicación?

La aplicación fue diseñada con principios de simplicidad y robustez. Logró funcionar de manera estable incluso cuando:

- Múltiples clientes se conectaban y desconectaban de forma arbitraria
- Se producían errores de red o pérdidas de conexión
- El servidor permanecía activo sin importar la salida de usuarios

El servidor maneja múltiples conexiones simultáneamente gracias al uso de `select`, evitando bloqueos. El cliente implementa hilos para escuchar y enviar mensajes en paralelo, manteniendo la experiencia fluida y en tiempo real.

Cada componente fue pensado para resistir fallos comunes y mantener el sistema operativo bajo condiciones adversas.

---

## ¿Qué aprendí cuando todo se rompió?

Durante este proyecto, aprendí a construir y mantener un sistema de comunicación distribuido desde sus fundamentos. Entendí en profundidad conceptos como:

- Monitoreo de múltiples sockets concurrentes sin hilos (con `select`)
- Comunicación segura y ordenada entre procesos de red
- Cierre de conexiones sin pérdidas de recursos
- Diseño de flujo de mensajes con nombre de usuario y control de comandos básicos

También reforcé la importancia del control de errores, el manejo adecuado de excepciones y la necesidad de anticiparse a los estados inesperados que pueden ocurrir en entornos distribuidos.

---

## Conclusión

Este challenge representó mucho más que una práctica de sockets. Fue un ejercicio completo de diseño, estabilidad, concurrencia y comunicación. Logré implementar un sistema que cumple con los principios clave de una red confiable: eficiencia, resistencia y claridad.

Estoy satisfecho con el resultado y con lo aprendido, y considero que este tipo de desafíos son fundamentales para crecer como desarrollador.
