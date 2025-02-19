# tibia
# Timer para Balsa da Hunt Ebb and Flow (Tibia)

Este é um script em Python que implementa um timer para a balsa da hunt *Ebb and Flow* no jogo *Tibia*. O timer exibe uma pequena janela flutuante com uma contagem regressiva de 2 minutos, tocando um alerta sonoro quando restam 10 segundos.

## 📌 Funcionalidades
- Janela flutuante sem bordas e transparente.
- Contagem regressiva automática de 2 minutos.
- Alerta sonoro quando restam 10 segundos.
- Atalhos de teclado:
  - `Espaço` → Iniciar/Retomar o timer.
  - `P` → Pausar o timer.
  - `ESC` → Fechar o timer.
- Arrastar a janela pressionando `Ctrl` + Clique Esquerdo do Mouse.

## 📦 Requisitos

Certifique-se de ter o Python instalado (versão 3.x) e instale as dependências necessárias executando:

```bash
pip install tkinter playsound pillow keyboard
```

## 🚀 Como Usar

1. Salve o código como `timer.py`.
2. Coloque a imagem `relogio.png` na mesma pasta do script.
3. Coloque o arquivo de som `alerta.mp3` na mesma pasta do script.
4. Execute o script:

```bash
python timer.py
```

A janela do timer aparecerá e poderá ser movida pressionando `Ctrl` enquanto arrasta com o mouse.

## 🛠 Possíveis Problemas
- Caso o *playsound* não funcione corretamente no Windows, tente instalar a versão alternativa:

  ```bash
  pip install playsound==1.2.2
  ```
- Se a imagem `relogio.png` não carregar, verifique o nome do arquivo e o diretório.

## 📜 Licença
Este projeto é de uso livre e pode ser modificado conforme necessário.

---
Criado para facilitar a caçada na hunt *Ebb and Flow* no Tibia! 🎮

