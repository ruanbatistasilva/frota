@echo off
SETLOCAL

REM Caminho do projeto
cd /d "C:\Users\ruan.batista\Downloads\frota"

REM Verifica se a venv já existe
IF NOT EXIST "venv" (
    echo Criando ambiente virtual...
    py -m venv venv
)

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Instala dependências (ignora erros se já estiverem instaladas)
echo Instalando dependências...
pip install -r requirements.txt

REM Inicia a aplicação
echo Iniciando aplicação...
py run.py

ENDLOCAL
pause
