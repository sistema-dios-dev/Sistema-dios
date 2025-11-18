#!/bin/bash
set -e

echo "🚀 Iniciando despliegue del Sistema Dios..."

# Solucionar posibles problemas de Git
git config --global http.postBuffer 524288000
git config --global https.postBuffer 524288000

# Intentar clonación con reintentos
for i in {1..5}; do
    echo "🔄 Intento de clonación $i/5..."
    if git clone --depth 1 https://github.com/sistema-dios-dev/Sistema-dios.git /tmp/repo-clone; then
        echo "✅ Clonación exitosa!"
        cp -r /tmp/repo-clone/* .
        rm -rf /tmp/repo-clone
        break
    else
        echo "❌ Falló el intento $i, reintentando en 10 segundos..."
        sleep 10
    fi
done

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "🎉 Build completado!"
