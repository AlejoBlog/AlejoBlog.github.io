window.addEventListener('scroll', () => {
  const btn = document.getElementById('toTop');
  if (btn) btn.style.display = window.scrollY > 300 ? 'block' : 'none';
});

document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('toTop');
  if (btn) btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  document.querySelectorAll('.menu-contenedor a').forEach(a => {
    a.addEventListener('click', () => {
      const c = document.getElementById('menu-toggle');
      if (c) c.checked = false;
    });
  });

  iniciarGaleriaAmpliada();
});

function iniciarGaleriaAmpliada() {
  const enlaces = Array.from(document.querySelectorAll('.gallery-link'));
  if (!enlaces.length) return;

  let indiceActual = 0;
  let ultimoFoco = null;

  const visor = document.createElement('div');
  visor.className = 'gallery-lightbox';
  visor.setAttribute('role', 'dialog');
  visor.setAttribute('aria-modal', 'true');
  visor.setAttribute('aria-label', 'Visor ampliado de fotografías');
  visor.innerHTML = `
    <div class="gallery-lightbox__dialog">
      <div class="gallery-lightbox__topbar">
        <span class="gallery-lightbox__title"></span>
        <button class="gallery-lightbox__button gallery-lightbox__close" type="button">Volver a la galería</button>
      </div>
      <div class="gallery-lightbox__stage">
        <button class="gallery-lightbox__arrow gallery-lightbox__arrow--prev" type="button" aria-label="Foto anterior">‹</button>
        <img class="gallery-lightbox__image" src="" alt="">
        <button class="gallery-lightbox__arrow gallery-lightbox__arrow--next" type="button" aria-label="Foto siguiente">›</button>
      </div>
      <div class="gallery-lightbox__bottombar">
        <span class="gallery-lightbox__counter"></span>
        <span>Usa ← y → para moverte, Esc para volver.</span>
      </div>
    </div>
  `;
  document.body.appendChild(visor);

  const imagen = visor.querySelector('.gallery-lightbox__image');
  const titulo = visor.querySelector('.gallery-lightbox__title');
  const contador = visor.querySelector('.gallery-lightbox__counter');
  const cerrar = visor.querySelector('.gallery-lightbox__close');
  const anterior = visor.querySelector('.gallery-lightbox__arrow--prev');
  const siguiente = visor.querySelector('.gallery-lightbox__arrow--next');

  function pintar() {
    const enlace = enlaces[indiceActual];
    const texto = enlace.dataset.title || enlace.querySelector('img')?.alt || 'Fotografía de la galería';
    imagen.src = enlace.href;
    imagen.alt = texto;
    titulo.textContent = texto;
    contador.textContent = `Foto ${indiceActual + 1} de ${enlaces.length}`;
  }

  function abrir(indice, origen) {
    indiceActual = indice;
    ultimoFoco = origen || document.activeElement;
    pintar();
    visor.classList.add('is-open');
    document.body.classList.add('lightbox-open');
    cerrar.focus();
  }

  function volver() {
    visor.classList.remove('is-open');
    document.body.classList.remove('lightbox-open');
    imagen.removeAttribute('src');
    if (ultimoFoco && typeof ultimoFoco.focus === 'function') ultimoFoco.focus();
  }

  function mover(pasos) {
    indiceActual = (indiceActual + pasos + enlaces.length) % enlaces.length;
    pintar();
  }

  enlaces.forEach((enlace, indice) => {
    enlace.addEventListener('click', evento => {
      evento.preventDefault();
      abrir(indice, enlace);
    });
  });

  cerrar.addEventListener('click', volver);
  anterior.addEventListener('click', () => mover(-1));
  siguiente.addEventListener('click', () => mover(1));

  visor.addEventListener('click', evento => {
    if (evento.target === visor) volver();
  });

  document.addEventListener('keydown', evento => {
    if (!visor.classList.contains('is-open')) return;
    if (evento.key === 'Escape') volver();
    if (evento.key === 'ArrowLeft') mover(-1);
    if (evento.key === 'ArrowRight') mover(1);
  });
}
