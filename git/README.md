# Comandos básicos do Git

O Git é um sistema de controle de versão distribuído que permite gerenciar e rastrear alterações em arquivos e projetos. A seguir, estão alguns dos comandos básicos do Git e suas respectivas funcionalidades.

## **Configuração inicial**

Para configurar o Git, é necessário definir seu nome de usuário e endereço de e-mail. Isso pode ser feito usando os seguintes comandos:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

## **Criando um novo repositório**

Para começar a usar o Git em um projeto, é necessário criar um repositório. Isso pode ser feito usando o seguinte comando:

```bash
git init
```

## **Adicionar e commitar arquivos**

Depois de inicializar um repositório, é possível adicionar e commitar arquivos usando os seguintes comandos:

```bash
git add <nome-do-arquivo>           # adiciona um arquivo ao índice
git add .                           # adiciona todos os arquivos modificados ao índice
git commit -m "mensagem de commit"  # commita as mudanças com uma mensagem descritiva
```

## **Visualizar o histórico de commits**

Para visualizar o histórico de commits em um repositório, é possível usar o seguinte comando:

```bash
git log
```

## **Desfazer mudanças**

Para desfazer mudanças em um arquivo, é possível usar o seguinte comando:

```bash
git checkout -- <nome-do-arquivo>  # desfaz as mudanças em um arquivo não commitado
```

## **Enviar mudanças para o servidor**

Para enviar mudanças para o servidor, é possível usar os seguintes comandos:

```bash
git remote add origin <url-do-repositório>  # adiciona o repositório remoto
git push -u origin master  # envia as mudanças para o repositório remoto
```

## **Atualizar o repositório local**

Para atualizar o repositório local com as mudanças mais recentes do servidor, é possível usar o seguinte comando:

```bash
git pull
```

## **Branch**

Para criar uma nova branch em um repositório e entrar nela, é possível usar o seguinte comando:

```bash
git branch <nome-da-branch>

```

Para alternar para uma branch existente, é possível usar o seguinte comando:

```bash
git checkout <nome-da-branch>
```

Para criar e alterar uma branch, é possível usar o seguinte comando:

```bash
git checkout -b <nome-da-branch>
```

Para mesclar uma branch com a branch atual, é possível usar o seguinte comando:

```bash
git merge <nome-da-branch>
```


<!--

-->
