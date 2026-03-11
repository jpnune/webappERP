# Log de Implementação - LolliPop

Este arquivo registra detalhadamente as decisões técnicas, mudanças de arquitetura e progresso diário.

## [2026-03-08] - Planejamento e Design Inicial

### [08/03/2026 11:38] - 001_PROJECT_REBRANDING
- **Action**: Renomeação do projeto de "InfantMix" para "LolliPop".
- **Rationale**: Alinhar o nome com o nicho de moda infantil de forma amigável e memorável.
- **Affected Files**: `README.md`, `PRD.md`.
- **Status**: Success

### [08/03/2026 11:40] - 002_SECURITY_DEFINITION
- **Action**: Escolha de SQLCipher para criptografia de banco local e Windows DPAPI para chaves.
- **Rationale**: Garantir segurança dos dados de estoque e clientes em ambiente offline.
- **Affected Files**: `PRD.md`, `segurancaIA.md`.
- **Status**: Success

### [08/03/2026 11:43] - 003_UI_FRAMEWORK_SELECTION
- **Action**: Seleção do framework WinUI 3 (Windows App SDK).
- **Rationale**: Proporcionar uma experiência nativa Windows com visual moderno (Fluent Design).
- **Affected Files**: `PRD.md`, `roadmap_tecnico.md`.
- **Status**: Success

### [08/03/2026 12:18] - 011_VISUAL_FIRST_PIVOT
- **Action**: Pivotagem estratégica para priorizar o Design e Frontend (MVP Visual).
- **Rationale**: Validar a UX e o fluxo de venda/grade com o usuário antes de consolidar o backend complexo.
- **Affected Files**: `roadmap_tecnico.md`, `task.md`.
- **Status**: Success

## [2026-03-09] - Protótipo e Mudança de Stack

### [09/03/2026 07:46] - 017_PIVOT_TO_WEB_PROTOTYPE_UX
- **Action**: Criação de Protótipo Web (HTML/CSS/JS) para validação rápida de UX.
- **Rationale**: Acelerar a visualização do fluxo de PDV e Matrix de Grade sem a curva de aprendizado inicial do WinUI 3.
- **Affected Files**: `prototype/`, `task.md`, `implementation_plan.md`.
- **Status**: Success

### [09/03/2026 09:25] - 018_INTEGRATE_EXTERNAL_FRONTEND
- **Action**: Integração do repositório Git `Erpforclothingstore`.
- **Rationale**: Utilizar uma base profissional em React/Vite/Tailwind em vez de protótipo manual, ganhando agilidade e qualidade estética.
- **Affected Files**: `frontend/`, `task.md`, `implementation_plan.md`.
- **Status**: Success

### [09/03/2026 10:00] - 019_PIVOT_TO_PYTHON_REACT_STACK
- **Action**: Redefinição total da stack para Python (FastAPI) e React (TypeScript).
- **Rationale**: Maior facilidade de manutenção para o usuário e flexibilidade para arquitetura Local-First (Edge Computing).
- **Affected Files**: `PRD.md`, `arquitetura_dados.md`, `implementation_plan.md`, `task.md`.
- **Status**: Success

### [09/03/2026 10:08] - 020_DEV_PROD_STRUCTURE
- **Action**: Criação das pastas `/development` e `/production` e regras de documentação técnica.
- **Rationale**: Garantir organização, legibilidade humana e automação clara no ciclo de vida do software.
- **Affected Files**: `PRD.md`, `/development`, `/production`.
- **Status**: Success

### [09/03/2026 10:22] - 021_GIT_INITIALIZATION
- **Action**: Inicialização do Git, criação de `README.md` / `.gitignore` e push para o GitHub.
- **Rationale**: Estabelecer controle de versão e backup remoto para o projeto `webappERP`.
- **Affected Files**: Todo o projeto, `.gitignore`, `README.md`.
- **Status**: Success

### [10/03/2026 09:42] - 022_PDV_MOCK_LAYER
- **Action**: Criação da Camada de Mock (`mockProducts.ts`, `mockSales.ts`) simulando delays assíncronos.
- **Rationale**: Isolar o Frontend, permitindo testar a usabilidade com loadings e validações visuais sem necessidade do tráfego ou backend real pronto.
- **Affected Files**: `src/app/services/mockProducts.ts`, `src/app/services/mockSales.ts`.
- **Status**: Success

### [10/03/2026 09:42] - 023_PDV_UI_IMPLEMENTATION
- **Action**: Construção de `Vendas.tsx` (Frente de Caixa), injetada nas Rotas e Menu Lateral.
- **Rationale**: Área crucial da venda. Possui controle de carrinho debounced na busca e totais automáticos com validação de limite de estoque simulando regras de negócio.
- **Affected Files**: `Vendas.tsx`, `Layout.tsx`, `routes.ts`.
- **Status**: Success

### [10/03/2026 10:05] - 024_THEME_CSS_CENTRALIZATION
- **Action**: Refatoração do `theme.css` e centralização no `colors.css`.
- **Rationale**: Garantir a fundação visual (Pastel Professional) para ser reaproveitada via variáveis CSS nativas sem hardcodings duplicados.
- **Affected Files**: `theme.css`, `colors.css`, `index.css`.
- **Status**: Success

### [10/03/2026 10:05] - 025_INVENTORY_FUNCTIONAL_MOCK_CRUD
- **Action**: Evolução do módulo de Produtos. Transformação do Componente `Inventory.tsx` e `ProductForm.tsx` de estático para Dinâmico conectado as promises do `mockProductsService`.
- **Rationale**: Demonstrar na prática o uso do design system com interações reais de tabelas, formulários, feedbacks de toast e exclusão, homologando as telas 100% no front-end.
- **Affected Files**: `mockProducts.ts`, `Inventory.tsx`, `ProductForm.tsx`, `routes.ts`.
- **Status**: Success

### [10/03/2026 10:07] - 026_INVENTORY_UX_IMPROVEMENTS
- **Action**: Injeção do botão de fechar (Close Button) no `Toaster` do Sonner e do ícone de 'X' na mensagem laranja de aviso geral, filtros interativos de Estoque ao clicar nos Componentes `MetricCard`, e refatoração final da `Product` Interface para aceitar variação multi-dimentional (Cores/Tamanhos). Além disso, a `GradeMatrix` agora roda com 100% de largura (`w-full`) sempre se expandindo junto à tabela pai, exibindo matrizes "Único/Padrão" vazias caso o produto não possua Grade cadastrada previamente. O Componente `MetricCard` foi polido, removendo os pequenos ícones de Seta de Tendência (`TrendingUp`/`Down`) e injetando o estado `warning` de cor laranja para o texto `Atenção`.
- **Rationale**: Ajuste refinado solicitado pelo usuário para elevar a usabilidade dos painéis do Estoque e permitir que todos os produtos suportem variações imediatamente (sem restrição de width ou sumiço de componentes). O alerta estático agora pode ser escondido.
- **Affected Files**: `App.tsx`, `Inventory.tsx`, `mockProducts.ts`, `GradeMatrix.tsx`.
- **Status**: Success

### [10/03/2026 11:10] - 027_INVENTORY_FILTERS_AND_SORTING
- **Action**: Implementação de menu dropdown para filtros e lógica de ordenação na tabela de produtos.
- **Rationale**: Melhorar a UX permitindo que o usuário limpe filtros rapidamente e organize a visualização por qualquer coluna (SKU, Nome, Preço, etc).
- **Affected Files**: `Inventory.tsx`, `src/__tests__/inventory/button_test/InventoryActions.test.tsx`.
- **Status**: Success
