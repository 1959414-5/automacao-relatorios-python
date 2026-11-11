# Arquitetura demonstrativa

## Objetivo

Demonstrar uma separação simples entre preparação de datas, apresentação de parâmetros, automação da interface e validação dos resultados.

## Componentes do estudo de caso

- **Calendário:** interpreta a lista de feriados e calcula o último dia útil anterior.
- **Interface auxiliar:** permite configurar parâmetros e revisar datas.
- **Automação desktop:** utiliza interações de mouse e teclado para operar uma interface ERP.
- **Controles:** oferece cancelamento, mensagens e conferência dos resultados.

## Fluxo lógico

```text
Início
  |
  v
Carregar calendário de feriados
  |
  v
Calcular datas de referência
  |
  v
Apresentar parâmetros para conferência
  |
  +---- Cancelar ---> Encerrar
  |
  v
Executar rotina demonstrativa de interface
  |
  v
Conferir arquivos e resultados
  |
  v
Encerrar
```

O código disponibilizado neste repositório implementa somente a parte independente de calendário. A navegação no ERP original não é publicada.
