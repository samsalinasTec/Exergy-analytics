# Plantilla: diagnóstico de datos

Entregable del peldaño 1 de la [escalera de oferta](../comercial/oferta-y-precios.md).

**Duración:** 2 a 3 semanas. **Esfuerzo:** ~40 horas de equipo.

**Su función real:** es nuestro mejor instrumento de prospección. Es barato para el cliente, de bajo riesgo, y nos da acceso y contexto que ningún competidor tiene. La mitad de nuestro pipeline debería salir de diagnósticos.

---

## Cómo se levanta

### Entrevistas (10 a 12 horas)

Tres perfiles, mínimo:
- Quien vive el proceso todos los días (el que más sabe y al que menos preguntan)
- Quien lo supervisa
- Quien lo paga

Preguntas que siempre se hacen:
1. Descríbeme el proceso como si yo fuera nuevo
2. ¿Qué parte te consume más tiempo?
3. ¿Dónde anotas las cosas? ¿En qué sistema, en qué archivo?
4. ¿Qué pregunta te hacen y no puedes contestar rápido?
5. ¿Qué haces cuando el sistema no te deja hacer algo?
6. Si pudieras cambiar una sola cosa, ¿cuál sería?

La pregunta 5 es la que más revela. Los Excel paralelos y los WhatsApp de coordinación son donde vive el proceso real.

### Inventario de fuentes (8 a 10 horas)

| Fuente | Tipo | Quién la alimenta | Frecuencia | ¿Se usa hoy? | Accesible |
|---|---|---|---|---|---|
| | ERP / SCADA / Excel / correo / papel | | | | |

Buscar específicamente: sistemas que ya existen y nadie consulta, datos que se capturan y se tiran, y reportes que alguien arma a mano cada semana.

**Contexto:** IBM estima que el 90 por ciento de los datos industriales que se recolectan nunca se usan. En energía y utilities, cerca del 68 por ciento de lo que capturan sensores y medidores queda sin procesar. El cuello de botella dominante no es la falta de sensores, es la falta de integración de lo que ya se captura.

### Mapa de casos de uso (8 horas)

Entre 3 y 5, priorizados:

| # | Caso de uso | Valor estimado | Esfuerzo | Datos necesarios | ¿Existen hoy? |
|---|---|---|---|---|---|
| 1 | | | | | |

Priorización simple: valor alto y esfuerzo bajo primero. Nada que requiera datos que no existen todavía.

---

## Estructura del entregable

Máximo 15 páginas, y una sesión de presentación de 45 minutos.

1. **Qué encontramos** (1 página, y es la única que va a leer quien firma)
2. Cómo funciona el proceso hoy, con diagrama Mermaid
3. Inventario de fuentes
4. Dónde se está perdiendo información
5. Casos de uso priorizados
6. Qué recomendamos hacer primero, y por qué
7. Qué haría falta para eso

---

## Regla de honestidad

**Si el diagnóstico concluye que no hay proyecto, se dice.** Nos cuesta una venta y nos gana la reputación que hace que nos recomienden.

Un diagnóstico que siempre concluye "sí, cómprennos el peldaño 2" deja de tener valor en cuanto el cliente lo nota, y lo nota.
