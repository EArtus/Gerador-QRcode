# Gerador de QR Code

Este projeto é um aplicativo web simples que gera QR Codes a partir de URLs fornecidas pelo usuário. Desenvolvido em Python, o aplicativo utiliza as bibliotecas [Streamlit](https://streamlit.io/), [qrcode](https://pypi.org/project/qrcode/) e [Pillow](https://pillow.readthedocs.io/en/stable/).

## Funcionalidades

- **Geração de QR Code:** Insira uma URL e o aplicativo gera automaticamente o QR Code correspondente.
- **Visualização imediata:** O QR Code é exibido na tela para que o usuário possa conferi-lo.
- **Download da imagem:** Permite baixar o QR Code gerado no formato PNG.

## Pré-requisitos

- **Python 3** instalado.
- **Dependências:** As dependências estão listadas no arquivo `requirements.txt` e incluem:
  - `streamlit`
  - `qrcode`
  - `Pillow`

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo:**

   ```bash
   streamlit run app.py
   ```

## Como usar

Ao executar o aplicativo, uma interface web será aberta:

- Digite ou cole a URL desejada no campo de entrada.
- O QR Code correspondente à URL será gerado e exibido.
- Clique no botão "Baixar QRcode" para salvar a imagem no seu dispositivo.
