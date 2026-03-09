PRD: Sistema de Gestão "LolliPop" (Local-First Edge Computing)

1. Visão Geral e Objetivo
Sistema de PDV e Gestão de Estoque para vestuário infantil. O notebook da loja atua como o **Servidor Local (Mestre)** rodando o Backend (Python/FastAPI) e Banco de Dados (SQLite). Dispositivos na loja (tablets/celulares) acessam via rede local. O sistema garante operação 100% offline, com sincronização assíncrona (FIFO) para a nuvem (Supabase) assim que houver internet.

2. Stack Tecnológica Refatorada
- **Backend (Servidor Local)**: Python 3.x com FastAPI.
- **Frontend (UI)**: React 18+ com TypeScript (Vite).
- **Banco de Dados Local**: SQLite (armazenado no notebook mestre).
- **Rede Local**: Uvicorn host 0.0.0.0 (exposição via Wi-Fi interno).
- **Nuvem (Sync/Backup)**: Supabase (PostgreSQL) + Edge Functions para reconciliação.

3. Requisitos de Operação Offline & Sincronização
- [R.NF.01] Operação Mestre: O sistema deve estar disponível na rede local independente de internet externa.
- [R.F.01] Sync Queue: Toda transação deve ser salva primeiro no SQLite local e enfileirada para a nuvem.
- [R.F.02] Conflitos FIFO: O timestamp de alta precisão gerado no notebook define a prioridade de estoque no servidor.
- [R.F.03] Status de Conectividade: O PDV deve exibir se a sincronia com a nuvem está ativa ou pendente.

4. Lógica de Reserva e Fila FIFO
- Soft Reservation (Reserva Leve): Trava o estoque imediatamente no SQLite.
- Fila de Eventos (Event Queue): Fila persistente no SQLite que garante que nenhuma venda se perca em falhas de hardware/rede.
- Timeout de 5 Minutos (Stale Cart): Alerta visual para itens parados no carrinho para evitar travar estoque desnecessariamente.

5. Instruções de Design (UI/UX)
- PDV Resiliente: Status "Semáforo" (Verde: Online/Sincronizado; Amarelo: Offline - Local OK; Vermelho: Erro de Rede).
- FEEDBACK CLARO: "Venda Salva Localmente" vs "Venda Sincronizada com a Nuvem".
- Grade Matriz: Interface tipo "Excel" em React para cadastro rápido de cores/tamanhos (RN a 16).

6. Configuração do Ambiente "Notebook Mestre"
- Host: O notebook da loja rodará o servidor FastAPI vinculando ao endereço IP local da rede Wi-Fi.
- Persistência: Banco SQLite deve ter backups periódicos (Snapshot) para segurança local extra.

7. Padrões de Desenvolvimento e Documentação
- **Documentação em Tempo Real**: Todo o código deve ser documentado (Docstrings, comentários explicativos) durante a criação para garantir máxima "leitura humana" futura.
- **Organização de Pastas (Dual-Path)**:
    - `/development`: Contendo o código-fonte original, histórico detalhado, comentários verbosos e ferramentas de auxílio ao desenvolvedor.
    - `/production`: Contendo o código otimizado, arquivos "minificados" (se aplicável), configurações de automação prontas e ambiente limpo para execução final.
