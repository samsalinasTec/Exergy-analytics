# 0001. Documentación en Markdown y Mermaid, en un repositorio

**Fecha:** 2026-08-14
**Estado:** aceptada
**Propuesta por:** el equipo

## Contexto

Somos cuatro personas en tres husos horarios con una sesión de trabajo por semana cada uno. Todo lo que no está escrito hay que reconstruirlo, y reconstruirlo cuesta más que haberlo escrito. Necesitábamos un formato con enlaces entre documentos que se pudiera navegar como una red, y que no dependiera de una herramienta de pago ni de un servicio externo.

## Decisión

Toda la documentación vive en archivos `.md` dentro de un repositorio de GitHub, con diagramas en Mermaid embebidos y enlaces relativos en Markdown estándar.

Obsidian se usa como visor opcional, configurado para **no** usar wikilinks.

## Alternativas consideradas

- **Notion:** mejor edición, pero es un servicio externo, no versiona por PR y no vive junto al código
- **Wikilinks de Obsidian:** más cómodos de escribir, pero GitHub no los renderiza y la documentación se vería rota para cualquiera que la abra ahí
- **Imágenes exportadas en vez de Mermaid:** se desactualizan y nadie las regenera

## Consecuencias

**Más fácil:** todo se versiona, se revisa por PR, y el mismo archivo se ve bien en GitHub y en Obsidian sin mantener nada duplicado.

**Más difícil:** editar Markdown a mano es más lento que un editor visual, y hay que resistir la tentación de usar plugins de Obsidian que rompen la portabilidad.
