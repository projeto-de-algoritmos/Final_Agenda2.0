# Final_Agenda2.0

**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno 
| -- | -- | 
| 18/0018159  |  Guilherme Veríssimo Cerveira Braz | 
| 18/0108344  |  Rafael Berto Pereira | 

## Sobre 
O Objetivo deste trabalho é melhorar a implementação da agenda de tarefas que foi implementada no módulo de algorítimo ambicioso.

Além do algoritimo de Interval Scheduling na agenda, iremos utilizar uma inferencia de grafos para calcular a estimativa de duração de uma tarefa para depois organizar na agenda.

Se todas as categorias forem marcadas o grafo gerado será algo parecido com a imagem a seguir:
![grafo](img/grafosCategorias.png)

## Screenshots

### Pagina principal
A primeira tela da aplicação. Onde o usuário irá indicar o prazo, marcar as categorias do trabalho, adicionar e/ou excluir trabalhos
![pp](screenshots/principal.png)

### Calendário
Marque o prazo do seu projeto usando o calendário
![cal](screenshots/calendario.png)

### Projeto adicionado
Mensagem após a adição de um novo projeto
![add](screenshots/adicao.png)

### Exclusão de um projeto
Apos clicar no botão de excluir abre-se esse menu
![excl](screenshots/delecao.png)
## Video
Em Breve

## Instalação 
```sh
pip install PySimpleGUI 
```

```sh 
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib 
```

**Linguagem**: Python3 <br>
**Bibliotecas**: 
- PySimpleGUI; 
- google-api-python-client;
- google-auth-httplib2;
- google-auth-oauthlib<br>

**Pre-Requisitos**: Python 3.10.4 <br>
## Uso 
* python main.py
