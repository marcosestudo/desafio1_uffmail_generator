Projeto criado pro processo seletivo do STIUFF. 
Um arquivo csv com nomes, números de matrícula, emails e a informação dizendo se a matrícula está ou não ativa deveria ser lido. 
O programa pede para ser inserido o número de matrícula que será buscado no arquivo. Se a matrícula for encontrada, estiver ativa e o aluno ainda não possuir email acadêmico, são geradas opções de emails de acordo com o nome do aluno.
O email escolhido é inserido no arquivo.

## É necessário ter o Python 3 instalado para rodar o código

## Clone o projeto:

```
git clone https://github.com/marcosestudo/desafio1_uffmail_generator.git
```

## Vá para a pasta:

```
cd desafio1_uffmail_generator
```

## Para abrir a aplicação, use o comando:

```
python main.py
```

## Para rodar os testes, use o comando:

```
python -m unittest
```

## ou, para rodar os testes na versão verbose:

```
python -m unittest -v
```

Obs: Os testes foram configurados para os arquivos .csv enviados na solução que está aqui neste no repositório, mas podem ser feitos testes manualmente com qualquer arquivo.

Obs2: Foram usadas somente bibliotecas nativas. Na versão mais recente do Python (3.10.6) todas já estão presentes por padrão. Foram usadas as bibliotecas "future" e "typing" para usar typehints mostrando os formatos de entrada e saída das funções / módulos; "re" para usar expressões regulares; "csv" para leitura e escrita em arquivos .csv; "unicodedata" para remover acentos e trocar "ç" por "c" e "unittest" para criar testes unitários.