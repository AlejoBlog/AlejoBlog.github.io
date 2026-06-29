# Informe de optimización del proyecto

**Autor:** Manus AI  
**Proyecto:** *El sueño de un futbolista — Alejo Encinas Camacho*  
**Objetivo:** reducir el peso del proyecto manteniendo el diseño, la navegación y la calidad visual apreciable en escritorio y móvil.

## Resumen ejecutivo

Se ha realizado una optimización conservadora del proyecto completo. La mejora principal se ha centrado en las fotografías de mayor tamaño, especialmente las de la temporada **2018/19**, que contenían imágenes originales de cámara con resoluciones de hasta 6016 píxeles y pesos cercanos o superiores a 10 MB por archivo. Estas imágenes se han redimensionado a un máximo de **1920 píxeles por lado mayor** y se han recomprimido con calidad alta, manteniendo los mismos nombres y rutas para no romper las galerías.

Además, dos imágenes PNG grandes de la temporada **2025/26** se han convertido a **WebP** porque eran fotografías sin transparencia. En ese caso sí se actualizaron sus referencias HTML correspondientes. También se eliminaron duplicados exactos no enlazados y archivos auxiliares generados durante la auditoría, conservando únicamente una carpeta de herramientas para un script útil de mantenimiento.

| Métrica | Antes de optimizar | Después de optimizar | Resultado |
|---|---:|---:|---:|
| Tamaño aproximado del proyecto descomprimido | Más de 190 MB | 60,64 MB | Reducción muy significativa |
| Fotografías JPEG/WebP optimizadas | 24 archivos | 24 archivos | Rutas conservadas |
| Ahorro en archivos tratados | 144,35 MB tratados | 8,62 MB finales | 135,72 MB menos en esas imágenes |
| Referencias locales rotas tras cambios | No aplicable | 0 en HTML y 0 en CSS | Validación correcta |
| Problema del nombre en móvil | El nombre podía ocultarse | Nombre visible en dos líneas | Corregido |

## Cambios aplicados

La optimización se ha hecho con un criterio prudente: no se han cambiado nombres de fotografías salvo en dos PNG convertidas a WebP, y en esos casos se han actualizado sus enlaces en la galería correspondiente. Las imágenes grandes de tipo JPEG se han mantenido como JPEG, con el mismo nombre de archivo y una compresión adecuada para web.

| Área | Cambio aplicado | Motivo |
|---|---|---|
| Imágenes 2018/19 | Redimensionado y recomprimido de fotografías muy pesadas | Reducir drásticamente el tamaño del proyecto sin perder calidad visible en web |
| Imágenes 2025/26 | Conversión de `i24.png` e `i25.png` a `i24.webp` e `i25.webp` | Eran fotografías sin transparencia; WebP reduce mucho el peso |
| HTML galería 2025/26 | Actualizadas las referencias de esas dos imágenes | Evitar enlaces rotos tras la conversión |
| Duplicados exactos | Eliminados `css/components1.css` y `html/contacto1.html` | No estaban enlazados y eran copias exactas |
| Temporales de auditoría | Eliminados scripts y resultados intermedios innecesarios | Dejar el proyecto más limpio |
| Validación móvil | Confirmado que `AE` y `Alejo Encinas Camacho` aparecen juntos | Mantener la corrección solicitada previamente |

## Validación realizada

Después de la optimización se ha ejecutado una validación automática de referencias locales en todos los HTML principales y en los CSS. El resultado fue correcto: **0 referencias inexistentes en HTML** y **0 referencias inexistentes en CSS**. También se generaron capturas de escritorio y móvil para confirmar que la portada conserva el diseño, el menú fijo y el nombre visible en móvil.

| Prueba | Resultado |
|---|---|
| Revisión de 20 archivos HTML | Correcta |
| Revisión de 8 archivos CSS | Correcta |
| Referencias locales inexistentes en HTML | 0 |
| Referencias locales inexistentes en CSS | 0 |
| Captura móvil 390 × 844 px | Nombre completo visible junto a `AE` |
| Captura escritorio 1365 × 768 px | Portada y menú conservan el diseño |

## Recomendaciones futuras

El proyecto ya queda bastante más ligero, pero si en el futuro se añaden muchas fotografías nuevas conviene repetir el mismo criterio: usar imágenes de máximo 1600–1920 px para galerías web, guardar JPEG con calidad alta pero optimizada, y usar WebP cuando el navegador de destino lo permita. También sería recomendable, en una fase posterior, unificar las páginas HTML duplicadas o casi duplicadas y separar claramente los archivos de mantenimiento de los archivos publicados.

> La versión entregada prioriza estabilidad: se ha reducido peso sin reestructurar agresivamente el proyecto ni cambiar su diseño visual.
