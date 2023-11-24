# YoutubeDownload

Utilizando Python, juntamente com as bibliotecas Tkinter(interface grafica) e Pytube(pegar dados do YouTube)
temos um script para baixar videos ou apenas o audio do video.

Obs: Pode dar erro caso o video que voce quer baixar tenha restriçao de idade 

Feature 1 - Combobox format
- Adiciona uma combobox com os valores
['Video','MP3'], para selecionar, assim poderá 
escolher o tipo de arquivo

Feature 2 - Button See
- adiciona um botao "Ver" que ao ser ativado
mostra o video do video que deseja e a quantidade de views

Feature 3 - Button Download
- ao colar o link que deseja e ver o seu titulo e views
ao apertar o botao Download baixará
o arquvio no formato que desejou, o arquivo
ira aparecer no mesmo diretorio em que esta
o arquivo .py

# Tutorial para conectar ao banco de dados
Para se conectar ao banco de dados local 
utilize algum SGDB de sua preferencia (Sistema de gerenciamento de banco de dados)
podendo ser DBeave,PGadmin, entre outros.

## Credenciais 
```bash
  HOST: localhost
  Porta: 5432
  Baco de dados:notedb
  Usuario: postgres
  Senha:Kaju
```

Abra o docker desktop, verifice se o container postgress esta rodando
após isso tente conectar ao banco de dados. O banco de dados estará vazio.

![dwmb](https://github.com/CaioSantdev/YoutubeDownload/assets/73500497/0af5a680-e66e-4d86-8f24-14af9b64c80c)


## *Possiveis erros:*

Caso você tenha o postgres instalado na sua maniquina ele estará tambem
usando a porta 5232, resultando em conflito caso tente se conectar.

abre seu cmd como administrador e rode o comando: 
```bash
  netstat -ano | findstr :5432
```
![dwmbcmd](https://github.com/CaioSantdev/YoutubeDownload/assets/73500497/1e5b419f-f6f1-40ba-aed2-4291e273e38f)

"mate" o processo com os dois endereços da ulima coluna

execute os seguintes comando: 
```bash
  taskkill /PID **** /F 
```
```bash
  taskkill /PID ***** /F
```
Tente se conectar novamente ao banco de dados.
