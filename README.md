<a id="readme-top"></a>

<div align="center">
  <h1 align="center">Aplicação Web - Visualização das Escolas de Rio Claro</h1>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#about-project">Sobre o Projeto</a>
        <ul><li><a href="#about-project_architecture">Arquitetura</a></li></ul>
        <ul><li><a href="#about-project_technologies">Tecnologias</a></li></ul>
    </li>
    <li>
      <a href="#modules-features">Módulos e Funcionalidades</a>
        <ul><li><a href="#modules-features_users">Usuários</a></li></ul>
        <ul><li><a href="#modules-features_schools">Escolas</a></li></ul>
        <ul><li><a href="#modules-features_bookmarks">Bookmarks</a></li></ul>
        <ul><li><a href="#modules-features_dashboards">Dashboards</a></li></ul>
    </li>
    <li>
      <a href="#how-to">Como Utilizar</a>
        <ul><li><a href="#how-to_local">Rodar Localmente</a></li></ul>
        <ul>
          <li><a href="#how-to_platform">Plataforma</a></li>
          <ul><li><a href="#how-to_platform__dashboards">Dashboards</a></li></ul>
          <ul><li><a href="#how-to_platform__users">Usuários</a></li></ul>
          <ul><li><a href="#how-to_platform__bookmarks">Bookmarks</a></li></ul>
          <ul><li><a href="#how-to_platform__schools">Escolas</a></li></ul>
          <ul><li><a href="#how-to_platform__logout">Logout</a></li></ul>
        </ul>
    </li>
    <li><a href="#contributors">Contribuidores</a></li>
    <li><a href="#contacts">Contatos</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<a id="about-project"></a>

## Sobre o Projeto

Este projeto foi desenvolvido durante a disciplina de Laboratório de Banco de Dados na UNESP e consiste em uma aplicação web voltada para a expansão e análise de um banco de dados das escolas do município de Rio Claro. O foco está na aplicação de técnicas de modelagem de banco de dados, utilizando diagramas entidade-relacionamento (DER), implementação de consultas e manipulação de dados em SQL, implementação do banco de dados em nuvem, aplicação web, além de outras práticas essenciais para o desenvolvimento de aplicações baseadas em banco de dados.

A aplicação pode ser acessada pelos dados abaixo:
- https://censo-escolar-laboratorio-bd.streamlit.app/
- Login: root@root.com
- Senha: 1234

<a id="about-project_architecture"></a>

### Arquitetura

Este projeto foi desenvolvido utilizando a arquitetura MVC (Model-View-Controller), facilitando a manutenção e expansão da aplicação.

- **Model:** Representa as estruturas de dados e a lógica de acesso ao banco de dados, além de definirem as operações CRUD para cada entidade. Os arquivos estão dentro de `src/models`: `bookmarks.py`, `dashboards.py`, `schools.py` e `user.py`  definem as operações CRUD para cada entidade.

- **View**: A interface do usuário é responsável pela interação com o usuário final, exibindo dados de forma visual e interativa através de dashboards. As views foram implementadas principalmente com streamlit, facilitando o gerenciamento e o acompanhamento dos dados escolares.
Os arquivos estão dentro de `src/views`: `dashboards.py`, `login.py` e `logout.py`. Outras views estão organizadas conforme o contexto que foram aplicadas, dentro de `bookmarks`, `schools`, e `users`, como `user-create`:
  - Bchools: `bookmark-create` e `bookmark-list`;
  - Schools: `school-list`;
  - Users: `user-create`, `user-list` e `user-update`.

- **Controller:** Responsável pela lógica da aplicação e lógica de processamento antes de enviar os dados para a view ou modelo, além de atuar como mediador entre os modelos e as views.
Os controladores essão representados pelos arquivos dentro de `src/controllers`: `bookmarks.py`, `dashboards.py`, `schools.py` e `user.py`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a id="about-project_technologies"></a>

### Tecnologias

- [![Next][Python]][Python-url]
- [![Next][Streamlit]][Streamlit-url]
- [![Next][Mysql]][Mysql-url]
- [![Next][Github]][Github-url]
- [Aiven Cloud](https://aiven.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MODULES AND FEATURES -->
<a id="modules-features"></a>

## Módulos e Funcionalidades

<a id="modules-features_users"></a>

### Usuários
- **Cadastrar Usuário:** Funcionalidade para criar novos usuários, que pode incluir ou não a flag de administrador (is_adm). A criação de usuários está definida tanto no controlador quanto no modelo, utilizando hashing de senha para garantir segurança.

- **Listar Usuários:** Listagem de todos os usuários cadastrados no sistema.

- **Buscar Usuário por ID:** Busca de informações detalhadas de um usuário específico.

- **Atualizar e Excluir Usuário:** Atualizar os dados do usuário ou removê-lo.

- **Autenticação:** Autenticação de um usuário pelo e-mail e senha, diferenciando acesso entre administrador e usuário comum. A função `check_password` é utilizada para verificar a senha fornecida.

- **Criar Super Usuário:** Criar de um usuário administrador (“super usuário”).
  - **Usuário Administrador:**
    - Possui privilégios adicionais para gerenciar o sistema
    - Pode criar, atualizar e excluir usuários, incluindo a possibilidade de definir novos administradores.
    - Tem acesso a funcionalidades administrativas que podem não estar disponíveis para usuários comuns.

  - **Usuário Comum:**
    - Pode criar e gerenciar bookmarks para escolas, listar escolas e visualizar dashboards.
    - Possui acesso restrito às funcionalidades de administração de usuários.

<a id="modules-features_schools"></a>

### Escolas

- **Listar Escolas:** Listagem de todas as escolas cadastradas, podendo utilizar filtros conforme necessidade.

- **Buscar Escola por ID:** Busca de informações detalhadas de uma escola específica.

<a id="modules-features_bookmarks"></a>

### Bookmarks

- **Adicionar Bookmark:** Usuários podem salvar bookmarks de escolas. O sistema verifica se um bookmark já existe antes de adicioná-lo.

- **Listar Bookmarks:** Listagem de todos os bookmarks cadastrados, podendo utilizar filtros conforme necessidade. Os bookmarks são associados às escolas, permitindo visualizar o nome da escola vinculada.

- **Buscar Bookmark por ID:** Busca de informações detalhadas de um bookmark específico através de seu ID.

- **Excluir Bookmark:** Função para remover um bookmark.

<a id="modules-features_dashboards"></a>

### Dashboards

- **Escolas da Cidade:** Listagem das escolas da cidade, com os seguintes atributos:
  - Nome;
  - Status de funcionamento;
  - Município;
  - Localização;
  - Dependência;
  - Níveis atendidos;

- **Visão da Escola:** Mostrar total de alunos, professores e turmas por escola.
  - É possível ordenar as escolas pelo número de alunos, professores ou turmas.

- **Visão de Turmas:** Selecionando uma escola, é listado todas as turmas, mostrando o nome e disciplina referente à turma.

- **Professores e Alunos da Escola:** Selecionando a escola, é listado os professores e alunos pertencentes à escola selecionada

- **Alunos por Etapa de Ensino:** Listagem da quantidade de alunos pertencentes a cada etapa de ensino, mostrando o código da pessoa e o tipo (aluno ou docente).

<!-- GETTING STARTED -->

<a id="how-to"></a>

## Como Utilizar

<a id="how-to_local"></a>

### Rodar Localmente
1. Clonar o repositório na máquina local
2. Criar um banco de dados local com o banco
3. No banco de dados, rode o arquivo `schema.sql`, e depois o arquivo `seed.sql`. Isso fará com que o banco seja criado e populado localmente.
4. Após isso, execute o arquivo `execute_script.py` a partir do comando `python .\execute_script.py`. Isso fara com o banco seja populado mais os arquivos `.csv`.
5. Criar um ambiente virtual com o comando `python -m venv venv`
  5.1 O comando pode ser diferente a depender da versão do python ou SO utilizado
6. Instalar as dependências necessárias, presentes dentro do arquivo `.\requirements.txt`, com o comando `pip install -r .\requirements.txt`
7. Na raiz do projeto, crie a pasta `.streamlit`, e dentro dela crie o arquivo `.secrets.toml`
8. Preencha o arquivo com o seguinte código:
    ```
      /* Preencha com os dados do banco de dados local */
      [db_credentials]
      user=""
      password=""
      host=""
      db="censo_escolar"
      port=
    ```
9. Inicialize a aplicação com o comando `streamlit run app.py`
10. Acesse com as credenciais cadastradas no banco

<a id="how-to_platform"></a>

### Plataforma

Após efetuar o login na plataforma na página inicial, o usuário será redirecionado para a tela principal da aplicação, onde terá acesso à um menu lateral com diversas opções para o usuário utilizar a plataforma.

<a id="how-to_platform__dashboards"></a>

#### Dashboard
- Página com a visualização dos gráficos mais importantes da aplicação

<a id="how-to_platform__users"></a>

#### Usuários
- Listagem dos usuários cadastrados
- Cadastro e remoção dos usuários
- Alterar os dados dos usuários cadastrados

<a id="how-to_platform__bookmarks"></a>

#### Bookmarks
- Listagem dos bookmarks cadastrados
- Remoção dos usuários
- Cadastro de novos bookmarks

<a id="how-to_platform__schools"></a>

#### Escolas
- Listagem das escolas cadastradas

<a id="how-to_platform__logout"></a>

#### Logout
Permite o usuário deslogar da aplicação

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

<a id="contributors"></a>

## Contribuidores

<a href="https://github.com/larissa-ferrari/censo-escolar-lab-bd/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Jeferson-Filho/DBLaboratory" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a id="contacts"></a>

<!-- CONTACT -->
## Contatos

Caio Bolhalter <br>
[![LinkedIn][linkedin]][caio-linkedin-url]

Jeferson Filho <br>
[![LinkedIn][linkedin]][jeferson-linkedin-url]

Larissa Ferrari <br>
[![LinkedIn][linkedin]][larissa-linkedin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-url]: https://www.linkedin.com/
[linkedin]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Python-url]: https://www.python.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Streamlit-url]: https://streamlit.io/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
[Mysql-url]: https://www.mysql.com/
[Mysql]: https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white
[Github-url]: https://github.com/
[Github]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[Aiven-url]: https://aiven.io/

[caio-linkedin-url]: https://www.linkedin.com/in/caio-bohlhalter-de-souza-202646232/
[jeferson-linkedin-url]: https://www.linkedin.com/in/jdietrichfho/
[larissa-linkedin-url]: https://www.linkedin.com/in/larissarodriguesferrari/