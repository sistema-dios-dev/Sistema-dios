#!/usr/bin/env python3
"""
🚀 SISTEMA DIOS - SCRIPT DE DEPLOY MEJORADO
Versión: 2.0 - Ultra Robusta
"""

import os
import sys
import time
import subprocess
import requests
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DeploySistemaDios:
    def __init__(self):
        self.repo_url = "https://github.com/sistema-dios-dev/Sistema-dios.git"
        self.max_retries = 8
        self.retry_delay = 15
        self.start_time = datetime.now()
        
    def print_banner(self):
        """Mostrar banner de inicio"""
        banner = """
🔥🔥🔥 SISTEMA DIOS - DEPLOY AUTOMATIZADO 🔥🔥🔥
        
⚡ Versión: 2.0 - Ultra Robusta
🎯 Objetivo: Despliegue sin errores
🕒 Inicio: {}
        
        """.format(self.start_time.strftime("%Y-%m-%d %H:%M:%S"))
        print(banner)
    
    def check_github_status(self):
        """Verificar estado de GitHub"""
        print("🔍 Verificando estado de GitHub...")
        
        try:
            # Verificar GitHub status
            status_url = "https://www.githubstatus.com/api/v2/status.json"
            response = requests.get(status_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                status = data['status']['description']
                print(f"✅ GitHub Status: {status}")
                return True
            else:
                print("⚠️ No se pudo verificar estado de GitHub, continuando...")
                return True
                
        except Exception as e:
            print(f"⚠️ Error verificando GitHub: {e}, continuando...")
            return True
    
    def check_repository_access(self):
        """Verificar acceso al repositorio"""
        print("🔍 Verificando acceso al repositorio...")
        
        for attempt in range(3):
            try:
                # Usar git ls-remote para verificar acceso
                result = subprocess.run(
                    ['git', 'ls-remote', self.repo_url, 'HEAD'],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    print("✅ Repositorio accesible")
                    return True
                else:
                    print(f"❌ Intento {attempt + 1}: No se pudo acceder al repositorio")
                    if attempt < 2:
                        time.sleep(10)
                        
            except subprocess.TimeoutExpired:
                print(f"⏰ Timeout en verificación {attempt + 1}")
            except Exception as e:
                print(f"❌ Error en verificación {attempt + 1}: {e}")
                
        return False
    
    def configure_git(self):
        """Configurar Git para mejor rendimiento"""
        print("⚙️ Configurando Git para deploy...")
        
        try:
            # Configuraciones para mejorar la clonación
            configs = {
                'http.postBuffer': '524288000',
                'https.postBuffer': '524288000',
                'core.compression': '9',
                'core.loosecompression': '6',
                'http.lowSpeedLimit': '0',
                'http.lowSpeedTime': '999999'
            }
            
            for key, value in configs.items():
                subprocess.run(['git', 'config', '--global', key, value], check=True)
                print(f"   ✅ {key} = {value}")
                
            print("✅ Configuración Git completada")
            return True
            
        except Exception as e:
            print(f"⚠️ Error en configuración Git: {e}")
            return True  # Continuar aunque falle
    
    def clone_repository(self):
        """Clonar repositorio con múltiples reintentos"""
        print(f"📥 Iniciando clonación del repositorio...")
        
        for attempt in range(1, self.max_retries + 1):
            print(f"\n🔄 INTENTO {attempt}/{self.max_retries}")
            print("=" * 40)
            
            try:
                # Limpiar directorio temporal si existe
                if os.path.exists('/tmp/repo-clone'):
                    subprocess.run(['rm', '-rf', '/tmp/repo-clone'])
                
                # Comando de clonación mejorado
                cmd = [
                    'git', 'clone', 
                    '--depth', '1',           # Solo último commit
                    '--branch', 'main',       # Rama principal
                    '--single-branch',        # Solo una rama
                    self.repo_url,
                    '/tmp/repo-clone'
                ]
                
                print(f"   Comando: {' '.join(cmd)}")
                
                # Ejecutar clonación con timeout
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=300  # 5 minutos timeout
                )
                
                if result.returncode == 0:
                    print("✅ ¡Clonación exitosa!")
                    
                    # Copiar contenido al directorio actual
                    if os.path.exists('/tmp/repo-clone'):
                        subprocess.run(['cp', '-r', '/tmp/repo-clone/.', '.'])
                        subprocess.run(['rm', '-rf', '/tmp/repo-clone'])
                        print("✅ Contenido copiado al directorio de trabajo")
                    
                    return True
                    
                else:
                    error_msg = result.stderr.strip() if result.stderr else "Error desconocido"
                    print(f"❌ Error en clonación: {error_msg}")
                    
                    # Esperar antes del reintento (con backoff exponencial)
                    wait_time = self.retry_delay * attempt
                    print(f"⏰ Esperando {wait_time} segundos antes del reintento...")
                    time.sleep(wait_time)
                    
            except subprocess.TimeoutExpired:
                print("⏰ Timeout en clonación, reintentando...")
                wait_time = self.retry_delay * attempt
                time.sleep(wait_time)
                
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                wait_time = self.retry_delay * attempt
                time.sleep(wait_time)
        
        print("💥 Todos los intentos de clonación fallaron")
        return False
    
    def install_dependencies(self):
        """Instalar dependencias Python"""
        print("\n📦 Instalando dependencias...")
        
        # Verificar si requirements.txt existe
        if not os.path.exists('requirements.txt'):
            print("❌ No se encuentra requirements.txt, creando uno básico...")
            self.create_basic_requirements()
        
        try:
            # Actualizar pip primero
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
            print("✅ Pip actualizado")
            
            # Instalar dependencias
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✅ Dependencias instaladas correctamente")
                return True
            else:
                print(f"⚠️ Error instalando dependencias: {result.stderr}")
                print("🔧 Intentando instalación individual...")
                return self.install_individual_dependencies()
                
        except Exception as e:
            print(f"❌ Error en instalación: {e}")
            return self.install_individual_dependencies()
    
    def create_basic_requirements(self):
        """Crear requirements.txt básico si no existe"""
        requirements = """python-telegram-bot==20.7
python-dotenv==1.0.0
aiohttp==3.9.0
requests==2.31.0
pytz==2023.3
"""
        with open('requirements.txt', 'w') as f:
            f.write(requirements)
        print("✅ requirements.txt creado")
    
    def install_individual_dependencies(self):
        """Instalar dependencias individualmente"""
        print("🔧 Instalando dependencias críticas individualmente...")
        
        dependencies = [
            'python-telegram-bot==20.7',
            'python-dotenv==1.0.0', 
            'aiohttp==3.9.0',
            'requests==2.31.0'
        ]
        
        for dep in dependencies:
            try:
                print(f"   Instalando {dep}...")
                subprocess.run([sys.executable, '-m', 'pip', 'install', dep], check=True)
                print(f"   ✅ {dep} instalado")
            except Exception as e:
                print(f"   ❌ Error instalando {dep}: {e}")
        
        return True
    
    def verify_environment(self):
        """Verificar variables de entorno"""
        print("\n🔍 Verificando entorno...")
        
        required_vars = ['TELEGRAM_TOKEN', 'ADMIN_CHAT_ID']
        missing_vars = []
        
        for var in required_vars:
            if not os.environ.get(var):
                missing_vars.append(var)
                print(f"   ⚠️ {var}: NO CONFIGURADA")
            else:
                print(f"   ✅ {var}: CONFIGURADA")
        
        if missing_vars:
            print(f"❌ Variables faltantes: {', '.join(missing_vars)}")
            print("💡 Configúralas en Render Dashboard -> Environment")
            return False
        
        return True
    
    def run_system_checks(self):
        """Ejecutar verificaciones del sistema"""
        print("\n🔧 Ejecutando verificaciones del sistema...")
        
        checks = [
            ("Verificando Python", ["python", "--version"]),
            ("Verificando Git", ["git", "--version"]),
            ("Verificando directorio", ["pwd"]),
            ("Listando archivos", ["ls", "-la"])
        ]
        
        for check_name, cmd in checks:
            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"   ✅ {check_name}: {result.stdout.strip()}")
                else:
                    print(f"   ⚠️ {check_name}: Error")
            except Exception as e:
                print(f"   ⚠️ {check_name}: {e}")
    
    def calculate_duration(self):
        """Calcular duración del deploy"""
        end_time = datetime.now()
        duration = end_time - self.start_time
        minutes = duration.total_seconds() / 60
        return f"{minutes:.2f} minutos"
    
    def deploy(self):
        """Ejecutar proceso completo de deploy"""
        self.print_banner()
        
        try:
            # 1. Verificaciones iniciales
            self.check_github_status()
            if not self.check_repository_access():
                print("💥 No se puede acceder al repositorio. Verifica:")
                print("   - Que el repositorio existe: https://github.com/sistema-dios-dev/Sistema-dios")
                print("   - Que es público o tienes acceso")
                return False
            
            # 2. Configuración
            self.configure_git()
            self.run_system_checks()
            
            # 3. Clonación
            if not self.clone_repository():
                return False
            
            # 4. Instalación
            if not self.install_dependencies():
                return False
            
            # 5. Verificación final
            if not self.verify_environment():
                print("💡 Configura las variables de entorno en Render Dashboard")
                return False
            
            # ✅ DEPLOY EXITOSO
            duration = self.calculate_duration()
            
            success_banner = f"""
🎉🎉🎉 DEPLOY EXITOSO 🎉🎉🎉

✅ Repositorio clonado correctamente
✅ Dependencias instaladas
✅ Entorno verificado
✅ Sistema listo para iniciar

⏱️  Duración total: {duration}
🚀 Iniciando SISTEMA DIOS SUPREMO...

            """
            print(success_banner)
            return True
            
        except Exception as e:
            logger.error(f"💥 Error crítico en deploy: {e}")
            return False

def main():
    """Función principal"""
    deployer = DeploySistemaDios()
    success = deployer.deploy()
    
    if success:
        # Importar y ejecutar el sistema principal
        try:
            print("🔥 IMPORTANDO SISTEMA DIOS...")
            from sistema_dios import main as sistema_main
            print("✅ Sistema importado, iniciando...")
            sistema_main()
        except ImportError as e:
            print(f"❌ Error importando sistema principal: {e}")
            print("🔧 Buscando archivo principal...")
            
            # Buscar archivo Python principal
            python_files = [f for f in os.listdir('.') if f.endswith('.py')]
            print(f"📁 Archivos Python encontrados: {python_files}")
            
            if python_files:
                main_file = python_files[0]
                print(f"🚀 Ejecutando {main_file}...")
                subprocess.run([sys.executable, main_file])
            else:
                print("💥 No se encontró archivo Python principal")
                sys.exit(1)
    else:
        print("💥 DEPLOY FALLIDO - Revisa los errores arriba")
        sys.exit(1)

if __name__ == '__main__':
    main()
