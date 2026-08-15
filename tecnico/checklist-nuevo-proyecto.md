# Checklist de nuevo proyecto

**Relacionado:** [Stack por defecto](stack-por-defecto.md), [Protocolo de trabajo](../protocolo-de-trabajo.md)

---

## Fase 0. Esqueleto en producción

**Semana 1. ~8 horas. Una sola persona. Nada más empieza hasta que esto está listo.**

- [ ] Repo privado creado en la organización de GitHub (no en una cuenta personal)
- [ ] Proyecto Django corriendo en local
- [ ] `.env.example` con todas las variables, y `.env` en `.gitignore`
- [ ] Repo conectado a Railway, con Postgres provisionado
- [ ] **Desplegado en producción, con una página que solo dice "hola"**
- [ ] Dominio o subdominio apuntando
- [ ] GitHub Actions corriendo: `ruff check`, `ruff format --check`, `pytest`, `makemigrations --check`
- [ ] Despliegue automático al mergear a `main`
- [ ] `main` protegida: no se puede pushear directo, se requiere 1 aprobación
- [ ] `CLAUDE.md` inicial, con la sección de prohibiciones
- [ ] `docs/decisions/` creada con el ADR 0001
- [ ] `README.md`: cómo levantar en local en menos de 10 minutos
- [ ] Tablero de GitHub Projects creado

**Por qué el despliegue va aquí y no al final:** el primer despliegue siempre duele (variables de entorno, archivos estáticos, migraciones, certificados) y son entre 6 y 10 horas imposibles de estimar. Si lo dejas para la semana 14, ese dolor cae justo cuando ya prometiste una fecha. Si lo haces la semana 1 con una app vacía, no hay presión y no hay nada que romper.

---

## Fase 1. Contratos

**Semana 2. ~8 horas. Dos personas.**

- [ ] Modelo de datos completo, acordado y escrito como ADR
- [ ] Migraciones base aplicadas en producción
- [ ] Apps de Django definidas, una por rebanada vertical
- [ ] URLs raíz definidas
- [ ] `base.html` y navegación mínima
- [ ] Datos de prueba (fixtures o factories)

**Esta fase evita el 80 por ciento de los choques posteriores.** Con el modelo de datos fijo, cuatro personas pueden trabajar en paralelo sin tocarse.

---

## Fase 2. Rebanadas en paralelo

**El grueso del proyecto.**

Cada persona toma una funcionalidad completa, de la base de datos a la pantalla, y la lleva a producción. Nadie se especializa en backend o frontend.

- [ ] Cada rebanada es su propia app de Django
- [ ] Cada rebanada tiene un dueño en el tablero
- [ ] Ninguna rebanada depende de que otra termine primero

---

## Fase 3. Integración y pulido

- [ ] Navegación coherente entre todas las rebanadas
- [ ] Manejo de errores y páginas 404 y 500
- [ ] Textos revisados (nada de "lorem ipsum" ni "TODO")
- [ ] Permisos y roles
- [ ] Datos de prueba realistas para la demo
- [ ] Documentación de entrega al cliente
- [ ] Respaldo de base de datos configurado
- [ ] Entrada en [aprendizajes.md](aprendizajes.md)

---

## Antes de dar por cerrado

- [ ] El cliente lo está usando, no solo lo vio en una demo
- [ ] Alguien más que nosotros puede operarlo
- [ ] Está claro qué pasa con el mantenimiento y quién lo paga
- [ ] Ficha del proyecto actualizada en [proyectos/](../proyectos/)
