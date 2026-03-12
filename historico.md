# Histórico de Desenvolvimento - LolliPop

## Cronologia

### Data: 12 de Março de 2026 - Gestão Avançada de Crédito e Regras de Status
**Mudanças Principais:**
- **2026-03-12 16:45**: [UX/UI] `CustomerForm.tsx` - Adicionado feedback visual de **"Segurança Reforçada"** (mensagem verde) quando o usuário opta por um limite manual mais conservador/menor que o sugerido pelo sistema.
- **2026-03-12 16:40**: [UX/BUGFIX] `CustomerForm.tsx` - Corrigido bug de interação nos campos numéricos (Taxa e Limite Manual). Agora é possível apagar completamente o valor sem que o zero persistente atrapalhe a digitação.
- **2026-03-12 16:35**: [BUGFIX] `customers.py`, `Vendas.tsx` - Corrigida prioridade de exibição do crédito. Agora, se um **Limite Manual** for definido, ele substitui o valor sugerido em todas as listas e validações do sistema, garantindo consistência entre o cadastro e o PDV.
- **2026-03-12 16:30**: [FINANCEIRO/PDV] `Vendas.tsx`, `sales.py` - Implementado método de pagamento **Fiado**. O sistema agora valida o limite (Manual ou Sugerido) antes de fechar a venda e exibe o saldo de crédito disponível no carrinho em tempo real.
- **2026-03-12 16:20**: [UX/UI] `CustomerForm.tsx` - Implementado o cálculo dinâmico de **Crédito Sugerido** (`Volume Gasto * Taxa (%)`). O campo agora reage em tempo real às alterações da taxa inserida pelo usuário.
- **2026-03-12 12:00**: [BACKEND/FRONTEND] `sales.py`, `customers.py`, `CustomerForm.tsx` - Removida a trava global de vendas para clientes inativos. O bloqueio agora é restrito ao **Crédito Fidelidade**, que é automaticamente zerado e desabilitado se o status do cliente não for "Ativo".
- **2026-03-12 11:30**: [UX/UI] `CustomerForm.tsx`, `switch.tsx` - Switch de crédito agora possui cor verde (`bg-green-600`) quando ativo e cinza claro (`bg-slate-200`) quando inativo, garantindo visibilidade total.
- **2026-03-12 11:00**: [NEW] `CustomerForm.tsx` - Implementado campo de **Limite Manual de Crédito** com inicialização em 0. Adicionado banner de **"Atenção: Risco Redobrado"** que exibe a diferença em Reais quando o limite manual excede o sugerido pelo sistema.
- **2026-03-12 10:30**: [BACKEND] `models.py`, `schemas.py`, `migrate_manual_credit.py` - Adicionada coluna `manual_credit_limit` ao banco de dados SQLite/SQLCipher e sincronizada com os esquemas Pydantic.
- **2026-03-12 09:15**: [I18N] `index.html` - Alterado idioma base para `pt-BR` e título do sistema para "LolliPop ERP - Gestão de Varejo".

### Data: 11 de Março de 2026 - UX Premium e Refinamentos de Variação
**Mudanças Principais:**
- **2026-03-11 18:45**: [FIX] `schemas.py`, `productService.ts` - Resolvido erro ao salvar produto. Flexibilização dos esquemas Pydantic para aceitar campos nulos/opcionais e melhoria no log de erros do frontend.
- **2026-03-11 18:20**: [UX/UI] `Inventory.tsx` - Refinamento da lista de variações com zebra-striping, fontes ampliadas e remoção de indicadores visuais redundantes para melhor legibilidade.
- **2026-03-11 18:15**: [NEW] `ProductForm.tsx` - Implementação do Switch "Tamanho Único" azul premium. Adicionada lógica de transição que preserva/restaura tamanhos anteriores ao alternar modos.
- **2026-03-11 18:10**: [FIX] `ProductForm.tsx` - Correção de erros de sintaxe JSX e restauração de funcionalidades de limpeza da grade (Matriz de Quantidades).
- **2026-03-11 16:00**: [REFATORAÇÃO] `productService.ts`, `customerService.ts`, `salesService.ts` - Removido prefixo `mock` de todos os arquivos e classes. Atualizados 100% dos componentes front-end (`Inventory.tsx`, `Vendas.tsx`, `ProductForm.tsx`, `CustomerForm.tsx`) para usar os serviços reais.
- **2026-03-11 15:50**: [BACKEND] `sales.py`, `models.py`, `schemas.py` - Implementado módulo de vendas no FastAPI com suporte a itens de venda e baixa automática de estoque no campo `variants_json` (campo dinâmico para MVP).
- **2026-03-11 15:15**: [MOD] `roadmap_tecnico.md`, `RESUMO_PARA_IA.md` - Sincronização da documentação de planejamento com o progresso real do projeto. Fase 1 marcada como concluída e Fase 2 (Infraestrutura Local/SQLCipher) iniciada e em andamento.
- **2026-03-11 11:28**: ... (restante do arquivo)
- **2026-03-11 11:10**: [NEW] `mockCustomers.ts`, `CustomerForm.tsx`, `Customers.tsx` - Implementado CRUD completo de Clientes com persistência em localStorage. Formulário construído com estado controlado e máscaras RegEx em tempo real para Telefone `(11) 99999-9999`, CPF e CEP `XXXXX-XXX`. Endereço reestruturado para múltiplos campos.
- **2026-03-11 10:45**: [TEST] `product-flow.spec.ts`, `ProductPage.ts` - E2E com Playwright estabilizado. Corrigido seletor problemático do Combobox do RadixUI e inserido adapter para persistência de localStorage nos testes de jornada.
- **2026-03-11 07:35**: [FIX] `colors.css` - Correção dos erros `unknown utility class border-border` e `outline-ring/50` através do mapeamento das variáveis `--color-border` e `--color-ring` no bloco `@theme` do Tailwind v4.

### Data: 10 de Março de 2026 - Padronização Visual e Estoque Funcional
**Mudanças Principais:**
- **Sistema de Cores**: Criação do arquivo `src/styles/colors.css` extraindo todas as variáveis CSS "hardcoded" do `theme.css`. Mapeamento oficial da paleta "Pastel Professional".
- **Mock Service Completo (CRUD)**: Ampliação do arquivo `mockProducts.ts` para agira como um banco de dados em memória, adicionando as funções Create, Update, Delete e GetById, todas com latências via Promises/setTimeout. A interface `Product` agora suporta Multi-Tamanhos e Multi-Cores.
- **Tela de Estoque Reativa e UX (`Inventory.tsx`)**: Substituição dos dados mockados estáticos da tela. A tabela, a busca e os filtros agora consultam dinamicamente a Promise `mockProductsService`. Os "Cards Superiores" (Sem Estoque, Baixo Estoque) foram transformados em botões interativos que filtram a tabela imediatamente. Clique na Tabela agora expande as **Variações de Matriz da Peça** (GradeMatrix View).
- **Tela de Detalhes (`ProductForm.tsx`)**: Refatoração do formulário para o modo Criação e Edição (puxando ID pela rota React Router `/:id`), carregando pre-loads do Mock e salvando ou atualizando na tabela de forma correta. Matriz de Grade incorporada ao Modo Edição.
- **Notificação e Testes**: O Sistema Universal de Avisos (Sonner Toaster) agora possui ícone interativo `(X)`. Execução das suítes de teste via Vitest re-validada provando integridade contínua (4 files passed).
- **2026-03-10 11:10**: [MOD] `Inventory.tsx`, `InventoryActions.test.tsx` - Implementação de DropdownMenu no botão de Filtros (Limpar Filtros e Filtro por Status) e adição de ordenação (Sort) em todas as colunas da tabela. Criação de suíte de testes dedicada para essas ações.

### Data: 10 de Março de 2026 - Ponto de Venda (PDV/Vendas)
**Mudanças Principais:**

- **2026-03-09 11:20**: [MOD] `roadmap_tecnico.md`, `implementation_plan.md`, `historico.md` - Atualização maciça detalhando os exatos próximos passos do Frontend (Foco na tela PDV/Vendas e Camada Mock API) e fixo do problema de Document Drift através da promessa de uma revisão periódica de governança na transição de tarefas.

- **2026-03-09 11:10**: [NEW] `ProductForm.tsx`, `CustomerForm.tsx`, `src/__tests__/` - Criação do Cadastro de Produtos e Clientes, com as devidas integrações de rota nas telas de listagem. Instalação e configuração completa do suite de testes automatizados com Vitest, happy-dom e React Testing Library (fundação do Test-First). Renderizados 6 testes de integração/UI com sucesso.

- **2026-03-09 10:55**: [FIX] `badge.tsx`, `Inventory.tsx`, `Orders.tsx`, `Dashboard.tsx` - Correção dos Badges de status. Implementação de variantes nativas (`success`, `warning`, `info`) para garantir que as cores semânticas (Verde, Laranja, Azul, Vermelho) sejam aplicadas corretamente sem sobreposição.

- **2026-03-09 10:27**: [MOD] `task.md`, `implementation_plan.md` - Pivot estratégico para **Frontend-First**. Prioridade total na UI e Mock Data antes do backend.

- **2026-03-09 10:22**: [NEW] `README.md`, `.gitignore`, `git init` - Inicialização do repositório Git e primeiro commit conectado ao GitHub (`webappERP.git`).

- **2026-03-09 10:17**: [MOD] `segurancaIA.md` - Adição da regra de Imutabilidade de Histórico e atualização da stack base (Python/React).

- **2026-03-09 07:46**: [NEW] `task.md`, [MOD] `implementation_plan.md` - **09/03/2026**: Pivot para integração de repositório Git externo (`Erpforclothingstore`). Protótipo manual substituído por base sólida em React/Vite/Tailwind.
- **09/03/2026**: Clonagem do repositório concluída na pasta `frontend`. Estrutura analisada e mapeamento de páginas (Dashboard, Inventory, Orders) realizado.

## [2026-03-08]

### v0.0.1 - Planejamento Inicial
- **2026-03-08 11:45**: [NEW] `PRD.md` - Definição dos requisitos iniciais.
- **2026-03-08 11:45**: [NEW] `brainstorm_inicial.md` - Brainstorming da visão do produto.
- **2026-03-08 11:45**: [NEW] `implementation_log.md` - Log de decisões técnicas.
- **2026-03-08 11:38**: [MOD] Renomeação do projeto de "InfantMix" para "LolliPop".
- **2026-03-08 11:38**: [MOD] Definição da paleta de cores oficial.
- **2026-03-08 11:40**: [MOD] Confirmação do uso de SQLCipher + Windows DPAPI.
- **2026-03-08 11:42**: [MOD] Escolha do Supabase (Cloud Postgres).
- **2026-03-08 11:43**: [MOD] Escolha do Framework UI WinUI 3.
- **2026-03-08 11:45**: [NEW] `arquitetura_dados.md` - Desenho da arquitetura híbrida.
- **2026-03-08 11:48**: [MOD] Definição da regra de resolução de conflitos (Prioridade FIFO + Supervisor).
- **2026-03-08 11:51**: [MOD] Confirmação da metodologia Test-First (TDD).
- **2026-03-08 11:57**: [NEW] `roadmap_tecnico.md` - Definição das 5 fases de construção.
- **2026-03-08 12:00**: [NEW] `segurancaIA.md` - Protocolo de governança para a IA.
- **2026-03-08 12:29**: [MOD] `brainstorm_inicial.md` - Alteração da Identidade Visual para a paleta ergonômica "Deep Logic & Action Blue".
- **2026-03-08 12:25**: [NEW] Mockup Visual da Tela de PDV (Vendas) gerado via StitchMCP.
- **2026-03-08 12:18**: [MOD] `roadmap_tecnico.md` - Pivotagem estratégica para **Visual-First**. Frontend priorizado.
- **2026-03-08 12:16**: [MOD] `roadmap_tecnico.md` - Esclarecimento sobre a fase de Prototipagem Visual Antecipada.
- **2026-03-08 12:12**: [NEW] `guia_verificacao.md` - Guia para acompanhamento humano do projeto.
- **2026-03-08 12:12**: [MOD] `segurancaIA.md` - Adição da regra de Proof of Work.
- **2026-03-08 12:07**: [NEW] `historico.md` - Criação do log de histórico de commits.
