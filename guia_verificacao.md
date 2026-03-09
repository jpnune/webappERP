# Guia de Verificação Humana - LolliPop

Este guia orienta como você deve acompanhar e validar cada passo do desenvolvimento realizado pela IA.

## 1. Rituais de Transparência
Ao final de cada sub-tarefa do `roadmap_tecnico.md`, a IA deve fornecer:

- **Proof of Work (Prova de Trabalho)**: Screenshots ou gravações de tela mostrando a funcionalidade rodando.
- **Relatório de Testes**: Saída do console mostrando que os testes (TDD) passaram (100% Green).
- **Resumo Semântico**: Uma explicação simples do que foi feito e por que é seguro.

## 2. Onde Verificar o Progresso?
- **[historico.md](file:///c:/Users/jpnun/Desktop/site_lollipop/historico.md)**: Veja as "commits" por data para saber exatamente quais arquivos foram tocados.
- **[implementation_log.md](file:///c:/Users/jpnun/Desktop/site_lollipop/implementation_log.md)**: Verifique se houve mudanças na arquitetura antes de autorizar o código.
- **[walkthrough.md](file:///c:/Users/jpnun/.gemini/antigravity/brain/2c6e3a24-0876-480a-b3c5-07fbdf8baa58/walkthrough.md)**: (Arquivo criado durante a execução) conterá os links para vídeos e imagens das telas prontas.

## 3. Pontos de Parada Críticos (Checkpoints)
Não avançaremos para a próxima fase sem sua aprovação explícita em:
1.  **Final da Fase 1**: Teste de abertura de banco criptografado com SQLCipher.
2.  **Final da Fase 2**: Simulação de conflito de estoque resolvida pelo Supervisor.
3.  **Final da Fase 4**: Aprovação visual do layout das telas.

## 4. Como Rejeitar uma Alteração?
Se você notar que algo não está conforme o planejado:
- Peça para "Reverter o último commit do historico.md".
- Aponte o erro citando a regra violada no `segurancaIA.md`.
