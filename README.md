# Projeto de Automação Smart Campus

Esse é um servidor python para fazer a integração do aplicativo Android com o Arduino

## Descrição

Este projeto é uma aplicação Flask que permite controlar vários dispositivos em uma casa, incluindo o ar condicionado, as luzes e monitorar a capacidade da lixeira e o consumo de energia.

## Instalação

1. Clone este repositório.
2. Instale as dependências usando pip: `pip install -r requirements.txt`
3. Execute o script: `python app.py`

## Uso

A aplicação tem várias rotas que correspondem a diferentes funcionalidades:

- `/`: Esta rota lê e retorna o conteúdo do arquivo 'teste1.txt'.
- `/arcondicionado/ligado=<string:ligado>&tempo=<string:tempo>&auto=<string:auto>`: Esta rota permite controlar o ar condicionado.
- `/luz/luzOnOff=<string:ligadorDesligarLuz>`: Esta rota permite ligar ou desligar as luzes.
- `/lixeira/`: Esta rota retorna a capacidade atual da lixeira.
- `/energia/`: Esta rota retorna o consumo atual de energia.

## Contribuindo

Contribuições são bem-vindas! Se você deseja melhorar o projeto, sinta-se à vontade para fazer um fork deste repositório, fazer suas alterações e criar um pull request.
