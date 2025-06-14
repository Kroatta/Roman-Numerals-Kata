# 🏛️ Roman Numerals Kata em Python

Este projeto resolve o clássico desafio de programação **Roman Numerals Kata**, onde o objetivo é converter números inteiros em suas representações com **algarismos romanos**.

---

## 🧠 O Desafio

> Escreva uma função que receba um número inteiro (`int`) e retorne uma string (`str`) com o número em **algarismos romanos**.

### ✅ Exemplos esperados:
| Número | Romano  |
|--------|---------|
| 1      | I       |
| 4      | IV      |
| 9      | IX      |
| 21     | XXI     |
| 48     | XLVIII  |
| 1000   | M       |

---

## 🛠️ Lógica da Solução

A função percorre uma lista de valores romanos em ordem decrescente, subtraindo do número de entrada e acumulando os símbolos correspondentes.

```python
valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

📄 Estrutura dos Arquivos

roman_numerals/
│
├── roman_numerals.py         # Função convert(number)
├── test_roman_numerals.py    # Testes automatizados com unittest













