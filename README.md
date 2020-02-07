# Desafio_treinamento_Django

Passo a passo django windows

	
#### 1 passo  istalar uma virtual machine   (Virtualenv) usando o comando:
  
	
		pip install virtualenv 
  
  
#### 2 Criando um ambiente Virtual

     
##### 2.1 criar a pasta do projeto 
     

- entrar na pasta em que o projeto esta
criar a pasta do projeto Usando o Comando:
		
````
mkdir django-nome_da_pasta 
````
    
entrar na pasta Usando o comando:
   
  
````
cd django-nome_da_pasta
````
     
##### 2.2 Criar o ambiente virtual dentro da pasta 

.Usar o Comando:
  
``
virtualenv venv
``
  
- Obs: Por convenção,utilizamos o nome venv,mas poderia ser qualquer nome

- Obs: Lembre-se de adicionar venv/ no gitignore para caro a venv seja criada dentro da pasta do projeto, elanão ir para o github

     	
 ##### 2.3  iniciar o ambiente virtual 

.Usar o comando:

``
venv\Scripts\activate 
``

-Obs: Para desativar o virtualenv,basta utilizar o comando:

``
deactivate
``
    
 #### 3  Instalando o Django 

. Usar o comando:

``
		pip install django
``

. Verificar se o Django foi estalado, usar o comando:

``
pip freeze 
``

- Esse comando vai listar todas as dependencias instaladas na venv.
-Sempre que você instalar uma dempêndencia nova, você deve Usar o comando:

``
pip freeze > requirement.txt 
``

- Obs: Esse comando vai escrever as dependdencias num arquivo`chamado requirements.txt´

- Obs: Lembre-se de sempre que baixar o projeto ou mudar de branch usar o comando (com a venv ativada ):

``
pip install -r requirements.txt
``

- Esse comando vai instalar todas as dependências que foram instaladas no projeto.


##### 4 Criando o seu projeto 

     
 ###### 4.1  Criando o projeto Django 

Na pasta onde esta a venv, Usar o Comando:

``
django-admin startproject nome_do_projeto . 
``

- Obs: NÂO ESQUEÇA O PONTO ( . )
. Agora Você criou o projeto e basta entrar na pasta dele.
. Usar o Comando:

``
cd nome_do_projeto 
``
     
##### 4.2  Iniciar uma app 

. No terminal Usar o Comando:

``		
python manege.py startapp core 
``
		
. Core é o app principal do projeto e nós acabamos de criar ele.
. Agora basta ir em 

			 settings.py	
 
que fica localizado no arquivo
				 
	 	nome_do_projeto/nome_do_projeto
           
e colocar no arquivo

     INSTALLED_APPS 
     
o app core, 'core' .

     
 ##### 4.3  Migrações

. Sempre que baixa o projeto ou fazer alterações no model, devem rodar esses comandos:

``
python manage.py makemigrations    
python manage.py migrate     
``

- Esses comandos lidam com as mudanças no banco de dados e muitas vezes seu projeto pode não rodar porque você não utilizou os dois.

     
##### 4.4 Rodando o Projeto 

. Usar o Comando:

``
python manage.py runserver
``
- Com esse comando seu app vai rodar e você sera capaz de ver uma url no terminal. Copiando e colando a url num navegador abrirá uma
	mensagem do django de sucesso.


