# Roadmap Técnico Detalhado - LolliPop

Este roadmap agora segue a estratégia **Visual-First (Design-Driven)**, priorizando a validação da interface antes da infraestrutura robusta.

## Fase 1: MVP de Design e Frontend (Prototipagem Real em React) [DONE]
- **Objetivo**: Criar a "casca" do programa com o visual premium para aprovação do UX.
- [x] 1.1 Configuração do ecossistema React, Vite e Tailwind CSS.
- [x] 1.2 Implementação do Shell (Menu lateral de Layout fixo, com navegação responsiva).
- [x] 1.3 Implementação de Temas e Cores Premium (Pastel Professional - Deep Logic & Action Blue).
- [x] 1.4 Tela e Formulário Base: Cadastro de Produtos (Matriz de Grade).
- [x] 1.5 Tela e Formulário Base: Cadastro de Clientes.
- [x] 1.6 Configuração da Suíte de Testes Automatizados (Vitest + React Testing Library).
- [x] 1.7 Criação da Tela de PDV / Frente de Caixa (Carrinho Dinâmico, Busca Rápida).
- [x] 1.8 Refinamento de Componentes UI (Modais de Confirmação, Toasts de Alerta).
- [x] 1.9 Validação Humana: Aprovação do "Look & Feel" final e fluxo de navegação do App React.
- [x] 1.10 Padronização Visual Global (CSS Centralizado `colors.css` / `theme.css`).
- [x] 1.11 Tela de Estoque Funcional Frontend (Listagem com status dinâmico via Mock API).
- [x] 1.12 Formulário de Produto 100% Funcional (Modo Edição e Criação, Salvamento Mockado).

## Fase 2: Infraestrutura e Base de Dados Local (Python/SQLCipher) [DONE]
- **Objetivo**: Implementar a persistência real criptografada, rodando 100% offline na máquina do usuário.
- [x] 2.1 Configuração do ambiente Python e Servidor FastAPI local.
- [x] 2.2 Integração do Provider SQLite com **SQLCipher**.
- [x] 2.3 Modelagem do Banco de Dados (SQLAlchemy) e Testes de Unidade.
- [x] 2.4 Integração Frontend React <-> Backend Python.
- [x] 2.5 Substituição total dos Mocks Frontend pela API Local.

## Fase 3: Domínio de Negócio Avançado (Offline) [DONE]
- **Objetivo**: Finalizar regras específicas de negócio antes de conectar na internet.
- [x] 3.1 Geração de Relatórios e Dashboards baseados na base local (Real-time).
- [x] 3.2 Lógica Avançada da Matriz de Grade (Tamanhos/Cores/Kits) com Alertas Inteligentes.
- [x] 3.3 Lógica de PDV integrada ao banco local.
- [x] 3.4 Fechamento Financeiro Offline e Fluxo de Caixa Real.

## Fase 4: Cloud, Sincronização e Nuvem (Supabase) [TODO]
- **Objetivo**: Conectar o sistema local finalizado com a nuvem de forma resiliente e econômica.
- [ ] 4.1 Integração e Setup Inicial do **Supabase/Postgres**.
- [ ] 4.2 Módulo de Cálculo de Drift e Fila de Sincronização (Local -> Cloud -> Local).
- [ ] 4.3 Lógica de Resolutor de Conflitos (Prioridade FIFO).
- [ ] 4.4 Sincronização em Background (Notificações In-App de Sync).

## Fase 5: Homologação e Empacotamento
- **Objetivo**: Preparação do binário final de Windows.
- [ ] 5.1 Testes E2E (Playwright) em Fluxos Completos (Frontend + Backend Local + Sync Cloud).
- [ ] 5.2 Auditoria de Segurança Local e Cloud.
- [ ] 5.3 Empacotamento do Backend Python e Frontend React no instalador `.msix` do Windows App SDK.
