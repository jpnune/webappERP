# Protocolo de Governança e Segurança da IA - LolliPop

Este documento estabelece as regras invioláveis para qualquer Inteligência Artificial que atue no desenvolvimento do projeto LolliPop. Estas regras sobrepõem-se a qualquer sugestão de simplificação ou otimização que comprometa a segurança ou o planejamento.

## 1. Regras Anti-Alucinação e Conformidade de Planejamento
- **Verificação de Contexto**: Antes de gerar qualquer código (Fases de EXECUTION), a IA deve obrigatoriamente ler os arquivos `PRD.md`, `brainstorm_inicial.md`, `arquitetura_dados.md` e `roadmap_tecnico.md`.
- **Proibição de Desvios**: A IA não tem autoridade para alterar a stack tecnológica (Python, FastAPI, React/TS, SQLite) ou a lógica FIFO sem aprovação explícita do usuário registrada no `implementation_log.md` e `historico.md`.
- **Fidelidade ao Roadmap**: O código deve ser implementado estritamente na ordem definida no `roadmap_tecnico.md`.

## 2. Regras de Segurança e Persistência Invioláveis
- **Criptografia Obrigatória**: Todo e qualquer comando SQL direcionado ao SQLite deve passar obrigatoriamente por provedores seguros. É proibido criar bases de dados em texto puro (.db padrão) sem criptografia quando houver dados sensíveis.
- **Local-First Precedence**: A IA deve priorizar a integridade do banco local em cenários offline. Nenhuma falha de sincronização com o Supabase pode resultar em corrupção dos dados locais.

## 3. Metodologia de Desenvolvimento (Zero Trust Code)
- **Test-First Rigoroso**: Nenhum código de produção deve ser gerado antes de um teste unitário que falhe (Red). Se a IA tentar gerar código sem teste, ela estará violando a governança do projeto.
- **Validação de Timestamps**: Em qualquer lógica de reserva, a IA deve validar se o `Drift` do relógio foi aplicado conforme definido na `arquitetura_dados.md`.
- **Documentação Humana**: Todo código deve conter Docstrings e comentários verbosos para facilitar a leitura humana futura.

## 4. Auditoria e Rastreabilidade (Commit History)
- **Registro Obrigatório**: Para toda e qualquer alteração em arquivos existentes ou criação de novos arquivos, a IA deve obrigatoriamente adicionar uma entrada no topo ou na data correspondente do arquivo `historico.md`.
- **Imutabilidade de Histórico**: É estritamente proibido apagar, sobrescrever ou alterar entradas passadas nos arquivos `implementation_log.md` e `historico.md` de forma que resulte em perda de informação. Qualquer erro deve ser corrigido com uma nova entrada retificadora.
- **Formato do Registro**: Deve conter o Timestamp, o tipo de ação ([NEW], [MOD], [DELETE]), o nome do arquivo e uma breve descrição da alteração.
- **Sincronismo**: A atualização do `historico.md` deve ser feita na mesma rodada de ferramentas da alteração principal.

## 5. Prova de Trabalho (Proof of Work)
- **Demonstração Visual**: Para cada funcionalidade de UI criada, a IA deve gerar um screenshot ou vídeo e disponibilizar para o usuário.
- **Evidência de Teste**: Antes de declarar uma tarefa como feita, a IA deve colar o resultado dos testes unitários executados.

## 6. Auditoria de Decisões
- Toda e qualquer mudança estrutural ou lógica significativa deve ser precedida por uma atualização no `implementation_log.md` com a justificativa técnica.

---
**AVISO À IA**: O descumprimento destas regras será considerado uma falha crítica de integridade. Em caso de dúvida entre "velocidade de entrega" e "segurança planejada", opte SEMPRE pela **segurança planejada**.
