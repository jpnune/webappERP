# Roadmap Técnico Detalhado - LolliPop

Este roadmap agora segue a estratégia **Visual-First (Design-Driven)**, priorizando a validação da interface antes da infraestrutura robusta.

## Fase 1: MVP de Design e Frontend (Prototipagem Real em React)
- **Objetivo**: Criar a "casca" do programa com o visual premium para aprovação do UX.
- [x] 1.1 Configuração do ecossistema React, Vite e Tailwind CSS.
- [x] 1.2 Implementação do Shell (Menu lateral de Layout fixo, com navegação responsiva).
- [x] 1.3 Implementação de Temas e Cores Premium (Pastel Professional - Deep Logic & Action Blue).
- [x] 1.4 Tela e Formulário Base: Cadastro de Produtos (Matriz de Grade).
- [x] 1.5 Tela e Formulário Base: Cadastro de Clientes.
- [x] 1.6 Configuração da Suíte de Testes Automatizados (Vitest + React Testing Library).
- [x] 1.7 Criação da Tela de PDV / Frente de Caixa (Carrinho Dinâmico, Busca Rápida).
- [ ] 1.8 Refinamento de Componentes UI (Modais de Confirmação, Toasts de Alerta).
- [ ] 1.9 Validação Humana: Aprovação do "Look & Feel" final e fluxo de navegação do App React.
- [ ] 1.10 Padronização Visual Global (CSS Centralizado `colors.css` / `theme.css`).
- [ ] 1.11 Tela de Estoque Funcional Frontend (Listagem com status dinâmico via Mock API).
- [ ] 1.12 Formulário de Produto 100% Funcional (Modo Edição e Criação, Salvamento Mockado).
## Fase 2: Infraestrutura e Base de Dados (Python / Supabase)
- **Objetivo**: Implementar a persistência real por trás da interface aprovada.
- [ ] 2.1 Integração do Provider SQLite com **SQLCipher**.
- [ ] 2.2 Migração dos dados simulados para persistência local real.
- [ ] 2.3 Implementação do Wrapper **Supabase/Postgres**.
- [ ] 2.4 Testes de Unidade: CRUD criptografado.

## Fase 3: Motor de Sincronização e Lógica FIFO
- **Objetivo**: Conectar o frontend/local com a nuvem de forma resiliente.
- [ ] 3.1 Módulo de Cálculo de Drift e Fila de Sincronização.
- [ ] 3.2 Lógica de Resolutor de Conflitos e Notificações In-App.
- [ ] 3.3 Testes de Integração: Conflitos offline entre instâncias.

## Fase 4: Domínio de Negócio Avançado
- **Objetivo**: Refinamento de regras específicas (Grades, Kits, Carrinho Amarrado).
- [ ] 4.1 Refinamento da Matriz de Grade (Tamanhos/Cores).
- [ ] 4.2 Lógica de "Reserva Leve" integrada à UI.
- [ ] 4.3 Testes de Regra de Negócio: Reserva atômica.

## Fase 5: Homologação e Empacotamento
- [ ] 5.1 Testes E2E e Auditoria de Segurança.
- [ ] 5.2 Geração do instalador (.msix).
