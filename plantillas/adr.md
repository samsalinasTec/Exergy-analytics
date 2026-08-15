# Plantilla de ADR (Architecture Decision Record)

Copia este archivo a `decisiones/00XX-titulo-corto.md` (o a `docs/decisions/` si es de un proyecto).

**Máximo 15 líneas de contenido.** Un ADR largo no se lee, y un ADR que no se lee no sirve.

---

```markdown
# 00XX. Título de la decisión

**Fecha:** AAAA-MM-DD
**Estado:** propuesta | aceptada | reemplazada por 00YY
**Propuesta por:** [nombre]

## Contexto
Qué problema teníamos. Dos o tres líneas.

## Decisión
Qué elegimos. Una o dos líneas.

## Alternativas consideradas
Qué más evaluamos y por qué no. Una línea por alternativa.

## Consecuencias
Qué se vuelve más fácil y qué se vuelve más difícil.
```

---

## Qué amerita un ADR

- Una dependencia nueva
- Un cambio de estructura
- Cualquier decisión que costó más de 20 minutos de discusión
- Cualquier cosa que alguien vaya a cuestionar en tres meses

## Qué NO amerita un ADR

- Nombres de variables
- Decisiones que se pueden revertir en una hora
- Cosas que ya están en el [stack por defecto](../tecnico/stack-por-defecto.md)

## Regla de escritura

**El ADR se escribe antes de comunicar la decisión, no después.** Documentar después es un paso que siempre se omite. Se abre el PR con el ADR y lo que se comunica es el enlace.

## Los ADRs no se borran

Si una decisión se revierte, el ADR viejo se marca como `reemplazada por 00YY` y se deja. El historial de por qué cambiamos de opinión es tan valioso como la decisión actual.
