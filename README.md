# 🟦 Jogo do **Par ou Ímpar** — Python  

Este projeto é uma implementação simples e divertida do clássico jogo **Par ou Ímpar**. O jogador escolhe um número e decide se quer apostar em **Par (P)** ou **Ímpar (I)**. O computador gera um número aleatório, a soma é calculada e então o jogo decide quem venceu.  
Você pode jogar quantas vezes quiser — até perder!  

---

## 🎮 **Como funciona?**

1. O jogador digita um número.
2. O computador sorteia um número entre **0 e 10** usando `randint`.
3. O jogador escolhe se quer apostar em **Par (P)** ou **Ímpar (I)**.
4. A soma dos números é calculada.
5. Se o jogador acertar o resultado (par ou ímpar), ele vence e o jogo continua.
6. Caso contrário, o jogo termina mostrando quantas vitórias consecutivas ele conseguiu.

---

## 🧠 **Lógica aplicada e comandos utilizados**

O projeto faz uso de alguns conceitos fundamentais de Python e lógica de programação:

### 📌 **1. Estruturas de repetição**
- `while True:` para manter o jogo rodando até o jogador perder.
- Laço de validação para garantir que o usuário digite apenas **P** ou **I**.

```python
while escolha not in "PI":
```

---

### 📌 **2. Comando de decisão**
- `if / else` para:
  - Verificar se o número é par ou ímpar (`total % 2 == 0`)
  - Validar a vitória ou derrota do jogador

---

### 📌 **3. Módulos e funções externas**
- `randint()` (do módulo `random`) → gera números aleatórios.
- `sleep()` (do módulo `time`) → cria pausas para deixar o jogo mais fluido.

```python
from random import randint
from time import sleep
```

---

### 📌 **4. Manipulação de strings**
- `.strip().upper()[0]` para limpar espaços, transformar em maiúscula e pegar apenas a primeira letra da escolha do jogador.

---

### 📌 **5. Contador de vitórias**
Variável simples usada para registrar quantas vezes o jogador venceu consecutivamente.

---

## ▶️ **Como executar o projeto**

1. Tenha o **Python 3** instalado em seu computador.
2. Baixe o arquivo `par_ou_impar.py` ou clone este repositório.
3. No terminal, execute:

```
python par_ou_impar.py
```

4. Divirta-se jogando! 😄

---

## 🖥️ **Código completo**

> O código do jogo está disponível no arquivo principal deste repositório.

---

## 🚀 **Possíveis melhorias futuras**

Se quiser evoluir o projeto, aqui vão algumas ideias:

- Adicionar um **menu inicial** (instruções, créditos, etc.)
- Criar um **modo difícil**, onde o computador tenta “trapacear” 😆
- Transformar em um **jogo com interface gráfica** usando Tkinter
- Registrar o maior número de vitórias do jogador no histórico
- Criar testes automatizados (pytest)

---

## 📄 **Licença**

Este projeto é livre para estudos e melhorias. Sinta-se à vontade para modificar e usar como quiser.








