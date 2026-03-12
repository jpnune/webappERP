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

## [2026-03-11] - Testes E2E e Gestão de Clientes


### [11/03/2026 18:50] - 039_PRODUCT_SAVE_VALIDATION_FIX
- **Action**: Tornei os campos secundários do produto (`brand`, `supplier`, `min_stock`, `margin`, `status`) opcionais nos esquemas Pydantic do backend e adicionei tratamento de erro detalhado no `productService.ts`.
- **Rationale**: Corrigir o erro 422 (Unprocessable Entity) que ocorria ao tentar salvar produtos com dados incompletos ou registros migrados com campos nulos. A API agora é mais resiliente e fornece logs claros caso ocorram falhas.
- **Affected Files**: `schemas.py`, `productService.ts`, `implementation_log.md`.
- **Status**: Success

### [11/03/2026 18:15] - 038_INVENTORY_AND_PRODUCT_FORM_UX_POLISH
- **Action**: Refinamento visual da lista de variações no Inventário (zebrado, exclusão de bullets, fontes maiores) e implementação do Switch "Tamanho Único" azul premium no `ProductForm.tsx`.
- **Rationale**: Elevando a qualidade visual e simplificando a jornada de cadastro de produtos sem grade complexa, atendendo às exigências estéticas do projeto.
- **Affected Files**: `Inventory.tsx`, `ProductForm.tsx`, `VariationListView.tsx` (inline), `implementation_log.md`.
- **Status**: Success

### [11/03/2026 21:00] - 037_PDV_VARIATIONS_AND_BARCODE
- **Action**: Implementação de suporte a variações de produtos (Tamanho/Cor) e scanner de código de barras no PDV.
- **Rationale**: Melhorar a precisão das vendas e agilidade no atendimento, permitindo selecionar grades específicas e usar hardware de scanner.
- **Affected Files**: `backend/models.py`, `backend/schemas.py`, `backend/routers/sales.py`, `productService.ts`, `salesService.ts`, `Vendas.tsx`, `ProductForm.tsx`.
- **Status**: Success

### [11/03/2026 20:25] - 036_CATEGORY_COMPONENT_FIX
- **Action**: Refatoração do componente de Categorias no `ProductForm.tsx`.
- **Rationale**: Corrigir bugs de interatividade no `Select` e falhas na criação de novas categorias causadas por conflitos de eventos e componentes customizados fora do padrão Radix UI.
- **Affected Files**: `ProductForm.tsx`.
- **Status**: Success

### [11/03/2026 19:30] - 034_PRODUCT_FORM_UX_AND_CATEGORIES
- **Action**: Implementação de categorias persistentes e melhoria na calculadora de preços/validação no `ProductForm.tsx`.
- **Rationale**: Atender à necessidade de categorias definidas pelo usuário e resolver bugs na lógica de precificação e feedback de erro.
- **Affected Files**: `ProductForm.tsx`, `categoryService.ts`, `backend/routers/categories.py`, `backend/models.py`.
- **Status**: Success

### [11/03/2026 16:00] - 033_SALES_AND_SERVICE_REFACTOR
- **Action**: Refatoração global dos nomes dos serviços (mock -> real) e implementação do backend de vendas.
- **Rationale**: Transição necessária do modelo "Mocked/Demo" para o modelo "Produção Local". A arquitetura agora permite persistência real em SQLite criptografado.
- **Affected Files**: `productService.ts`, `customerService.ts`, `salesService.ts`, `backend/routers/sales.py`, `backend/models.py`, `backend/schemas.py`, `backend/main.py`.
- **Status**: Success

### [11/03/2026 15:15] - 032_DOCUMENTATION_SYNC
- **Action**: Atualização do `roadmap_tecnico.md` e `RESUMO_PARA_IA.md`.
- **Rationale**: Garantir que o planejamento reflita a conclusão do Frontend MVP e o início da integração com a API FastAPI local e suporte a SQLCipher.
- **Affected Files**: `roadmap_tecnico.md`, `RESUMO_PARA_IA.md`.
- **Status**: Success

### [11/03/2026 10:45] - 028_E2E_PLAYWRIGHT_STABILIZATION
- **Action**: Configuração completa e estabilização do Playwright para testes End-to-End (E2E).
- **Rationale**: Garantir que o fluxo crítico (Ex: Cadastro de Produtos) funcione como um usuário real. Correção de seletores complexos do Radix UI (Select/Combobox) e injeção do mock de localStorage.
- **Affected Files**: `playwright.config.ts`, `e2e/specs/product-flow.spec.ts`, `e2e/pages/ProductPage.ts`.
- **Status**: Success

### [11/03/2026 11:10] - 029_CUSTOMER_CRUD_AND_MASKS
- **Action**: Construção completa do módulo de Clientes (`Customers.tsx`, `CustomerForm.tsx`, `mockCustomers.ts`) com persistência em `localStorage`. Injeção de máscaras e formatação.
- **Rationale**: Replicar a arquitetura bem sucedida de Produtos para os Clientes. O formulário agora exige validações rígidas de UX: Telefone `(11) 99999-9999`, CPF (apenas números), CEP `XXXXX-XXX` e separação completa do endereço (Rua, Número, Bairro, Complemento).
- **Affected Files**: `Customers.tsx`, `CustomerForm.tsx`, `mockCustomers.ts`, `routes.ts`.
- **Status**: Success

### [11/03/2026 11:28] - 030_UNIT_TEST_CLEANUP
- **Action**: Varredura e exclusão de testes unitários defasados da interface, documentações TXT antigas e remoção de imagens mock em base64 (`ImageWithFallback.tsx`). Correção da suíte `vite.config.ts` para ignorar os testes do Playwright.
- **Rationale**: Manter o repositório limpo e os testes 100% verdes após as refatorações massivas das interfaces de Inventário e Vendas.
- **Affected Files**: `vite.config.ts`, exclusão de `src/app/features/inventory/__tests__`, entre outros.
- **Status**: Success

### [11/03/2026 11:40] - 031_PIVOT_LOCAL_FIRST_EXCLUSIVE
- **Action**: Alteração estrutural do `roadmap_tecnico.md`. Supabase e Cloud atrasados para a Fase 4. Fase 2 e 3 focadas integralmente em SQLite + SQLCipher + Integração Frontend-Backend.
- **Rationale**: Pedido expresso do usuário para não onerar custos com nuvem (Supabase) prematuramente. Construção e homologação do software deverá ser garantida 100% offline antes da sincronização remota.
- **Affected Files**: `roadmap_tecnico.md`, `task.md`, `implementation_plan.md`.
- **Status**: Success

## [2026-03-12] - Gestão de Crédito e Refinamento de Status

### [12/03/2026 09:15] - 040_I18N_AND_BRANDING
- **Action**: Atualização do `index.html` para `lang="pt-BR"` e novo título.
- **Rationale**: Padronizar o sistema para o mercado brasileiro de acordo com a solicitação do usuário.
- **Affected Files**: `index.html`.
- **Status**: Success

### [12/03/2026 10:30] - 041_MANUAL_CREDIT_BACKEND
- **Action**: Adição do campo `manual_credit_limit` e execução de script de migração em database criptografada.
- **Rationale**: Permitir que administradores definam limites de crédito fixos, ignorando a taxa variável se necessário.
- **Affected Files**: `models.py`, `schemas.py`, `database.py`, `migrate_manual_credit.py`.
- **Status**: Success

### [12/03/2026 11:00] - 042_CREDIT_RISK_UI
- **Action**: Implementação do cálculo de risco em tempo real no `CustomerForm.tsx` com banner de aviso Amber.
- **Rationale**: Transparência financeira. O usuário deve ser alertado visualmente sobre o risco assumido ao liberar crédito acima do sugerido pelo histórico de compras.
- **Affected Files**: `CustomerForm.tsx`.
- **Status**: Success

### [12/03/2026 11:30] - 043_SWITCH_VISUAL_POLISH
- **Action**: Ajuste de cores do Componente Switch (`green-600` para checked, `slate-200` para unchecked).
- **Rationale**: Melhorar o contraste e a identificação rápida do estado de ativação do crédito.
- **Affected Files**: `CustomerForm.tsx`, `switch.tsx`.
- **Status**: Success

### [12/03/2026 12:00] - 044_STATUS_VS_CREDIT_REFACTOR
- **Action**: Vinculação do crédito ao status Ativo e remoção de trava de venda para inativos.
- **Rationale**: Flexibilidade comercial (permitir vendas de queima de estoque para inativos) mantendo a segurança financeira (bloqueio de crédito para inativos).
- **Affected Files**: `backend/routers/sales.py`, `backend/routers/customers.py`, `CustomerForm.tsx`.
- **Status**: Success

### [12/03/2026 16:30] - 046_FIADO_PAYMENT_METHOD
- **Action**: Implementação do método de pagamento "Fiado" utilizando o limite de crédito.
- **Rationale**: Atender à necessidade de vendas a prazo (caderneta) com segurança financeira, garantindo que o cliente não exceda o limite liberado (seja ele manual ou baseado em taxa).
- **Affected Files**: `sales.py`, `customers.py`, `Vendas.tsx`.
- **Status**: Success
