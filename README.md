# Documentação: DevBox Manager

O **DevBox Manager** é um sistema web funcional desenvolvido em Python e Django, voltado para a organização e catalogação de conhecimento técnico e anotações. Criado para permitir que usuários salvem fragmentos de conhecimento ou guias rapidamente por meio de um sistema de "Caixinhas" vinculadas a "Projetos".

Abaixo detalhamos todas as capacidades desenvolvidas, a estrutura lógica aplicada no código e a composição de seus diretórios.

---

## 1. Funcionalidades do Sistema

O sistema conta com capacidades que garantem a segurança dos dados de cada pessoa e um fluxo completo de manipulação do conhecimento:

- **Autenticação e Segurança (Sessões Privadas):**
  - **Login / Logout:** Entrada no sistema de modo protegido usando o motor built-in do Django.
  - **Privacidade e Isolamento de Dados:** Cada usuário visualiza exclusivamente os projetos e anotações que efetuou. Toda a navegação por URL conta com barreira técnica (`@login_required`) e verificação de propriedade das informações.

- **Gestão Organizacional (Projetos):**
  - **Dashboard Visão Geral:** Tela principal contendo um sumário de todos os projetos na conta, organizados com os mais recentes primeiro.
  - **CRUD Completo:**
    - **Criar** novos projetos (Título e Descrição).
    - **Leitura/Visualização:** Acesso aos detalhes do projeto.
    - **Edição** de dados a qualquer momento.
    - **Exclusão** segura, através de uma tela de confirmação (`confirm_delete.html`), assegurando que tudo dentro do projeto será apagado caso o mesmo seja excluído.

- **Gestão de Anotações (Caixinhas de Conteúdo):**
  - **Organização Relacional:** Todas as "Caixinhas" são construídas e moram obrigatoriamente dentro de um "Projeto" (Agrupador).
  - **CRUD Completo:**
    - **Adicionar:** Inclusão de snippet rico de texto, como anotação, contendo um título e uma descrição curta opcional para fins de rápida localização visual.
    - **Visualização Expandida:** Leitura em página própria detalhando todas as escritas registradas no formato completo.
    - **Modificar / Excluir:** Manipulação independente de cada conteúdo em caso de atualizações de anotações ou obsolescências, também equipado de telas de confirmação.

- **Métricas e Resumos:**
  - **Página de Relatórios:** Um núcleo apartado que processa rapidamente as totalizações analíticas da conta gerando um Report que consolida: "Total de Projetos de sua propriedade" e "Total de Caixinhas arquivadas".

---

## 2. Estrutura Lógica do Sistema

A base lógica segue explicitamente o paradigma de arquitetura de software **MVT (Model-View-Template)**, muito aderente ao framework Django, e modelagem de banco relacional:

### Banco de Dados (Models):
O sistema se ampara em um banco SQLite embutido estruturando-se em três pilares relacionais:
1. **User (Usuário):** Tabela padrão enraizada do Django para cuidar das senhas criptografadas e identificação de perfil.
2. **Project (Projeto):** Possui relação forte de `1:N` (Um para Muitos) com o Usuário. Ou seja, um usuário possui diversos projetos. Armazena as nomenclaturas do agrupamento principal.
3. **ContentBox (Caixinha):** Possui relação forte `1:N` (Um para Vários) com o Projeto. Toda Caixinha de Conteúdo pertence estritamente a um *Project* (através de uma `ForeignKey` que ativa a exclusão em cascata: se o projeto for apagado, as caixinhas o acompanham).

### Controladores (Views) e Formulários (Forms):
- **Views baseadas em Função (`func-based views`):** Toda requisição web interceptada passa pelo `manager/views.py`. Nele as transações do banco de dados ocorrem, assim como a conferência se o formulário preenchido nos inputs do HTML são válidos ou de caráter perigoso (Cross-Site Scripting, etc).
- **Validação com `ModelForms`:** A ligação entre a visualização web e o objeto persistido do banco é facilitado pelo `manager/forms.py` que herdam a estrutura restritiva dos modelos diretamente na tela.

### Roteadores (URLs):
- Rotas objetivas criadas em escopos amigáveis como: `/projeto/<ID>/editar`, garantindo clareza funcional via browser com os verbos de trânsito HTTP padrão (GET para puxar a tela, POST para salvar/deletar a informação).

---

## 3. Explicação da Estrutura de Diretórios

O projeto físico na sua máquina possui divisões estratégicas de arquivos e pastas.

```text
DevBox Manager/                   # Raiz do Espaço de Trabalho (Workspace)
│
├── venv/                         # (Virtual Environment) Isole de dependências, garantindo que o Django não afete a máquina inteira.
├── db.sqlite3                    # Arquivo do Banco de Dados onde as tabelas e linhas dos registros residem (Produzido localmente).
├── manage.py                     # CLI Principal: Script executivo que o admin do sistema usa para iniciar serviços e manutenções do servidor.
├── setup_admin.py                # Utilitário: Script customizado criado para configurar o primeiro admin mestre automaticamente.
├── iniciar_sistema.*             # Facilitadores (.bat / .sh) para clique único (ou terminal simples), garantindo uso por pessoas "não programadoras".
│
├── devbox_project/               # (Settings Core) Central de Configurações Técnicas
│   ├── settings.py               # Orquestração do projeto: Define língua, relógios, templates e conexões de base de dados.
│   ├── urls.py                   # Delegador de Rotas: Ele recebe todos os links acessados e repassa ao App.
│   └── wsgi.py / asgi.py         # Conectores com a Web para caso se queira fazer o deploy no futuro visibilidade global.
│
└── manager/                      # App Funcional: A alma do software, onde a mágica do DevBox acontece de verdade.
    ├── migrations/               # Pasta de trilhas e log das mudanças do banco (arquivos de versionamento do Models).
    ├── templates/manager/        # Front-end (HTML): Todas as telinhas (Views HTML renderizadas) ficam aqui. Contém heranças em comum com um "base.html".
    ├── models.py                 # Arquitetura Estrutural, Classes que originam as tabelas e o relacionamento do banco.
    ├── views.py                  # Lógica de Controle: Validador mental principal, trata autenticações e distribui as informações do backend para o Frontend de cada página.
    ├── forms.py                  # Componente para simplificar e garantir a limpeza do ingresso das inputs dos usuários na plataforma.
    └── urls.py                   # Mapa de tráfego que declara e amarra o que cada caminho digitado no navegador executará de código correspondente na "View".
```

