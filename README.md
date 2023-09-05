<h1 align="center">
    <img alt="SIGEMH" title="SIGEMH" src="setup/static/images/icon.svg" width="70px" />
</h1>

<h4 align="center">
    SIGEMH
</h4>

## 🚀 Tecnologias
Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## 💻 Projeto
**Sistema de gestão de Engenharia Clínica para cadastro de equipamentos e ordem de serviço.**
<div align="center">
    <img alt="Models" title="Models" src="apps/models.png" width="400px" />
</div>
<p align="center">Models</p>
<hr>

### Pré requisitos
Ter instalado:
- [Python](https://www.python.org/downloads/)
- [Conda](https://conda.io/projects/conda/en/stable/user-guide/install/download.html)


### Run
```sh
# clonar repositório
git clone https://github.com/andre23arruda/sigemh

# Entrar na pasta
cd sigemh

# Instalação
make install

# Executar as migrações
make migrate

# Start
make run
```

## Funcionalidades
- Cadastro de colaboradores da engenharia clínica
- Cadastro de solicitantes de ordem de serviço (enfermeiros, fisioterapeutas e médicos)
- Armazém: controle de produtos, categorias, solicitantes, fornecedores, checkin e checkout
- Cadastro de Locais (setores de serviço da unidade de saúde) e Normas de equipamentos.
- Cadastro de equipamentos: fabricante, tipo de equipamento, modelo de equipamento e fotos.
- Abertura de ordem de serviço (manutenção corretiva) de acordo com equipamento. Com check-in quando um usuário selecionar a OS e checkout ao finalizar.
- Criação automática de ordem de serviço (manutenção preventiva e calibração)

Cada equipamento do quadro de equipamentos da engenharia clínica possui um QR code para acesso de suas informações, histórico e ordem de serviço disponível.
Se o usuário for da engenharia clínica, ao ler o QR code, poderá selecionar uma OS do equipamento para realizar. Ao realizar, pode descrever o trabalho realizado para facilitar futuro trabalho.
Se o usuário for do corpo de saúde, poderá solicitar a abertura de uma OS.

Envio de email para gestor.

Possibilidade de desativar equipamento.

Facilidade de encontrar equipamento, pois este deve ser cadastrado com setor de serviço da Unidade de saúde.