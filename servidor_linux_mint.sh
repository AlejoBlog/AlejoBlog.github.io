#!/usr/bin/env bash
set -e

PUERTO="${1:-8080}"
CARPETA_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$CARPETA_SCRIPT"

echo "Servidor local iniciado para el proyecto de Alejo."
echo "Abre esta dirección en tu navegador: http://localhost:${PUERTO}"
echo "Para detenerlo, vuelve a esta terminal y pulsa Ctrl + C."

if command -v xdg-open >/dev/null 2>&1; then
  (sleep 1; xdg-open "http://localhost:${PUERTO}" >/dev/null 2>&1 || true) &
fi

python3 -m http.server "$PUERTO"
