# Brainstorm Inicial - Sistema LolliPop

Este documento serve como o ponto de partida para a construção da ideia do sistema **LolliPop**. Ele será refinado até que tenhamos uma visão clara para o protótipo.

## 1. Visão Geral do Desafio
O LolliPop é um sistema PDV Windows (Local-First) que precisa resolver o problema de estoque em lojas de moda infantil com sincronização offline/online. O maior desafio é garantir a integridade do estoque (FIFO) e evitar vendas duplicadas sem exigir conexão constante.

## 2. Agentes de Apoio Selecionados
Para o desenvolvimento, utilizaremos a seguinte combinação de "Agentes" (Skills):
- **Estrategista (Project-Blueprint)**: Garantirá que cada passo seja documentado e que testes venham antes do código.
- **Consultor (Brainstorming)**: Ajudará a questionar e validar cada funcionalidade antes da implementação.
- **Arquiteto Sênior (Senior-Architect)**: Fornecerá os padrões de design (.NET/WPF/Postgres) e melhores práticas.

## 3. Pilares da Solução (Baseado no PRD)
- **Local-First Reais**: SQLite criptografado como fonte da verdade local.
- **Sincronização FIFO**: Ordem de prioridade baseada no timestamp local (com proteção contra desajuste de relógio).
- **Reserva Leve (Soft Reservation)**: Um estado intermediário que "segura" o item no notebook antes da confirmação no servidor.
- **Gestão de Grade**: Matriz de Tamanho/Cor otimizada para entrada rápida.

## 4. Metodologia de Desenvolvimento (Test-First)
Para o LolliPop, seguiremos rigorosamente a cultura de **Test-Driven Development (TDD)**:
1.  **Red**: Escrever o teste para o requisito (ele deve falhar inicialmente).
2.  **Green**: Escrever o código mínimo necessário para o teste passar.
3.  **Refactor**: Melhorar o código mantendo o teste passando.
*Não será aceito código de funcionalidade sem o respectivo teste de validação prévio.*

## 4. Suposições Iniciais (Validar)
- [x] O banco de dados PostgreSQL será hospedado no **Supabase** (Confirmado). Aproveitaremos recursos de Realtime e Auth caso necessário no futuro.
- [x] A aplicação será desenvolvida em **WinUI 3 (Windows App SDK)**. Como o sistema será usado a partir do Windows 11, esta é a escolha ideal para garantir o visual mais moderno (Fluent Design, Mica, bordas arredondadas) e melhor performance em hardware atual.
- [x] **Segurança Multinível**: Confirmada a utilização de **SQLCipher** (criptografia AES-256) em conjunto com **Windows DPAPI** para proteção da chave mestra (atrelada ao usuário do Windows).

## 5. Próximas Perguntas Críticas
1. **Resolução de Conflitos (Regra de Negócio)**:
    - **Prioridade Absoluta**: A primeira ordem processada pelo servidor (baseada no Timestamp sincronizado) recebe o status "Reserva Garantida".
    - **Notificação de Reserva Falha**: Se o sistema detectar que o item já está travado por outro PDV, o usuário recebe: *"Produto em estoque, mas já reservado por outro terminal. Entre em contato com o supervisor."*
    - **Intervenção Manual**: O Supervisor tem o poder de:
        - **Liberar Manualmente**: Cancela a primeira reserva e entrega ao segundo requerente.
        - **Manter Reserva**: Mantém a fila original.
2. **Setup de Nuvem**: Há uma infraestrutura de servidor já definida ou devo propor uma (ex: Supabase)?
- **Identidade Visual (Paleta Deep Logic & Action Blue)**:
    - **Primária**: Azul Oceano (#1A73E8) - Ações principais.
    - **Fundo**: Off-White (#F8F9FA) - Ergonomia visual/Redução de fadiga.
    - **Texto/Títulos**: Cinza Frio (#202124) - Alto contraste.
    - **Sucesso**: Verde Esmeralda (#1E8E3E).
    - **Atenção**: Ambar (#F9AB00).
    - **Erro/Perigo**: Carmim (#D93025).
    - *Nota: Design focado em uso intenso de 8h/dia, priorizando redução de brilho e clareza semântica.*

## 6. Requisitos Não Funcionais (Critérios de Qualidade)
- **Performance**: Tempo de resposta do PDV < 200ms para leitura de código de barras (mesmo com DB criptografado).
- **Escalabilidade**: Suporte para até 10 PDVs simultâneos na mesma loja sincronizando com o Supabase.
- **Resiliência**: Capacidade de operar 100% offline por até 7 dias sem perda de integridade de timestamps.
- **Segurança**: Conformidade com LGPD para dados de clientes colecionados no PDV.

## 7. Roadmap de Planejamento (Pré-Codificação)
Para um planejamento de excelência, seguiremos estas etapas antes de abrir o IDE para o código da aplicação:

1.  **[ ] Step-by-Step Roadmap Técnica**: Detalhar a ordem exata de implementação dos módulos (Config -> DB -> Sync -> UI).
2.  **[ ] Especificação de User Stories & Gherkin**: Escrever cenários de teste em linguagem natural (Ex: *Dado que o produto X tem 1 unidade... Quando vendedora A e B reservarem...*).
3.  **[ ] Modelagem de Dados Detalhada (DDL)**: Scripts SQL iniciais para Supabase e SQLite para validar tipos de dados e constraints.
4.  **[ ] Protótipo de Baixa Fidelidade (Wirefames)**: Desenhar o layout das 3 telas principais (PDV, Dashboard, Grade) para validar o UX.
5.  **[ ] Análise de Riscos Técnica**: Documentar o que acontece em falhas catastróficas (ex: corrupção de banco local).

## 8. Próximos Passos Imediatos
1. Iniciar o **Roadmap Técnico Detalhado**.
2. Criar as **User Stories** com critérios de aceitação rigorosos.
