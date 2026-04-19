#!/bin/bash
echo "=========================================="
echo "     Iniciando o DevBox Manager..."
echo "=========================================="
echo ""

if [ ! -d "venv" ]; then
    echo "[1/4] Criando ambiente do sistema (isso só acontece na primeira vez)..."
    python3 -m venv venv
fi

echo "[2/4] Ativando ambiente..."
source venv/bin/activate

echo "[3/4] Instalando pacotes base..."
pip install django==4.2.11 > /dev/null 2>&1

echo "[4/4] Preparando banco de dados local e usuário inicial..."
python manage.py makemigrations manager > /dev/null 2>&1
python manage.py migrate > /dev/null 2>&1
python setup_admin.py

echo ""
echo "=========================================="
echo " O DevBox Manager está PRONTO PARA USO!"
echo "=========================================="
echo ""
echo "1. Abra seu navegador de internet"
echo "2. Acesse: http://127.0.0.1:8000"
echo "3. Faça login com usuário: visitante / senha: DevBox2024"
echo ""
echo "[Para desligar o sistema, aperte CTRL+C]"
echo ""
python manage.py runserver
