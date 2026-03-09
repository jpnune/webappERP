# Resumo de Contexto para a Próxima Sessão da IA (Handover)

**Data da pausa:** 2026-03-09
**Projeto:** LolliPop (ERP / PDV)
**Stack Atual:** React, Node (Vite), Tailwind CSS, Vitest, React Testing Library.

## 📍 Onde Paramos e Qual é o Foco
O foco de desenvolvimento da fase atual é estritamente **FRONTEND-FIRST (Prototipagem Real)**. A infraestrutura de backend está pausada até a aprovação visual.
Terminamos com sucesso a fase de cadastros (Clientes e Produtos) e configuramos 100% da suíte de testes automatizados com Vitest, que está rodando com todos os testes no verde.

**Os Exatos Próximos Passos (Conforme Roadmap Técnico):**
1.  **Criar a Tela de PDV / Frente de Caixa (`Vendas.tsx`):** Construir o layout flexível do carrinho dinâmico de produtos, listagem para busca rápida e informações de totalização. Ela terá que estar visualmente linda em nossa paleta "Pastel Professional".
2.  **Integração de Mocks Robustos:** Construir uma fina camada de serviços TypeScript com funções assíncronas "Fake" (Promises com `setTimeout`) para simular o trânsito de dados (Loading state, Error state, Success state) em toda a interface.

## ⚠️ Regras Cruciais de Governança (Você DEVE ler isto!)
O usuário possui regras muito estritas que você deve seguir sem falhas:
1.  **`segurancaIA.md` (MUITO IMPORTANTE):** A IA **DEVE OBRIGATORIAMENTE** registrar cada passo que modificar arquivos de projeto dentro de DOIS arquivos: `historico.md` **e** `implementation_log.md`. Isso precisa ser feito na mesma rodada (mesmo tool call / momento) em que você altera o código. Evite o Document Drift.
2.  **Padrão de Data no Histórico:** Ao documentar em `historico.md`, você deve usar EXATAMENTE o padrão de Data/Hora (Exemplo: `- **2026-03-09 10:55**: [MOD] ...`). Jamais fuja dessa formatação.

## 📚 Documentos para Ler no Início da Próxima Sessão
Antes de escrever 1 linha de código, rode o `view_file` nos seguintes arquivos para entender as rédeas do projeto:
*   `roadmap_tecnico.md` (Sua bússola de prioridades)
*   `C:\Users\jpnun\.gemini\antigravity\brain\98aa2e97-e82d-4482-a6c2-977367c9ab1d\implementation_plan.md` (As regras de design da UI e plano tático)
*   `historico.md` e `implementation_log.md` (Sua fonte cronológica do que fiz até o último segundo)
*   `segurancaIA.md` (Limites da IA)

## 🎯 Instrução Imediata para a IA ao Iniciar
Diga *“Olá! Eu li o arquivo RESUMO_PARA_IA.md. Pelo que vi, nosso próximo foco é começar a desenhar a super Tela de PDV (Frente de Caixa) com mock data. Está pronto para darmos partida nisso? Lembre-se que documentarei todos os passos no histórico e no log de implementação simultaneamente, de acordo com o `segurancaIA.md`.”*
