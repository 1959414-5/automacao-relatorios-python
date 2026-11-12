# Escopo de publicação, privacidade e limitações

## Natureza do repositório

Este repositório contém uma demonstração técnica independente, inspirada no estudo de caso apresentado no portfólio. Não é uma cópia nem uma distribuição do software corporativo original.

O código publicado implementa a parte independente de calendário: leitura de feriados e cálculo de dias úteis. A navegação operacional no ERP permanece fora do repositório.

## Conteúdo disponibilizado

- Código demonstrativo para cálculo de dias úteis.
- Arquivo CSV de exemplo com feriados fictícios.
- Testes unitários para as regras de calendário.
- Documentação da arquitetura e das limitações da automação por interface.

## Informações mantidas fora da publicação

O material público não contém:

- código-fonte proprietário da automação do ERP;
- credenciais, tokens, senhas ou endereços internos;
- coordenadas de mouse ou posições reais de campos;
- nomes de relatórios e parâmetros internos;
- caminhos locais, dados operacionais ou informações confidenciais;
- capturas proprietárias de telas corporativas.

## Limitações técnicas

A automação desktop depende do estado visual da aplicação, da resolução da tela, das posições dos controles e da sequência de navegação. Mudanças na interface podem exigir manutenção do fluxo.

Sempre que disponível, uma API, integração oficial ou rotina documentada tende a ser mais robusta que interações baseadas em coordenadas.

## Controles representados no estudo de caso

A arquitetura descrita prevê conferência humana dos parâmetros, possibilidade de cancelamento e validação dos arquivos gerados. Esses elementos fazem parte do desenho funcional apresentado no estudo de caso; não significam que a implementação completa do ERP esteja publicada aqui.
