# Roadmap Técnico Detalhado - LolliPop

Este roadmap agora segue a estratégia **Visual-First (Design-Driven)**, priorizando a validação da interface antes da infraestrutura robusta.

## Fase 1: MVP de Design e Frontend (Prototipagem Real)
- **Objetivo**: Criar a "casca" do programa com o visual premium para aprovação do UX.
- [ ] 1.1 Configuração do projeto WinUI 3 (Windows App SDK) e Tema LolliPop.
- [ ] 1.2 Implementação do Shell (Menu lateral, efeito Mica, navegação).
- [ ] 1.3 Criação da Tela de PDV (Vendas) com dados simulados (Dummy Data).
- [ ] 1.4 Criação da Tela de Dashboard/Supervisor (Mockup funcional).
- [ ] 1.5 Validação Humana: Aprovação do "Look & Feel" e fluxo de navegação.

## Fase 2: Infraestrutura e Base de Dados (Core)
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
