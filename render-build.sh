#!/bin/bash
set -e

echo "🚀 INICIANDO BUILD EN RENDER..."
echo "🔍 Python version: $(python --version)"
echo "🔍 Git version: $(git --version)"

# Configurar Python path
export PYTHONPATH="/opt/render/project/src:$PYTHONPATH"

# Ejecutar el script de deploy Python
python deploy.py

echo "🎉 BUILD COMPLETADO EXITOSAMENTE"
