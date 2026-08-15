# Aprendizajes

**El archivo más valioso de este repositorio y el que todos los equipos abandonan.**

Aquí va lo que costó caro. En seis meses vale más que todo lo demás junto.

**Relacionado:** [Checklist de nuevo proyecto](checklist-nuevo-proyecto.md), [Protocolo de trabajo](../protocolo-de-trabajo.md)

---

## Cómo se escribe una entrada

Cuando algo salga mal, se agrega una entrada. Formato corto:

```
### [Fecha] Título de lo que pasó
**Qué pasó:** en una o dos líneas
**Qué nos costó:** horas, o qué se rompió
**Qué hacemos distinto:** la regla concreta
```

**Nada de culpas.** Si documentar un error se siente como una acusación, nadie va a documentar nada, y perdemos el archivo más valioso que tenemos. La seguridad psicológica está entre los predictores más fuertes del desempeño de un equipo de software. Esto es parte de eso.

---

## Sección precargada: lo que sabemos que nos va a pasar

Estas no son experiencias nuestras todavía. Son los modos de falla documentados de equipos como el nuestro. Están aquí para que no los aprendamos a la mala.

**Cuando alguno nos pase de verdad, se mueve a la sección de arriba con fecha y con el costo real.**

### El PR de 900 líneas que nadie leyó

La IA genera código mucho más rápido de lo que podemos revisarlo. DORA 2024 y 2025 documentan que la adopción de IA aumenta la productividad individual y **degrada la estabilidad de entrega**, porque los changelists crecen y la revisión no alcanza a absorberlos.

Va a pasar así: alguien tendrá prisa, generará una funcionalidad completa en una sesión, abrirá un PR enorme, y quien revise le dará aprobación sin leerlo porque son 900 líneas un domingo en la noche. Tres semanas después nadie entiende esa parte del sistema y nadie se atreve a tocarla.

**Regla:** si no se lee en 20 minutos, se parte antes de abrirse. Aprobar sin leer es peor que no revisar, porque genera una falsa sensación de control.

### Las migraciones en paralelo

Dos personas generan una migración de Django la misma semana sobre tablas relacionadas. Al mergear, conflicto. Resolver conflictos de migraciones es de las cosas más frustrantes que existen y suele terminar en "borremos todo y regeneremos", que en producción no es opción.

**Regla:** una migración por PR, `git pull` de `main` antes de generarla, y el PR se mergea en menos de 24 horas o se cierra.

### Los tres meses en local

Cada quien desarrolla en su máquina, a todos les funciona, y al integrar no funciona nada. Se llama "integration hell" y es exactamente el problema que la integración continua fue inventada para resolver. Con una sesión semanal por persona, un mes de integración dolorosa nos cuesta el proyecto entero.

**Regla:** despliegue en la semana 1, con la app vacía. Merge a `main` despliega solo.

### El alcance que creció sin que nadie lo aprobara

El cliente pide "una cosita más" en una llamada. Quien la recibió dice que sí porque suena chiquita. Nadie lo escribe. Se repite cuatro veces. En el mes tres el proyecto lleva 200 horas en lugar de 120 y nadie sabe en qué momento pasó.

**Regla:** todo cambio de alcance se escribe como issue antes de aceptarse, y quien lo acepta es el dueño de producto, no quien recibió la llamada.

### El proyecto que se abandonó porque apareció algo más interesante

DORA documenta que las prioridades inestables causan caídas de productividad y aumentos de burnout, con un efecto que **persiste incluso con buenos líderes y buena documentación**. Es de los daños más difíciles de revertir.

Va a pasar así: en el mes dos, el proyecto de RH se pone tedioso justo cuando aparece una idea nueva y brillante. Los cuatro se entusiasman. Se abandona lo que estaba a la mitad.

**Regla:** un proyecto a la vez, y se termina. Cambiar de proyecto a media obra nos daña más que haber elegido mal el proyecto.

### El repositorio de documentación como procrastinación colectiva

Escribir documentación se siente productivo, no tiene rechazo posible, no requiere hablar con nadie y no genera un peso. Es el proyecto perfecto para evitar el trabajo incómodo, que es conseguir clientes.

**Regla:** si en una semana el repo de documentación avanzó más que el producto, algo va mal.

### El cliente que "estaba muy interesado"

El interés es gratis. Nadie dice que no a una idea bien contada que no le cuesta nada. La única señal que vale es alguien que dice cuánto pagaría y cuándo.

**Regla:** las 5 preguntas de calificación antes de escribir una línea de código. Ver [pipeline](../comercial/pipeline.md).

### Sam como cuello de botella

El que más sabe termina revisando todos los PRs, hablando con todos los clientes y tomando todas las decisiones técnicas. Se siente responsable, no delega, y en el mes tres es el único que puede desbloquear cualquier cosa. Con una sesión semanal por persona, eso significa que **el equipo entero avanza al ritmo de una persona**.

**Regla:** el proyecto de RH lo lidera quien menos experiencia tiene. Las áreas de decisión se rotan. Sam presupuesta 1 de sus 4 horas en coordinación, explícitamente.

### El trabajo guardado en la laptop

Alguien tiene una rama de tres semanas porque "todavía no está listo para que lo vean". Cuando la abre, ya chocó con todo lo demás y no lo sabía.

**Regla:** ninguna rama vive más de 3 días. El código a medias vive en `main` detrás de una bandera o en una URL que nadie enlaza.

### La decisión que se reabrió en octubre

En agosto se discutió durante 40 minutos si usar HTMX o React. Se decidió HTMX. En octubre entra alguien con una idea, nadie recuerda los argumentos, y se vuelve a discutir 40 minutos. Con nuestro presupuesto de horas, eso es media semana de equipo tirada.

**Regla:** toda decisión que costó discusión se escribe como ADR el mismo día. Los ADRs sustituyen las conversaciones que no podemos tener por los husos horarios.

### La estimación hecha en horas de calendario

Alguien dice "eso son dos días". Son dos días **de trabajo continuo**. A cuatro horas semanales, dos días de trabajo son dos semanas y media de calendario. Todas las promesas al cliente se rompen por esta confusión.

**Regla:** se estima en horas de trabajo y se convierte a calendario dividiendo entre 4 por persona. Siempre.

### WhatsApp como base de datos

Una decisión importante se toma en un hilo de WhatsApp un viernes. Dos meses después nadie la encuentra, y buscar en WhatsApp es imposible. Se vuelve a decidir distinto, y ahora hay dos verdades.

**Regla:** WhatsApp solo para avisar que algo se rompió y para el trato humano. Si una conversación produce una decisión, quien la inició abre el ADR ese mismo día.

---

## Aprendizajes reales

*(Todavía vacío. Se llena con el primer proyecto.)*
