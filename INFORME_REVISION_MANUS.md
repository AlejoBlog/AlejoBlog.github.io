# Revisión completa del proyecto “El Sueño de un Futbolista”

**Autor:** Manus AI  
**Fecha de revisión:** 10 de junio de 2026

## Resumen ejecutivo

He revisado el proyecto completo que enviaste, incluyendo la estructura HTML, los estilos CSS, el JavaScript, las galerías y las referencias locales a imágenes y recursos. El sitio está planteado correctamente como una web estática: tiene páginas separadas por secciones, galerías por temporada, un menú común, metadatos descriptivos y una identidad visual coherente con la temática deportiva.

El problema concreto que comentabas en móvil ya está localizado y corregido. En pantallas pequeñas se veía el distintivo **“AE”**, pero no el texto **“Alejo Encinas Camacho”**, porque una regla responsive del archivo `css/media-queries.css` ocultaba expresamente el segundo `span` de la marca. Como el nombre estaba escrito dentro de ese segundo `span`, el navegador hacía exactamente lo indicado por CSS: mostrar “AE” y ocultar el nombre.

> **Causa exacta:** la regla móvil `.brand-mini span:last-child { display: none; }` ocultaba el texto del nombre en dispositivos de hasta 900 px de ancho.

## Correcciones aplicadas

| Área revisada | Problema detectado | Corrección aplicada |
|---|---|---|
| Marca en móvil | El segundo `span` de `.brand-mini`, donde aparece “Alejo Encinas Camacho”, se ocultaba en móvil. | Se cambió la regla para mantenerlo visible y se añadió una anulación final para que, en móviles estrechos, el nombre pueda mostrarse en dos líneas en lugar de desaparecer o cortarse. |
| Galería 2021/22 | Había tres referencias a imágenes inexistentes: `IMG-20260606-WA0025.webp`, `IMG-20260606-WA0026.webp` e `IMG-20260606-WA0027.webp`. | Se sustituyeron por archivos existentes de la misma carpeta: `b219.webp`, `b220.webp` y `b2221.webp`. Después de la corrección, la auditoría indica **0 referencias locales inexistentes**. |
| Caché de CSS | Algunas páginas cargaban `estilos.css` sin versión, por lo que el navegador podía mantener estilos antiguos en caché. | Se añadió una versión común `?v=revision-completa-1` a las referencias de CSS en las páginas HTML. |
| Imágenes principales | Algunas imágenes principales no incluían atributos de decodificación/carga segura. | Se añadieron atributos no invasivos como `decoding="async"` y, donde correspondía, `loading="lazy"`. |
| Validación responsive | Se necesitaba comprobar visualmente la vista móvil tras la corrección. | Se generaron capturas en móvil y escritorio. En móvil ya se lee **“Alejo Encinas Camacho”** junto al distintivo “AE”. |

## Resultado de validación

Después de aplicar las correcciones, se ejecutó de nuevo la auditoría de referencias locales. El resultado fue correcto: no quedan enlaces internos rotos ni referencias CSS inexistentes.

| Validación | Resultado |
|---|---:|
| Referencias locales HTML inexistentes | 0 |
| Referencias locales CSS inexistentes | 0 |
| Captura móvil de portada | Correcta: aparece “AE” y también “Alejo Encinas Camacho”. |
| Captura escritorio de portada | Correcta: el menú conserva el diseño y la portada mantiene la foto fija y centrada. |

## Mejoras recomendadas para una siguiente fase

La mejora más importante pendiente es el **peso de las imágenes**. El proyecto completo ocupa aproximadamente **200 MB**, y la carpeta `images/2018-19` concentra imágenes JPEG muy pesadas, varias de entre 9 MB y 11 MB. Aunque el sitio funciona, en móviles o conexiones lentas esas imágenes pueden tardar mucho en cargar.

| Prioridad | Mejora recomendada | Motivo |
|---:|---|---|
| Alta | Optimizar imágenes grandes y crear versiones WebP ligeras. | Reduciría mucho el peso total del sitio y mejoraría la carga en móvil. |
| Media | Consolidar reglas CSS finales. | Hay varias anulaciones acumuladas con `!important`; funcionan, pero sería más mantenible ordenar el CSS en una versión limpia. |
| Media | Revisar archivos duplicados. | `components1.css` es idéntico a `components.css`, `contacto1.html` es idéntico a `contacto.html` e `index1.html` es casi una copia de `index.html`. Conviene decidir si son copias de seguridad o eliminarlas. |
| Media | Añadir una política clara de nombres de imágenes. | En algunas temporadas los nombres son secuenciales y en otras mezclan formatos. Un patrón estable evita errores de referencia. |
| Baja | Añadir `aria-current="page"` en todos los enlaces activos del menú. | Mejoraría la accesibilidad para lectores de pantalla. |

## Conclusión

El fallo del nombre en móvil no era un problema del HTML ni del navegador: era una regla responsive que ocultaba el segundo `span` de la marca. La versión corregida mantiene visible el distintivo **“AE”** y también el nombre **“Alejo Encinas Camacho”**, adaptándolo a dos líneas cuando el ancho del móvil no permite mostrarlo cómodamente en una sola.

Además, he corregido las referencias rotas detectadas en una galería y he dejado el proyecto preparado para evitar problemas de caché con el CSS. La web queda lista para probar en local y seguir mejorándola, especialmente en la optimización de imágenes si quieres reducir mucho el tamaño total del proyecto.
