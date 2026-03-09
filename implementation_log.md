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
