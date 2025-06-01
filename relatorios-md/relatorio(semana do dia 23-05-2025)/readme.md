# 🗓️ Relatório Semanal – 23/05/2025 a 30/05/2025

## ✅ Principais Atividades

### 🔐 1. Implementação da Funcionalidade de Logs

- Foi desenvolvida a classe `LoggerJSON`, responsável por registrar eventos do sistema em formato `.json`.
- A estrutura de log implementada segue a seguinte classificação:

| Tipo   | Significado                                                                 |
|--------|------------------------------------------------------------------------------|
| `INFO` | Ações normais do sistema (ex: login, cadastro, listagem)                    |
| `WARN` | Algo que não é erro, mas requer atenção (ex: tentativa de login inválida)   |
| `ERROR` | Problemas que impedem a ação (ex: exceções não tratadas)                    |
| `DEBUG`| Mensagens úteis para desenvolvedores (opcional em produção)                 |
| `AUDIT`| Eventos de rastreio importantes (ex: alteração de dados sensíveis)          |

- A funcionalidade está integrada à tela de login, com registros automáticos de ações como:
  - Tentativas de login bem-sucedidas (`INFO`)
  - Falha de autenticação (`WARN`)
  - Exceções no carregamento de imagens (`WARN`)
  - Campos vazios no login (`ERROR`)

---

### 📁 2. Reorganização da Estrutura de Pastas

- A estrutura do projeto foi reorganizada para maior modularidade e legibilidade:
  - Criação das pastas `controllers`, `models` e `views`
  - Os arquivos foram redistribuídos conforme suas responsabilidades no padrão MVC
  - A pasta `views` foi alterada, onde ao invês de ser uma única classe suporta todas as telas. Agora as telas estão separadas em arquivos separados ! 

---

### 👤 3. Criação da Tela de Login

- A interface gráfica de login foi desenvolvida utilizando `Tkinter`.
- Autor: **Gabriel Morais**
- Destaques:
  - Estilo moderno e compatível com a identidade visual da Pousada Maré Mansa
  - Verificação de campos obrigatórios e autenticação básica
  - Inclusão de opção para exibir/esconder a senha
  - Integração com o sistema de logs
  - Criação automática do usuário administrador (`admin`, senha `senha123`) se não existir

---

### 🛠️ 4. Melhorias Gerais e Outras Ações

- Ajustes e testes na funcionalidade de autenticação.
- Tratamento de exceções com feedback visual via `messagebox`.
- Correções em mensagens, nomes de variáveis e consistência de estilo.

---

## 📌 Observações Finais

- O projeto avança com base em boas práticas de desenvolvimento.
- A modularização já permite expansão com novas funcionalidades, como cadastro de hóspedes, reservas e relatórios.
- O uso de logs facilitará auditorias e manutenções futuras.

---
  
📅 **Data:** 31/05/2025