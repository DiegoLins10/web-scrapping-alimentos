# 🥗 Web Scraper - TBCA 🥗

Bem-vindo ao projeto de Web Scraping da **Tabela Brasileira de Composição de Alimentos (TBCA)**! 

> **by Diego Lins** ✨

---

## 📋 O que é este projeto?

Este é um **scraper inteligente** que coleta dados nutricionais de milhares de alimentos da base de dados TBCA! 🍎🍊🥕 O projeto extrai automaticamente:

- 🔢 **Código do alimento**
- 📝 **Descrição detalhada**
- 🏷️ **Classificação**
- 💪 **Dados nutricionais completos** (proteína, carboidrato, gordura, vitaminas, minerais, etc.)

---

## 🚀 Como funciona?

### Passo 1️⃣: Coleta de Alimentos
O script acessa a página principal da TBCA e coleta os códigos de todos os alimentos disponíveis, navegando por todas as páginas! 📄

### Passo 2️⃣: Extração de Dados
Para cada alimento encontrado, o scraper:
- Acessa a página de detalhes 🔗
- Extrai a descrição nutrição 📊
- Coleta a tabela de nutrientes
- Salva tudo em formato JSON 📦

### Passo 3️⃣: Armazenamento
Todos os dados são salvos em `alimentos.txt` (um JSON por linha) para fácil processamento! 💾

---

## 📦 Requisitos

Certifique-se de ter instalado:

```bash
pip install -r requirements.txt
```

**Dependências:**
- 🐍 Python 3.7+
- 📚 `requests` - Para fazer requisições HTTP
- 🍲 `beautifulsoup4` - Para parsear HTML

---

## ▶️ Como usar?

Bem simples! Execute:

```bash
python main.py
```

E deixe a mágica acontecer! ✨ O script vai:
1. Fazer o scraping de todos os alimentos 🍽️
2. Extrair os dados nutricionais 📈
3. Salvar em `alimentos.txt` 💾

---

## 📁 Estrutura do Projeto

```
web-scrapping/
├── main.py              # 🐍 Script principal (o coração do projeto!)
├── requirements.txt     # 📦 Dependências
├── alimentos.txt        # 💾 Saída (JSON lines com dados dos alimentos)
└── README.md           # 📖 Você está aqui!
```

---

## 📊 Formato de Saída

Cada linha do `alimentos.txt` é um JSON com a estrutura:

```json
{
  "codigo": "BRC0001C",
  "classe": "C - Frutas e derivados",
  "descricao": "Abacate, polpa, in natura, Brasil",
  "nutrientes": [
    {
      "Componente": "Energia",
      "Unidades": "kcal",
      "Valor por 100g": "76"
    },
    ...
  ]
}
```

---

## ⚡ Recursos Legais

✅ **Tratamento de erros robusto** - Se um alimento não for encontrado, o script continua!  
✅ **URLs criptografadas** - Usa os links reais do site, não tenta adivinhar!  
✅ **Dados completos** - Coleta todos os nutrientes disponíveis  
✅ **Formato estruturado** - JSON puro, fácil de processar  

---

## 🎯 Casos de Uso

- 📊 Análise de composição nutricional de alimentos
- 🥗 Desenvolvimento de apps de saúde e nutrição
- 📈 Pesquisa científica em alimentação
- 💪 Cálculo de macros para dietas personalizadas
- 🤖 Datasets para machine learning

---

## ⚠️ Avisos Importantes

- ⏱️ O scraping pode demorar um tempo (há muitos alimentos!)
- 🙏 Respeite o servidor - não faça múltiplas requisições simultâneas
- 📜 Verifique os termos de uso do TBCA antes de usar os dados
- 🔄 O site pode mudar sua estrutura HTML - se isso acontecer, o script pode precisar de ajustes

---

## 🐛 Troubleshooting

**Problema:** *"Warning: Could not find description element"*  
**Solução:** 🆗 Isso é normal! Alguns alimentos podem ter estrutura HTML diferente. O script pula automaticamente.

**Problema:** *Conexão recusada*  
**Solução:** Verifique sua conexão com a internet! 🌐

**Problema:** *Script muito lento*  
**Solução:** Paciência é uma virtude! 😅 O site pode estar respondendo lentamente.

---

## 📝 Licença

Use livremente! Mas lembre-se: **sempre cite a TBCA** como fonte dos dados! 📚

---

## 👨‍💻 Autor

**Diego Lins** 🎉

Desenvolvido com ❤️ e muita dedicação! 

---

**Divirta-se explorando os dados nutricionais!** 🎉🥗✨
