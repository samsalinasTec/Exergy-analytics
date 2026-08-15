# Protocolo de trabajo

Documento vivo. Vive en el repositorio, se cambia por Pull Request, no por WhatsApp.

**Versión:** 0.1 (borrador para discusión)
**Dueño actual:** [Sam]
**Última revisión:** [fecha]

---

## 0. Para qué existe este documento

Somos cuatro personas, en tres husos horarios, con unas cuatro horas semanales cada uno. En esas condiciones, la coordinación informal no funciona: una pregunta no resuelta cuesta una semana de calendario.

Este documento existe para que nadie tenga que preguntar cómo se hacen las cosas. Si algo no está aquí y hace falta, se agrega. Si algo está aquí y ya no sirve, se quita. Ambas cosas se hacen por PR.

**Regla de oro:** si te encuentras explicando lo mismo por segunda vez, la respuesta correcta no es explicarlo mejor, es escribirlo aquí.

---

## 1. Las restricciones de las que sale todo lo demás

Estos números no son pesimismo, son el presupuesto real con el que se diseñó todo lo que sigue.

| Variable | Valor |
|---|---|
| Personas | 4 |
| Horas nominales por persona por semana | 4 |
| Horas nominales de equipo por semana | 16 |
| Horas productivas reales tras coordinación y pausas | ~7.5 |
| Horas productivas en 6 meses | ~190 |
| Sesiones de trabajo por persona por semana | 1 |
| Husos horarios | 3 (JST, EST, CST México) |
| Ventana común entre semana | Japón 22:00 / Toronto 09:00 / México 07:00 |
| Ventana común fin de semana | Japón sáb 09:00 / Toronto vie 20:00 / México vie 18:00 |

**Las tres consecuencias que gobiernan todo:**

1. Una persona trabaja **una vez por semana**. Si su tarea depende de que otro termine primero, el handoff cuesta 7 días de calendario, no 2 horas.
2. Una junta de una hora con los cuatro consume **el 25 por ciento** de la capacidad semanal del equipo. Las juntas son caras y se tratan como tales.
3. Todo lo que no está escrito, no existe. Nadie está despierto para preguntarle.

---

## 2. Los principios, y de dónde salen

No son opiniones. Vienen de dos cuerpos de evidencia documentada.

### 2.1 DORA / Accelerate

El programa DORA (Forsgren, Humble, Kim) lleva desde 2014 encuestando a miles de organizaciones de ingeniería con métodos estadísticos para identificar relaciones causales, no solo correlaciones. Su síntesis es el libro *Accelerate* (2018) y los reportes anuales *State of DevOps*.

**Hallazgo central, repetido cada año desde 2014:** velocidad y estabilidad no son un intercambio. Los equipos que despliegan más frecuentemente tienen *menos* fallas y se recuperan más rápido.

**Las prácticas de los equipos élite:**
- Desarrollo sobre trunk, sin ramas de larga vida
- Pruebas automatizadas en cada commit
- Lotes pequeños que limitan el radio de daño
- Un pipeline lo bastante rápido y confiable como para que ejecutarlo sea rutinario

**El hallazgo que más nos aplica (DORA 2024/2025):** la adopción de IA aumenta la productividad individual, el flujo y la satisfacción, pero **impacta negativamente la estabilidad y el throughput de entrega**. La causa hipotetizada por los autores: la IA permite producir mucho más código en el mismo tiempo, los changelists crecen, y los cambios grandes son más lentos y más propensos a generar inestabilidad. La revisión y la infraestructura de despliegue no alcanzan a absorber el volumen.

Nosotros vamos a trabajar con IA de forma intensiva. Este es, literalmente, nuestro modo de falla documentado. Las reglas de la sección 6 existen por esto.

**Otros dos hallazgos relevantes:**
- La **seguridad psicológica** está entre los predictores más fuertes del desempeño de entrega.
- Las **prioridades inestables** causan caídas de productividad y aumentos de burnout, con un efecto resistente a mitigación que persiste incluso con buenos líderes y buena documentación. Cambiar de proyecto a media obra nos daña más que haber elegido mal el proyecto.

### 2.2 El modelo GitLab

GitLab opera con más de 2,000 personas en más de 65 países y cero oficinas. Es la cultura remota mejor documentada que existe, y su manual es público.

**Handbook-first:** la documentación se escribe *antes* de comunicar, no después. Documentar después es un paso que siempre se omite.

**Prácticas codificadas:**
- Las juntas son último recurso, no primera respuesta
- Todo empieza como un issue o un merge request; propuestas, decisiones y discusiones ocurren por escrito primero
- Las juntas requieren agenda y un resultado documentado
- Si no puede escribirse, probablemente no necesitaba una junta
- **No hay expectativa de respuesta inmediata**, y los tiempos de respuesta esperados están documentados explícitamente

---

## 3. Cómo nos comunicamos

### 3.1 Dónde vive cada cosa

| Tipo de contenido | Dónde vive | Dónde NO vive |
|---|---|---|
| Decisiones técnicas | `docs/decisions/` (ADR) | WhatsApp, la junta |
| Tareas y su estado | GitHub Projects | La cabeza de alguien |
| Discusión sobre código | Comentarios del PR | Mensajes directos |
| Discusión sobre alcance | Issue de GitHub | WhatsApp |
| Cómo se hace algo | Este documento | La memoria de Sam |
| Contexto para la IA | `CLAUDE.md` | Cada quien por su lado |
| Coordinación urgente | WhatsApp | (único uso válido) |

**WhatsApp es para avisar que algo se rompió y para el trato humano. Nada que sea una decisión, un acuerdo o contexto puede vivir ahí.** Si una conversación de WhatsApp produce una decisión, quien la haya iniciado abre el PR con el ADR ese mismo día.

### 3.2 Tiempos de respuesta esperados

Explícitos, para que nadie viva con deuda.

| Situación | Respuesta esperada |
|---|---|
| Producción caída | Lo antes posible, se avisa por WhatsApp |
| Bloqueo de alguien más | 24 horas |
| Revisión de PR | 48 horas |
| Discusión de diseño o alcance | 72 horas |
| Todo lo demás | Cuando puedas |

**Nadie debe nada fuera de esos tiempos.** No responder en 3 horas no es descortesía, es el funcionamiento esperado.

### 3.3 Ceremonias

Solo dos. Todo lo demás es asíncrono.

**Junta quincenal, 45 minutos.** Sábado 09:00 Japón (viernes 20:00 Toronto, viernes 18:00 México). Agenda fija, publicada 24 horas antes en un issue:
1. Métricas de la sección 8 (5 min)
2. Qué se cerró desde la última (5 min)
3. Bloqueos que no se resolvieron por escrito (15 min)
4. Decisiones que requieren los cuatro (15 min)
5. Quién toma qué en las próximas dos semanas (5 min)

Reglas: se graba, alguien toma notas en el issue, y **nada de informar cosas que ya estaban escritas**. Si el punto se puede leer, no se dice.

**Check-in escrito semanal.** Cada quien, el día que le toque, tres líneas en el issue de la semana:
```
Hice: ...
Sigo con: ...
Bloqueado en: ... (o "nada")
```

Si alguien no publica su check-in, no pasa nada. No es un mecanismo de control, es un mecanismo de contexto.

---

## 4. Cómo se organiza el trabajo

Esta es la sección que decide si nos pisamos o no.

### 4.1 La decisión de fondo: verticales, no capas

**Nadie se especializa en backend o frontend. Cada persona toma una funcionalidad completa, de la base de datos a la pantalla.**

La razón es la restricción del punto 1.3. Si Ana hace el backend y Luis el frontend, Luis no puede empezar hasta que Ana termine su endpoint. Ana trabaja el martes, Luis el jueves. Si Ana no alcanzó, Luis pierde su única sesión de la semana. Con especialización por capas, **la mitad de nuestra capacidad se va en esperar**.

Con rebanadas verticales, cada quien avanza solo, siempre.

Ejemplo aplicado al proyecto de RH:

| Rebanada | Incluye |
|---|---|
| Candidatos | Modelo, migración, CRUD, vista de listado, plantilla |
| Kanban de etapas | Modelo de etapa, transiciones, vista, drag & drop |
| Agendamiento | Integración con Google Calendar, lógica de disponibilidad, vista |
| Notificaciones | Plantillas de correo, disparadores, envío |
| Dashboard | Consultas agregadas, vista, gráficas |

Una persona toma una rebanada completa y la lleva a producción.

**El costo aceptado:** todos aprendemos todo, lo que significa que todos somos más lentos al principio. Se compensa con creces contra el costo de esperar.

**La excepción:** las cuatro primeras semanas de cada proyecto, cuando se construyen los cimientos, sí conviene que una sola persona monte el esqueleto (proyecto, deploy, CI, modelo base). Cuatro personas montando cimientos en paralelo es garantía de choque.

### 4.2 Dueños de decisión (no de trabajo)

Cada quien es dueño de un área **de decisión**, no de un área de código. Ser dueño significa que si hay duda, tú decides y lo escribes. No significa que solo tú tocas eso.

| Área | Dueño | Qué decide |
|---|---|---|
| Arquitectura y modelo de datos | [ ] | Estructura de apps, modelos, migraciones |
| Infraestructura, CI/CD, deploy | [ ] | Pipeline, ambientes, variables, monitoreo |
| UI y componentes | [ ] | Estilos, componentes reutilizables, consistencia |
| Producto y alcance | [ ] | Qué entra, qué sale, qué es "terminado" |

Se rota cada proyecto. Nadie se vuelve indispensable.

### 4.3 Fases de un proyecto

**Fase 0. Esqueleto en producción (semana 1, ~8 horas, una persona).**
Proyecto Django creado, desplegado en Railway con Postgres, CI corriendo, dominio apuntando, `CLAUDE.md` inicial. La app no hace nada y ya está en producción. **Nada más empieza hasta que esto está listo.**

**Fase 1. Contratos (semana 2, ~8 horas, dos personas).**
Modelo de datos completo acordado y escrito como ADR. Migraciones base aplicadas. URLs y nombres de apps definidos. Esta fase es la que evita el 80 por ciento de los choques posteriores: **una vez que el modelo de datos está fijo, cuatro personas pueden trabajar en paralelo sin tocarse.**

**Fase 2. Rebanadas en paralelo (semanas 3 a 12, el grueso).**
Cada quien toma una rebanada de la sección 4.1 y la lleva a producción. Aquí es donde se gana o se pierde el proyecto.

**Fase 3. Integración y pulido (semanas 13 a 16).**
Lo que ninguna rebanada cubrió: navegación coherente, manejo de errores, textos, permisos, datos de prueba realistas, y la documentación de entrega al cliente.

### 4.4 Cómo no pisarnos

Los choques no ocurren al azar. Ocurren en archivos predecibles, y se previenen así:

**a) Fronteras por app de Django.** Cada rebanada es su propia app: `candidatos/`, `etapas/`, `agenda/`, `notificaciones/`, `reportes/`. Cada app tiene su `models.py`, sus vistas y sus plantillas. Dos personas en apps distintas casi nunca tocan los mismos archivos.

**b) Los archivos compartidos son zona de cuidado.** `settings.py`, `urls.py` raíz, `base.html`, `requirements.txt`. Reglas: cambios mínimos, un cambio por PR, y se mergea el mismo día. No se acumulan.

**c) Las migraciones son el choque clásico.** Dos migraciones creadas en paralelo sobre la misma tabla generan conflictos feos.
- Una migración por PR, máximo
- Un PR con migración se mergea en menos de 24 horas o se cierra
- Antes de generar una migración, `git pull` de main, siempre
- Si tu PR con migración lleva más de 2 días, lo rebasa y regeneras

**d) Contratos antes que implementación.** Si tu rebanada necesita algo de la de otro, no esperas: acuerdan la firma (nombre de la función, qué recibe, qué devuelve) en el issue, y cada quien implementa su lado contra esa firma. Puedes trabajar contra algo que todavía no existe.

**e) Nadie se guarda trabajo.** El código a medias vive en main detrás de una bandera o en una URL que nadie enlaza, no en la laptop de alguien. Código en una rama de 3 semanas es código que ya chocó y todavía no lo sabes.

---

## 5. Flujo de código

### 5.1 Ramas

**Trunk-based.** Una sola rama permanente: `main`.

- Ramas de trabajo cortas: `feat/agenda-disponibilidad`, `fix/kanban-orden`
- **Vida máxima de una rama: 3 días.** Si no cabe en 3 días, la tarea está mal partida.
- `main` siempre desplegable. Siempre.
- Nada de `develop`, `release/*`, gitflow ni nada parecido

### 5.2 Pull Requests

**Este es el freno anti-IA. Es la regla más importante del documento.**

- **Un PR se lee completo en 20 minutos.** Si no, se parte antes de abrirse.
- Guía práctica: por debajo de ~400 líneas cambiadas. Si Claude generó 900, no abres el PR de 900. Lo partes.
- **Ningún merge sin que otra persona lo haya leído.** Sin excepción, ni siquiera Sam, ni siquiera "es un cambio chiquito".
- Descripción del PR: qué hace, por qué, y cómo se prueba. Tres líneas bastan.
- Squash merge, para que el historial de `main` sea legible.

**Por qué es innegociable:** la evidencia de DORA muestra que los equipos que adoptan IA degradan su estabilidad de entrega precisamente porque el volumen de código generado supera la capacidad de revisión. Nuestra ventaja de velocidad se convierte en nuestra fuente de inestabilidad si no ponemos este freno.

**Presupuesto de revisión: 20 minutos por PR.** Sí, sale de nuestras 4 horas. Es la inversión más rentable que hacemos.

### 5.3 Qué corre el CI

En cada push, y debe terminar en menos de 3 minutos:
- `ruff check` y `ruff format --check` (nunca discutimos estilo)
- `pytest`
- `python manage.py makemigrations --check --dry-run` (detecta migraciones olvidadas)

### 5.4 Pruebas

No perseguimos cobertura, no tenemos horas. Se prueba solo lo que duele si se rompe:
- Lógica de negocio no trivial (disponibilidad de calendario, transiciones de etapa, cálculos del dashboard)
- Cualquier bug que ya nos pasó una vez (prueba de regresión, siempre)

No se prueban: vistas CRUD generadas, plantillas, el admin de Django.

### 5.5 Despliegue

- **Merge a `main` despliega a producción automáticamente.** Sin intervención humana.
- Migraciones se aplican en el despliegue.
- Si el despliegue rompe algo, **se revierte primero y se investiga después.** Revertir es barato, depurar en producción es caro.
- Meta: al menos un despliegue por semana. Es nuestro termómetro de tamaño de lote.

---

## 6. Estándar de trabajo con IA

**Un solo estándar para los cuatro, versionado en el repo.** Con una sesión semanal por persona, que cada quien tenga su propia forma significa que nadie puede continuar el trabajo del otro.

### 6.1 El archivo `CLAUDE.md`

Vive en la raíz. Es el contrato. Se cambia por PR como cualquier otra cosa. Contiene, en este orden:

1. **Stack exacto con versiones.** Django 5.x, Python 3.12, HTMX, Alpine, Tailwind, Postgres.
2. **Estructura de carpetas** y dónde va cada tipo de archivo.
3. **Convenciones:** nombres, manejo de errores, validación, dónde va la lógica de negocio.
4. **Comandos:** cómo levantar local, cómo correr pruebas, cómo desplegar.
5. **Prohibiciones explícitas.**

La sección 5 es la que más valor da y la que todo el mundo olvida. Sin ella, cada sesión introduce una dependencia nueva y en dos meses hay cuatro formas distintas de hacer lo mismo. Ejemplos de lo que va ahí:

```
- No agregar dependencias sin un ADR aprobado
- No usar Django REST Framework en este proyecto; las vistas devuelven HTML
- No usar Celery; las tareas programadas son management commands
- No escribir JavaScript fuera de Alpine, salvo el kanban
- No crear abstracciones para un solo caso de uso
- No tocar settings.py sin avisar en el PR
```

### 6.2 Cómo trabajamos con el modelo

- **Planear en texto antes de generar código.** El código generado sin plan es el que se tira.
- **Sesiones cortas, un objetivo.** Limpiar contexto entre tareas distintas.
- **Nunca pegar el repositorio completo.** Apuntar a los archivos concretos.
- **Paralelizar solo tareas independientes.**
- **Leer todo lo que se va a mergear.** Si no entiendes una línea de tu propio PR, no está lista.

### 6.3 La regla que resume todo

**Nunca mergeamos código que nadie entiende.** Que funcione no es suficiente. Código que funciona y nadie entiende es deuda técnica con esteroides cuando somos cuatro a tiempo parcial.

---

## 7. Documentación

### 7.1 ADRs (Architecture Decision Records)

Carpeta `docs/decisions/`. Un archivo por decisión, numerado: `0007-usar-htmx-en-lugar-de-react.md`.

Plantilla, y no más de 15 líneas:

```markdown
# 0007. Título de la decisión

**Fecha:** 2026-08-15
**Estado:** aceptada | reemplazada por 00XX
**Propuesta por:** [nombre]

## Contexto
Qué problema teníamos.

## Decisión
Qué elegimos.

## Alternativas consideradas
Qué más evaluamos y por qué no.

## Consecuencias
Qué se vuelve más fácil y qué más difícil.
```

**Qué amerita un ADR:** una dependencia nueva, un cambio de estructura, una decisión que costó discusión, cualquier cosa que alguien vaya a cuestionar en tres meses.

**Para qué sirven de verdad:** sustituyen las conversaciones que no podemos tener por los husos horarios, y evitan que en octubre alguien reabra una discusión que ya cerramos en agosto.

### 7.2 Regla de escribir primero

Ninguna decisión se comunica antes de estar escrita. Se abre el PR con el ADR, y *después* se avisa. No al revés, porque documentar después es el paso que siempre se omite.

---

## 8. Cómo medimos

Tres números, del equipo, revisados en la junta quincenal.

| Métrica | Cómo se mide | Meta |
|---|---|---|
| Frecuencia de despliegue | Despliegues a producción por semana | ≥ 1 |
| Tiempo de ciclo | De que la tarea se toma a que está en producción | < 7 días |
| Tasa de cierre semanal | % de tareas terminadas en la semana en que se tomaron | ≥ 70% |

**Cómo se leen:**
- Frecuencia baja: los lotes están creciendo. Partir mejor el trabajo.
- Tiempo de ciclo alto: hay dependencias en serie o PRs esperando revisión.
- Tasa de cierre baja: las tareas están mal dimensionadas para una sesión de 3 horas.

**Dos prohibiciones:**

1. **Estas métricas nunca se usan para evaluar personas.** Son indicadores de sistema. Aplicarlas a individuos incentiva inflar commits y partir lotes artificialmente, y destruye su valor como diagnóstico.
2. **Nada de story points, velocity ni sprints.** Con una sesión semanal por cabeza, esas ceremonias cuestan más de lo que informan.

---

## 9. Regla de pausas

Cualquiera puede pausar el proyecto por temas de su vida (una vacante, un examen, una mudanza, lo que sea).

- **No se justifica.** Se avisa. Pedir justificación reintroduce exactamente el costo social que esta regla existe para eliminar.
- **Aviso con dos semanas**, en la junta o por escrito.
- **Máximo una persona en pausa a la vez.** Con dos pausados quedan 8 horas semanales y el proyecto se detiene de facto. El segundo en avisar espera turno.
- **Máximo dos meses por persona por año.** Más que eso deja de ser pausa y se trata en el acuerdo de socios.
- **Handoff obligatorio antes de pausar:** media hora escribiendo qué estabas haciendo, dónde quedó y qué sigue. Media hora tuya ahorra tres horas de los demás.

Quien regresa, regresa sin deuda y sin conversación incómoda. Ese es el punto.

---

## 10. Definición de terminado

Una tarea está terminada cuando **todas** se cumplen:

- [ ] El código está en `main`
- [ ] Está desplegado en producción
- [ ] Otra persona leyó el PR
- [ ] El CI pasó
- [ ] Si había decisión de diseño, hay ADR
- [ ] Si cambió cómo se opera algo, este documento está actualizado

No hay "terminado pero falta desplegar". Eso es "no terminado".

---

## 11. Cómo se cambia este documento

PR al repositorio. Se necesita que al menos una persona más lo apruebe. El dueño del documento rota cada tres meses.

Si una regla de aquí les está estorbando, la regla está mal, no ustedes. Ábranle un PR.
