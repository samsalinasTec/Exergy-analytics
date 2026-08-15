# CLAUDE.md

Reglas de trabajo obligatorias para Claude Code en este repositorio.

Estas reglas no admiten excepciones. La única forma de saltarse una es que el
usuario lo autorice de forma explícita en la conversación, y esa autorización
aplica solo para esa acción puntual, no para las siguientes.

---

## 1. Prohibido hacer commit sin autorización explícita del usuario

Nunca ejecutes `git commit` por iniciativa propia. Antes de cualquier commit:

1. Muestra al usuario exactamente qué archivos cambiaron y qué contiene cada cambio.
2. Propón el mensaje de commit.
3. Espera a que el usuario diga que sí.

Que el usuario haya autorizado un commit antes **no** autoriza el siguiente.
Cada commit se pide por separado.

Lo mismo aplica a cualquier operación que reescriba historia o toque el remoto:
`git push`, `git push --force`, `git reset --hard`, `git rebase`, borrar ramas.

## 2. Crear siempre una rama cuando se declare una "sesión de trabajo"

Cuando el usuario diga que inicia una **sesión de trabajo**, lo primero que debes
hacer es crear una rama nueva a partir de `main` y trabajar ahí. Nunca trabajes
directamente sobre `main`.

```bash
git checkout main
git pull                          # traer lo último del remoto
git checkout -b <nombre-de-rama>   # crear la rama y cambiarse a ella
```

Propón el nombre de la rama al usuario antes de crearla.

> **Qué es una rama:** una copia paralela e independiente del proyecto. Los
> cambios que hagas dentro de ella no afectan a `main` hasta que se integren
> deliberadamente. Sirve para que el trabajo en curso, que puede estar a medias
> o roto, nunca ensucie la versión estable del repositorio.

## 3. Pedir el Pull Request al cerrar cada sesión de trabajo

Al terminar una sesión de trabajo, es **tu deber** preguntarle al usuario si
quiere que se abra el Pull Request de esa rama. No lo abras por tu cuenta:
pregunta y espera respuesta.

Puede haber sesiones que terminen sin cerrar la rama, porque el trabajo sigue
pendiente para otro día. Eso es válido y esperado. Aun así **debes preguntar**,
salvo que el usuario te haya indicado lo contrario para esa rama en particular.

> **Qué es un Pull Request (PR):** una solicitud formal para integrar los cambios
> de tu rama dentro de `main`. Abre un espacio donde el equipo puede revisar,
> comentar y aprobar el trabajo antes de que se incorpore. Es el punto de
> control de calidad del repositorio.

## 4. Explicar con lujo de detalle

Tu obligación es que el usuario entienda por completo lo que dices y lo que
haces. No basta con que la respuesta sea correcta: tiene que quedar entendida.

Explica todo, y muy especialmente los temas técnicos, **como si el usuario fuera
un desarrollador junior con muy pocos conocimientos técnicos**:

- Define cada término técnico la primera vez que lo uses.
- Explica el *porqué* de cada acción, no solo el *qué*.
- Al mostrar un comando, di qué hace y qué va a pasar al ejecutarlo.
- Si algo salió mal, explica la causa real, no solo el síntoma.
- Nunca des por supuesto que el usuario ya conoce una herramienta o un concepto.

Es preferible sobrexplicar a dejar un hueco de comprensión.

## 5. Prohibido hacer cualquier cosa que el usuario no haya pedido

Haz exactamente lo que el usuario pidió. Ni más, ni menos.

Queda prohibido, sin pedirlo antes:

- Crear archivos, carpetas o configuración que no se solicitaron.
- Añadir contenido inventado o "de relleno" a un archivo.
- Reorganizar, renombrar o borrar cosas por criterio propio.
- Instalar dependencias o herramientas.
- Modificar archivos que quedan fuera de lo que se pidió.
- Ejecutar acciones adicionales "de una vez ya que estamos".

Si detectas algo que crees que conviene hacer, **dilo y espera respuesta**. Una
sugerencia se escribe en el chat; nunca se ejecuta por adelantado.

Si la instrucción del usuario es ambigua, la regla es **preguntar**, no elegir
por él la interpretación que te parezca más razonable.
