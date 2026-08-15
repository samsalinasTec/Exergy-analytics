# Stack por defecto

**Relacionado:** [Checklist de nuevo proyecto](checklist-nuevo-proyecto.md), [Aprendizajes](aprendizajes.md)

---

## El criterio

No elegimos por elegancia ni por lo que sea mejor en abstracto. Elegimos por **horas ahorradas**.

Con unas 7.5 horas productivas de equipo por semana, cada servicio administrado vale más que cualquier decisión arquitectónica bonita. Cada tecnología nueva que alguien tenga que aprender es una curva que compite con aprender a trabajar en equipo y a llevar algo a producción.

**Dos curvas simultáneas es el máximo. Tres es garantía de fracaso.**

---

## El stack

| Capa | Decisión | Por qué |
|---|---|---|
| Backend | Django 5, Python 3.12 | Los cuatro ya pensamos en Python. Trae ORM, migraciones, autenticación, permisos y formularios de fábrica |
| Panel administrativo | Django Admin | Regala el backoffice completo. En un sistema tipo CRUD son ~30 horas que no escribimos |
| Frontend | HTMX + Alpine.js + Tailwind | Interfaces dinámicas devolviendo fragmentos de HTML desde Django, sin una app de JavaScript aparte. Curva: unas 4 horas |
| Arrastrar y soltar | SortableJS | Solo donde haga falta un kanban |
| Base de datos | PostgreSQL administrado | Nunca administramos una base nosotros |
| Despliegue | Railway | PaaS: hacemos push y él construye, despliega y maneja certificados y dominios |
| Tareas programadas | Management commands de Django + cron de Railway | Nada de Celery ni colas |
| Analítica o ML, cuando llegue | FastAPI como servicio aparte | Desacoplado, con su propia frontera |
| CI | GitHub Actions | ruff + pytest + check de migraciones. Menos de 3 minutos |
| Formato de código | ruff format | Para no discutir estilo jamás |
| Tablero | GitHub Projects | Ya viene incluido, y las tarjetas son issues del propio repo |

---

## Lo que NO usamos el primer año

Kubernetes, Terraform, microservicios, Kafka, Celery, Redis, React, Next.js, Django REST Framework, monorepos, arquitectura hexagonal, feature flags, GraphQL.

Todo eso es correcto en una empresa con 40 ingenieros de tiempo completo. Con 16 horas semanales de equipo es suicida.

**Regla:** cualquier dependencia nueva necesita un ADR aprobado. No basta con que sea buena.

---

## Costo de infraestructura

| Concepto | Mensual |
|---|---|
| Railway (app + Postgres) | 5 a 20 USD |
| Dominio | ~1 USD |
| GitHub Actions | Gratis hasta 2,000 minutos en repos privados |

Unos 20 dólares al mes entre cuatro. El costo de **no** tenerlo (descubrir problemas de despliegue en la semana 14) se mide en decenas de horas.

---

## Vocabulario, para que nadie asuma que el otro lo sabe

| Término | Qué es |
|---|---|
| **Desplegar** | Poner una versión del código en el ambiente donde realmente corre. Mientras vive en tu laptop, no existe para nadie |
| **Lote (batch)** | Cuánto cambio va junto en un despliegue. Lote grande: 40 archivos de golpe y 40 sospechosos si algo falla. Lote pequeño: un cambio cada dos días y siempre sabes cuál fue |
| **CI (integración continua)** | En cada push, un servidor corre pruebas y linter automáticamente |
| **CD (entrega continua)** | Al mergear a `main`, se despliega solo, sin que nadie apriete nada |
| **PaaS** | Railway, Render, Heroku. Ahí vive tu app y ellos manejan la infraestructura |
| **IaaS** | AWS, GCP, Azure. Te dan piezas crudas, tú armas todo |
| **Issue** | Un ticket. Título, descripción, comentarios. No tiene nada que ver con código |
| **Pull Request (PR)** | Propuesta de cambio que alguien revisa antes de aceptarla. GitLab le llama Merge Request |
| **Trunk-based** | Una sola rama permanente (`main`) y ramas de trabajo que viven menos de 3 días |
| **Desplegar ≠ publicar** | Una app puede estar en producción, en una URL que nadie conoce y con acceso restringido, durante meses |
