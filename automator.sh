#!/bin/bash

VENV_DIR="venv"  # Nome do diretório do ambiente virtual

function display_intro() {
    RED='\033[0;31m'
    NC='\033[0m'
    echo -e "${RED}***************************************"
    echo "*                                     *"
    echo "*   Welcome to the Automata Manager   *"
    echo "*                                     *"
    echo "***************************************"
    echo ""
    echo " ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███   "
    echo "▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒ "
    echo "▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒"
    echo "░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  "
    echo "▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒"
    echo "▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░"
    echo "▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░"
    echo "░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░      ░     ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ "
    echo "    ░  ░   ░                  ░ ░         ░         ░  ░            ░ ░     ░     "
    echo ""
}

function create_venv() {
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
    fi
}

function activate_venv() {
    echo "Activating virtual environment..."
    source "$VENV_DIR/bin/activate"
}

function install_dependencies() {
    echo "Installing dependencies..."
    create_venv
    activate_venv
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "Dependencies installed!"
    clear
}

function start_app() {
    echo "Starting FastAPI application..."
    activate_venv
    open_browser
    cd ./api
    uvicorn main:app --reload --port 8000
}

function run_tests() {
    echo "Running tests..."
    activate_venv
    pytest tests/integration
}

function open_browser() {
    local url="$(pwd)/gui/templates/index.html"

    if grep -iqE "(microsoft|WSL)" /proc/sys/kernel/osrelease; then
        local wsl_path=$(echo "$url" | sed 's|/|\\|g')
        local wsl_url="\\\wsl.localhost\Ubuntu$wsl_path"
        echo $wsl_url
        explorer.exe "$wsl_url"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        open "$url"
    else
        xdg-open "$url"
    fi
}

function display_menu() {
    display_intro
    echo "Select an option:"
    echo "1) Start Application"
    echo "2) Install Dependencies"
    echo "3) Run Tests"
    echo "4) Exit"
}

function main() {
    while true; do
        display_menu
        read -p "Enter your choice (1-4): " choice

        case $choice in
            1)
                start_app
                ;;
            2)
                install_dependencies
                ;;
            3)
                run_tests
                ;;
            4)
                echo "Goodbye!"
                exit 0
                ;;
            *)
                echo "Invalid choice, please try again."
                ;;
        esac
    done
}

main