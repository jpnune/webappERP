# LolliPop ERP - Gestão Inteligente para Moda Infantil

O **LolliPop** é um sistema de ERP e PDV (Ponto de Venda) de alto desempenho, desenhado especificamente para o varejo de moda infantil. O projeto utiliza uma arquitetura de **Edge Computing (Local-First)**, onde o servidor principal roda localmente na loja, garantindo operação contínua mesmo sem internet, com sincronização inteligente na nuvem.

## 🚀 Diferenciais Estratégicos

### 1. Arquitetura Local-First (Offline-Ready)
Diferente de sistemas 100% web que travam quando o Wi-Fi oscila, o LolliPop mantém o PDV e o estoque operacionais no servidor local (notebook mestre). As vendas são salvas instantaneamente no SQLite e enviadas para a nuvem de forma assíncrona assim que a conexão é restabelecida.

### 2. Sincronização FIFO (First-In, First-Out)
Para evitar que o mesmo item de estoque seja vendido simultaneamente em canais diferentes (loja física vs e-commerce), o sistema implementa uma fila de prioridade baseada em timestamps de alta precisão. Quem reserva primeiro no PDV, tem a prioridade da baixa do estoque.

### 3. Matriz de Grade Dinâmica
Interface otimizada para o cadastro rápido de roupas por tamanho (RN a 16) e cor, gerando automaticamente todos os SKUs de uma vez, padrão essencial para o mercado têxtil.

## 🛠️ Stack Tecnológica

- **Backend**: Python 3.12+ com **FastAPI**.
- **Frontend**: React 18+ com **TypeScript** e **Vite**.
- **Banco de Dados Local**: **SQLite** (Resiliência e Velocidade).
- **Banco de Dados Nuvem**: **Supabase (PostgreSQL)** para backup e dashboards remotos.
- **Styling**: Tailwind CSS + Material UI (MUI).

## 📂 Estrutura do Projeto

O repositório segue uma organização rigorosa para garantir legibilidade humana e facilidade de automação:

- `/development`: Código-fonte principal, documentação técnica verbosa e ambiente de desenvolvimento.
- `/production`: Builds otimizadas, arquivos minificados e configurações prontas para o ambiente de loja.
- `/docs`: Documentação de requisitos (PRD), arquitetura de dados e protocolos de segurança.

## 🛡️ Governança e Segurança

O projeto segue um protocolo de **Zero Trust Code**, onde cada alteração é documentada no `historico.md` e decisões técnicas são justificadas no `implementation_log.md`. A segurança dos dados locais é prioridade absoluta.

---

*Desenvolvido com foco em resiliência, estética premium e eficiência operacional.*
