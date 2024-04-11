#!/bin/bash

echo "[+] Setting up NPM..."
npm init -y
echo "[+] Installing TailwindCSS..."
npm i tailwindcss
echo "[+] Creating tailwind.config.js..."
npx tailwindcss init

read -p "Do you want to use daisyui, kutty, preline, rippleui, none, all or custom? " choice

update_config() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "$1" tailwind.config.js
    else
        sed -i "$1" tailwind.config.js
    fi
}

update_build_script() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "$1" package.json
    else
        sed -i "$1" package.json
    fi
}

case $choice in
    daisyui)
        echo "[+] Installing DaisyUI..."
        npm i -D daisyui@latest
        echo "[+] DaisyUI installed successfully"
        echo "[+] Adding DaisyUI to tailwind.config.js"
        update_config 's|plugins: \[|plugins: \[require("daisyui"), |'
        ;;
    kutty)
        echo "[+] Installing Kutty..."
        npm install kutty --save
        echo "[+] Kutty installed successfully"
        echo "[+] Adding Kutty to tailwind.config.js"
        update_config 's|plugins: \[|plugins: \[require("kutty"), |'
        ;;
    preline)
        echo "[+] Installing Preline..."
        npm i preline
        echo "[+] Preline installed successfully"
        echo "[+] Adding Preline to tailwind.config.js"
        update_config 's|plugins: \[|plugins: \[require("preline/plugin"), |'
        echo "[+] Adding Preline to content in tailwind.config.js"
        update_config 's|content: \[|content: \["node_modules/preline/dist/*.js", |'
        ;;
    rippleui)
        echo "[+] Installing RippleUI..."
        npm install rippleui
        echo "[+] RippleUI installed successfully"
        echo "[+] Adding RippleUI to tailwind.config.js"
        update_config 's|plugins: \[|plugins: \[require("rippleui"), |'
        ;;
    none)
        ;;
    all)
        echo "[+] Installing all plugins..."
        npm i -D daisyui@latest kutty preline rippleui
        echo "[+] All plugins installed successfully"
        echo "[+] Adding all plugins to tailwind.config.js"
        update_config 's|plugins: \[|plugins: \[require("daisyui"), require("kutty"), require("preline/plugin"), require("rippleui"), |'
        echo "[+] Adding Preline to content in tailwind.config.js"
        update_config 's|content: \[|content: \[require("node_modules/preline/dist/*.js"), |'
        ;;
    custom)
        read -p "Enter the names of the plugin you want to use: " plugin
        npm i $plugin
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

read -p "Where are your template files located? (default: ./templates/) Please put the full route including the . and /s " templates
echo "[+] Adding templates to tailwind.config.js"
update_config "s|content: \[|content: \['$templates*.html', |"

read -p "Enter your static file path (./static/) Please put the full route including the . and /s " static

echo "[+] Creating the css folder and input.css file..."

inputcss="${static}css/input.css"
mkdir -p "${static}css"
touch "$inputcss"
echo "[+] CSS folder and input.css file created successfully"
echo "[+] Adding tailwind directives to input.css"
echo "@tailwind base;
@tailwind components;
@tailwind utilities;" >> "$inputcss"
echo "[+] Tailwind directives added successfully"

echo "[+] Starting Build Process..."
outputcss="${static}css/output.css"
echo "[+] Output file will be located at $outputcss"
echo "[-] <link href=\"{{url_for('static',filename='css/output.css')}}\" rel=\"stylesheet\"> is the link to the css file to be included in your html files"

echo "[+] Setting up the build script..."
update_build_script "s|\"scripts\": {|\"scripts\": {\n\"buildcss\": \"npx tailwindcss -i $inputcss -o $outputcss --watch\",|"


echo "[+] Build script is ready to use. Run npm run buildcss to build the css file"

echo "[+] Done!"