@echo off
setlocal enabledelayedexpansion

:: Função para exibir a introdução
:display_intro
echo ***************************************
echo *                                     *
echo *   Welcome to the Automata Manager   *
echo *                                     *
echo ***************************************
echo.
echo  ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███   
echo  ▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒ 
echo  ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
echo  ░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
echo  ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
echo  ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
echo  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
echo  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░      ░     ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
echo      ░  ░   ░                  ░ ░         ░         ░  ░            ░ ░     ░     
echo.

goto :eof

:: Função para instalar dependências
:install_dependencies
echo Installing dependencies...
:: Instalação do Graphviz no Windows usando choco (Chocolatey), você precisa ter o Chocolatey instalado
choco install graphviz -y
pip install -r requirements.txt
echo Dependencies installed!
cls
goto :eof

:: Função para iniciar o aplicativo
:start_app
echo Starting FastAPI application...
:: Abre o navegador (substitua conforme necessário)
start http://localhost:8000
cd api
uvicorn main:app --reload --port 8000
goto :eof

:: Função para rodar os testes
:run_tests
echo Running tests...
pytest tests\integration
goto :eof

:: Função para exibir o menu
:display_menu
call :display_intro
echo Select an option:
echo 1) Start Application
echo 2) Install Dependencies
echo 3) Run Tests
echo 4) Exit
goto :eof

:: Função principal
:main
:loop
call :display_menu
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    call :start_app
) else if "%choice%"=="2" (
    call :install_dependencies
) else if "%choice%"=="3" (
    call :run_tests
) else if "%choice%"=="4" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice, please try again.
    goto :loop
)

goto :eof
