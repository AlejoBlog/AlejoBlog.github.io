from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
HTML = ROOT / 'html'
IMG = ROOT / 'images'

SEASONS = [
    {'slug': '2025-26', 'label': '2025/26', 'club': 'Alhendín', 'role': 'Lateral izquierdo / central', 'story_title': 'Segunda Andaluza Infantil', 'story': 'Nuevo club y nuevo reto. Empezó como lateral izquierdo, en el tercer partido pasó a central y terminó la temporada jugando todos los minutos hasta el final.'},
    {'slug': '2024-25', 'label': '2024/25', 'club': 'Ogíjares 89', 'role': 'Formación competitiva', 'story_title': 'Infantil', 'story': 'Una etapa de crecimiento físico, táctico y mental dentro del fútbol base, preparándose para competir con mayor exigencia.'},
    {'slug': '2023-24', 'label': '2023/24', 'club': 'Ogíjares 89', 'role': 'Jugador de campo', 'story_title': 'Alevín de segundo año', 'story': 'Temporada de consolidación como jugador, ganando confianza, lectura de juego y compromiso con el equipo.'},
    {'slug': '2022-23', 'label': '2022/23', 'club': 'Ogíjares 89', 'role': 'Jugador de campo', 'story_title': 'Alevín', 'story': 'Nueva categoría y más aprendizaje. Alejo siguió sumando recursos técnicos y competitivos para hacerse importante dentro del grupo.'},
    {'slug': '2021-22', 'label': '2021/22', 'club': 'Ogíjares 89', 'role': 'Jugador de campo', 'story_title': 'Benjamín de segundo año', 'story': 'Una temporada clave para reforzar hábitos de entrenamiento, disciplina y lectura del juego.'},
    {'slug': '2020-21', 'label': '2020/21', 'club': 'Ogíjares 89', 'role': 'Jugador de campo', 'story_title': 'Benjamín', 'story': 'Alejo continuó evolucionando como jugador, aplicando en el campo todo lo aprendido en entrenamientos y vídeos.'},
    {'slug': '2019-20', 'label': '2019/20', 'club': 'Ogíjares 89', 'role': 'Transición a jugador', 'story_title': 'Prebenjamín de segundo año', 'story': 'Después de empezar como portero, quiso ser jugador. Aunque al principio no todos confiaban en que pudiera hacerlo bien, estudió vídeos, entrenó a diario y acabó siendo imprescindible también en el campo.'},
    {'slug': '2018-19', 'label': '2018/19', 'club': 'Ogíjares 89', 'role': 'Portero', 'story_title': 'Prebenjamín', 'story': 'Primer contacto serio con el fútbol. Alejo empezó bajo palos, aprendiendo valentía, reflejos y responsabilidad desde la portería.'},
]

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif', '.bmp', '.tif', '.tiff', '.svg'}
MAIN_PATTERN = re.compile(r'<main class="galeria-temporada">.*?</main>', re.DOTALL)


def sort_key(path: Path):
    match = re.search(r'(\d+)', path.stem)
    return (int(match.group(1)) if match else 10**9, path.name.lower())


def season_nav(active_slug):
    links = []
    for season in SEASONS:
        active = ' active-season' if season['slug'] == active_slug else ''
        aria = ' aria-current="page"' if season['slug'] == active_slug else ''
        links.append(f'<a class="season-pill{active}" href="galeria-{season["slug"]}.html"{aria}>{season["label"]}</a>')
    return f'''
    <section class="season-switcher glass" aria-label="Cambiar de temporada">
      <div>
        <h2>Cambiar de temporada</h2>
        <p>Desde esta página puedes ir directamente a cualquier otra galería sin volver al índice principal.</p>
      </div>
      <div class="season-pills">
        {''.join(links)}
      </div>
    </section>'''


def image_cards(season):
    folder = IMG / season['slug']
    folder.mkdir(parents=True, exist_ok=True)
    images = sorted([p for p in folder.glob('*') if p.is_file() and p.suffix.lower() in IMAGE_EXTS], key=sort_key)
    intro = f'''
      <article class="tarjeta-imagen placeholder-card gallery-info-card">
        <span>{season['label']}</span>
        <h3>{season['club']}</h3>
        <p>{season['role']}</p>
      </article>'''
    if not images:
        return intro + f'''
      <article class="tarjeta-imagen placeholder-card gallery-info-card">
        <span>Fotos</span>
        <h3>Próximamente</h3>
        <p>Añade imágenes en <strong>images/{season['slug']}/</strong> y ejecuta <strong>python3 actualizar_galerias.py</strong>. Se insertarán automáticamente con tamaño uniforme.</p>
      </article>'''
    cards = [intro]
    total = len(images)
    for index, image in enumerate(images, 1):
        src = f'../images/{season["slug"]}/{image.name}'
        title = f'{season["label"]} · Foto {index} de {total}'
        cards.append(f'''
      <figure class="tarjeta-imagen gallery-photo">
        <a class="gallery-link" href="{src}" data-gallery="galeria-{season['slug']}" data-title="{title}">
          <img src="{src}" alt="Alejo Encinas Camacho, {season['label']}, foto {index}" loading="lazy">
        </a>
        <figcaption>{title}</figcaption>
      </figure>''')
    return ''.join(cards)


def build_main(season):
    return f'''<main class="galeria-temporada">
    <section class="gallery-story glass">
      <h2>{season['story_title']}</h2>
      <p>{season['story']}</p>
      <p class="nota">Las fotografías de esta temporada se muestran en miniaturas uniformes. Al pulsar sobre una foto se abre en grande con controles para volver, avanzar y retroceder.</p>
    </section>
    {season_nav(season['slug'])}
    <section class="galeria-grid gallery-grid-enhanced" aria-label="Fotos de la temporada {season['label']}">
      {image_cards(season)}
    </section>
  </main>'''


def main():
    for season in SEASONS:
        path = HTML / f'galeria-{season["slug"]}.html'
        if not path.exists():
            raise FileNotFoundError(path)
        text = path.read_text(encoding='utf-8')
        new_text, count = MAIN_PATTERN.subn(build_main(season), text, count=1)
        if count != 1:
            raise RuntimeError(f'No se pudo actualizar el bloque principal de {path.name}')
        path.write_text(new_text, encoding='utf-8')
        print(f'Actualizada: {path.name}')
    print('Galerías actualizadas correctamente.')


if __name__ == '__main__':
    main()
