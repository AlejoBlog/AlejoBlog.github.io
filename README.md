# El Sueño de un Futbolista

Proyecto web personal adaptado para **Alejo Encinas Camacho**, niño de 13 años que sueña con ser futbolista profesional.

La web recoge su trayectoria desde sus inicios como portero en el Ogíjares 89 en la temporada 2018/19, su evolución como jugador de campo gracias al estudio y al entrenamiento diario, y su etapa 2025/26 en el Alhendín como lateral izquierdo y central en Segunda Andaluza Infantil.

## Estructura

- `index.html`: portada del proyecto.
- `html/historia.html`: cronología por temporadas.
- `html/estadisticas.html`: resumen de trayectoria y evolución.
- `html/sobre.html`: perfil personal y deportivo.
- `html/logros.html`, `html/diario.html`, `html/galeria.html`, `html/videos.html`, `html/eventos.html`, `html/contacto.html`: secciones complementarias.

## Identidad visual

La paleta se ha modernizado con azul noche, azul eléctrico, verde césped y acentos lima, creando una identidad visual deportiva, actual y adecuada para Alejo.

## Cómo añadir fotos a las galerías

Cada temporada tiene su propia carpeta dentro de `images/`. Por ejemplo, las fotos de la temporada `2018/19` van en `images/2018-19/`, las de `2019/20` en `images/2019-20/`, y así sucesivamente.

Para añadir nuevas fotos, copia las imágenes en la carpeta de la temporada correspondiente y después ejecuta este comando desde la carpeta principal del proyecto:

```bash
python3 actualizar_galerias.py
```

El actualizador revisará automáticamente las carpetas de imágenes y regenerará las páginas `html/galeria-*.html`. Todas las miniaturas se mostrarán con el mismo tamaño gracias a los estilos incluidos, aunque las fotos originales tengan proporciones distintas.

## Cómo ver la web en Linux Mint

Desde la carpeta principal del proyecto ejecuta:

```bash
python3 -m http.server 8080
```

Después abre el navegador en:

```text
http://localhost:8080
```

Para detener el servidor, vuelve a la terminal y pulsa `Ctrl + C`.

## Mejoras incluidas en las galerías

Las galerías permiten cambiar directamente de una temporada a otra sin volver al índice principal. Al pulsar una fotografía se abre un visor ampliado con botón **Volver a la galería**, flecha para avanzar, flecha para retroceder, contador de fotos y navegación con teclado mediante `←`, `→` y `Esc`.

## Portada actualizada

La pantalla principal incorpora `images/alejo-portada.png` como imagen hero integrada mediante degradados, máscaras visuales y mezcla de color para respetar la paleta azul, verde y lima del proyecto.
