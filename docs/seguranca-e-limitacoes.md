# Segurança, privacidade e limitações

## O que não é publicado

O projeto original foi utilizado em um ambiente corporativo. Por isso, este repositório não disponibiliza:

- código-fonte original da automação do ERP;
- coordenadas de mouse ou posições de campos;
- nomes de relatórios e parâmetros internos;
- credenciais, endereços de e-mail ou caminhos locais;
- dados reais da empresa ou capturas de telas proprietárias.

## Limitações de automação por interface

Automação desktop depende do estado visual da aplicação, da resolução da tela, das posições dos controles e da sequência de navegação. Alterações no ERP podem quebrar o fluxo automatizado.

Sempre que possível, prefira APIs, integrações oficiais, filas ou rotinas de importação/exportação documentadas pelo fornecedor do sistema.

## Controles recomendados

- Confirmação humana de parâmetros antes da execução.
- Mecanismo de interrupção acessível durante todo o processo.
- Logs sem dados pessoais ou informações sensíveis.
- Validação dos arquivos gerados antes de atualizar sistemas externos.
- Uso de ambiente de teste e dados fictícios para desenvolvimento.

## Natureza deste repositório

O conteúdo é uma demonstração técnica independente, inspirada no estudo de caso descrito no portfólio da autora. Não é uma cópia nem uma distribuição do software corporativo original.
