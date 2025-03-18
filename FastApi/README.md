Rest é uma arquitetura, um padrão utilizado para que os sistemas se comuniquem.

Framework é um conjunto de bibliotecas, unidas para determinado fim.

API (Interface de Programação de Aplicações) é um conjunto de ferramentas, definições e protocolos para a criação de aplicações de software.

API Rest e afins são baseadas nos métodos:
GET - Usado para solicitar que um servidor envie um recurso
POST - Envia dados de entrada para o servidor. Normalmente para formulários HTML
PUT - Edita e atualiza documentos em um servidor
PATCH - Atualiza parcialmente um recurso
DELETE - Exclui um recurso

FASTAPI é um framework com o objetivo de construir de maneira rápida e fácil sua API.

INSTALAÇÃO DAS BIBLIOTECAS
<py
pip install fastapi
>

Para nosso servidor local
<py
pip install uvicorn
>

Para executar (colocar no ar) o código localmente, estando na mesma pasta aonde definida a instância FastAPI
<py
uvicorn main:app --reload
>

'--reload' o código reinicia o servidor automaticamente após qualquer modificação e salvá-lo.

Caso queira parar a execução do servidor, pressione as seguintes teclas em sequência 'ctrl+c' no terminal (estou usando o powershell)

Download das bibliotecas que estou usando, utilize:
<py
pip install -r requirements.txt
>

Para adicionar novas versões de bibliotecas, use:
<py
pip freeze > requirements.txt
>

Ele reescreverá o arquivo requirements adicionando todas as bibliotecas instaladas.