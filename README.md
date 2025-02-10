# Automator
 Este projeto é uma aplicação simples com **backend desenvolvido em FastAPI**, projetada para seguir boas práticas de desenvolvimento e garantir alta testabilidade. A aplicação oferece uma **interface intuitiva** que permite a manipulação e o teste de autômatos de maneira simples e eficiente. 

O sistema é capaz de:

- **Criar autômatos**.
- **Listar autômatos** existentes (todos ou algum específico).
- **Gerar diagramas** que representam os autômatos.
- **Testar autômatos** com uma string de entrada para verificar se a entrada é aceita.

## Como Configurar e Executar

1. Clone o repositório:

    ```bash
    git clone https://github.com/PedroCobucci/automator.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd automator
    ```

3. Instale as dependências:

    Para instalar as dependências, utilize o automator e selecione a **segunda opção**.:

    ```bash
    bash automator.sh
    ## Selecione a 2º Opção
    ```

4. Execute o projeto:

    Para rodar o projeto, utilize o automator e selecione a **primeira opção**.

    ```bash
    bash automator.sh
    ## Selecione a 1º Opção
    ```

    Isso deve iniciar uma instância do seu navegador com o frontend da aplicação. Caso isso não ocorra automaticamente, acesse o index em:
    ```bash
    ./gui/templates/index.html
    ```

5. Documentações

    Acesse `http://127.0.0.1:8000/docs` para utilizar o SWAGGER da aplicação


## Limitações e Pressupostos
 - Embora o projeto teoricamente possa rodar em Windows e Mac, não foi testado para essas plataformas.
 - Os dados são armazenados em memória.

## Exemplos de Uso da API



### Criar Novo Automato

CURL:
```bash
curl --location 'http://127.0.0.1:8000/pushdown_automaton/' \
--header 'sec-ch-ua-platform: "Windows"' \
--header 'Referer;' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0' \
--header 'Accept: */*' \
--header 'sec-ch-ua: "Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"' \
--header 'Content-Type: application/json' \
--header 'sec-ch-ua-mobile: ?0' \
--data '{"name":"1","states":["q0","q1","q2","q3"],"input_symbols":["a","b"],"stack_symbols":["0","1"],"transitions":{"q0":{"a":{"0":["q1",["1","0"]]}},"q1":{"a":{"1":["q1",["1","1"]]},"b":{"1":["q2",""]}},"q2":{"b":{"1":["q2",""]},"":{"0":["q3",["0"]]}}},"initial_state":"q0","initial_stack_symbol":"0","final_states":["q3"],"acceptance_mode":"final_state"}'
```

```bash
POST http://127.0.0.1:8000/pushdown_automaton/
Corpo da requisição:
{
   "name":"1",
   "states":[
      "q0",
      "q1",
      "q2",
      "q3"
   ],
   "input_symbols":[
      "a",
      "b"
   ],
   "stack_symbols":[
      "0",
      "1"
   ],
   "transitions":{
      "q0":{
         "a":{
            "0":[
               "q1",
               [
                  "1",
                  "0"
               ]
            ]
         }
      },
      "q1":{
         "a":{
            "1":[
               "q1",
               [
                  "1",
                  "1"
               ]
            ]
         },
         "b":{
            "1":[
               "q2",
               ""
            ]
         }
      },
      "q2":{
         "b":{
            "1":[
               "q2",
               ""
            ]
         },
         "":{
            "0":[
               "q3",
               [
                  "0"
               ]
            ]
         }
      }
   },
   "initial_state":"q0",
   "initial_stack_symbol":"0",
   "final_states":[
      "q3"
   ],
   "acceptance_mode":"final_state"
}
Resposta:
{
    "message": "Pushdown Automaton created successfully!"
}
```

### Obter Automato

CURL:
```bash
curl --location 'http://127.0.0.1:8000/pushdown_automaton/1' \
--header 'Accept: */*' \
--header 'Accept-Language: pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
--header 'Connection: keep-alive' \
--header 'Origin: null' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: cross-site' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0' \
--header 'sec-ch-ua: "Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"'
```

```bash
POST http://127.0.0.1:8000/pushdown_automaton/{name}
Resposta:
{
    "states": [
        "q1",
        "q2",
        "q3",
        "q0"
    ],
    "input_symbols": [
        "b",
        "a"
    ],
    "stack_symbols": [
        "0",
        "1"
    ],
    "transitions": {
        "q0": {
            "a": {
                "0": [
                    "q1",
                    [
                        "1",
                        "0"
                    ]
                ]
            }
        },
        "q1": {
            "a": {
                "1": [
                    "q1",
                    [
                        "1",
                        "1"
                    ]
                ]
            },
            "b": {
                "1": [
                    "q2",
                    ""
                ]
            }
        },
        "q2": {
            "b": {
                "1": [
                    "q2",
                    ""
                ]
            },
            "": {
                "0": [
                    "q3",
                    [
                        "0"
                    ]
                ]
            }
        }
    },
    "initial_state": "q0",
    "initial_stack_symbol": "0",
    "final_states": [
        "q3"
    ],
    "acceptance_mode": "final_state",
    "name": "1"
}
```


