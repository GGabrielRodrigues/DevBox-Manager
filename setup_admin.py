import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devbox_project.settings')
django.setup()

from django.contrib.auth.models import User

# Cria um usuário padrão para facilitar o acesso de não-programadores
if not User.objects.filter(username='visitante').exists():
    User.objects.create_user('visitante', 'visitante@example.com', 'DevBox2024')
    print("Usuário 'visitante' criado com a senha 'DevBox2024'")
else:
    print("Usuário 'visitante' já existe e está pronto para uso.")
