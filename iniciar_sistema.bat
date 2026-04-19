@echo off
echo ==========================================
echo      Iniciando o DevBox Manager...
echo ==========================================
echo.
if not exist venv (
    echo [1/4] Criando ambiente do sistema (isso so acontece na primeira vez)...
    python -m venv venv
)

echo [2/4] Ativando ambiente...
call venv\Scripts\activate.bat

echo [3/4] Instalando pacotes base...
pip install django==4.2.11 > nul

echo [4/4] Preparando banco de dados local e usuario inicial...
python manage.py makemigrations manager > nul
python manage.py migrate > nul
python setup_admin.py

echo.
echo ==========================================
echo O DevBox Manager esta PRONTO PARA USO!
echo ==========================================
echo.
echo 1. Abra seu navegador de internet
echo 2. Acesse: http://127.0.0.1:8000
echo 3. Faca login com usuario: visitante / senha: DevBox2024
echo.
echo [Para desligar o sistema, feche esta janela ou aperte CTRL+C]
echo.
python manage.py runserver
pause
