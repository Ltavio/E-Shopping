# E-Shopping

## Descrição:

Nesse projeto realizado em equipe foi desenvolvido uma aplicação backend voltada para a estruturação de uma api de marketplace,com o objetivo de facilitar o usuário a cadastrar sua empresa de uma maneira simples e dinâmica no site da sua empresa, com o auxílio de regras de negócios que deixam a aplicação mais segura e eficaz.
A aplicação contou com a alimentação de bibliotecas como a do mercadopago e gerencianet para o desenvolvimento da funcionalidade de pagamento.

## Regras de negócio utilizadas na aplicação:

- A obtenção do acesso para que um usuário possa cadastrar sua empresa é através de uma permissão concedida por algum dos administradores da aplicação.
- Cadastramento de categorias de produtos e os produtos serão feitos apenas pelas empresas cadastradas na aplicação.
- Usuários apenas poderão prosseguir com produtos para o carrinho, com suas contas de usuários logadas e autenticadas.
- Apenas usuários admin têm privilégios nos acessos das rotas da aplicação. 

## Tecnologias utilizadas:

- black
- click
- dj-database-url
- Django
- django-environ
- django-formtools
- django-otp
- django-phonenumber-field
- django-registration
- django-rest-swagger
- django-softdelete
- django-two-factor-auth
- djangorestframework
- djangorestframework-simplejwt
- drf-spectacular
- environ
- executing
- gerencianet
- gunicorn
- ipdb
- ipython
- itypes
- jedi
- jsonschema
- MarkupSafe
- matplotlib-inline
- mercadopago
- psycopg2-binary
- pycodestyle
- pycryptodome
- PyJWT
- PyQRCode
- pyrsistent
- pytest
- pytest-django
- pytest-testdox
- qrcode
- simplejson
- sqlparse
- stack-data
- uritemplate
- urllib3

## Diagrama da aplicação:

![Diagrama EShopping](https://user-images.githubusercontent.com/96259892/212782437-4f8ba1cf-1efb-45fc-85d1-e5fd6074d040.png)

## Fluxograma da aplicação:

![fluxo grama E-Shopping](https://user-images.githubusercontent.com/96259892/212782222-3e5a728a-d11f-4899-aa14-ba1176bc475f.png)

## Endpoints do serviço:

<table>
    <thead>
        <tr>
            <th>Método</th>
            <th>Endpoint</th>
            <th>Responsabilidade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>POST</td>
            <td>/users</td>
            <td>Criação de usuário</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/users</td>
            <td>Lista todos os usuários</td>
        </tr>
        <tr>
            <td>PATCH</td>
            <td>/users</td>
            <td>Atualiza um usuário</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/users/:id</td>
            <td>Realiza um soft delete no usuário</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/login</td>
            <td>Gera o token de autenticação</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/categories</td>
            <td>Criação de categoria</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/categories/:id/properties</td>
            <td>Lista todos imóveis que pertencem a uma categoria</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/properties</td>
            <td>Criação de um imóvel</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/properties</td>
            <td>Lista todos os imóveis</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/schedules</td>
            <td>Agenda uma visita a um imóvel</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/schedules/properties/:id</td>
            <td>lista todos os agendamentos de um imóvel</td>
        </tr>
    </tbody>
</table>

### Para inicializar a aplicação:

````
yarn dev
````
