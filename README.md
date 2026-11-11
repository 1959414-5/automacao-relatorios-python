<p align="center">
  <img src="https://img.shields.io/badge/PYTHON-AUTOMAÇÃO-f15aa7?style=for-the-badge&labelColor=150f18&logo=python&logoColor=fbf4fa" alt="Python automation" />
  <img src="https://img.shields.io/badge/ERP-DESKTOP%20RPA-35263d?style=for-the-badge&labelColor=150f18" alt="ERP desktop RPA" />
</p>

<h1 align="center">Automação de Relatórios com Python</h1>

<p align="center">
  <strong>Automação desktop para padronizar rotinas recorrentes de relatórios em um ERP.</strong><br/>
  <sub>Projeto demonstrativo inspirado em um estudo de caso real, com ambiente e dados corporativos preservados.</sub>
</p>

<p align="center">
  <a href="https://1959414-5.github.io/meu-portfolio/projeto-automacao-relatorios.html">
    <img src="https://img.shields.io/badge/VER_ESTUDO_DE_CASO-f15aa7?style=for-the-badge&logo=googlechrome&logoColor=fbf4fa" alt="Ver estudo de caso" />
  </a>
  <a href="https://github.com/1959414-5">
    <img src="https://img.shields.io/badge/GITHUB-35263d?style=for-the-badge&logo=github&logoColor=fbf4fa" alt="GitHub" />
  </a>
</p>

---

## Visão geral

Este repositório apresenta uma **implementação demonstrativa e independente** de uma automação desktop para apoiar a geração recorrente de relatórios em um sistema ERP.

A solução de referência foi desenvolvida em Python para reduzir etapas manuais de navegação, preenchimento de filtros, geração de arquivos e atualização de informações em planilhas.

O projeto foi organizado conceitualmente em quatro responsabilidades:

1. **Preparação do calendário:** leitura de feriados e cálculo de datas úteis.
2. **Conferência:** apresentação dos parâmetros calculados antes da execução.
3. **Automação desktop:** interação com a interface por mouse e teclado.
4. **Controles:** mecanismos de interrupção, configuração e mensagens de execução.

> **Importante:** este repositório não contém o código-fonte proprietário utilizado no ambiente corporativo. Os exemplos publicados são independentes e didáticos. Não há credenciais, coordenadas reais, nomes de relatórios internos, dados operacionais ou configurações da empresa.

## Resultado observado no estudo de caso

| Indicador | Processo manual | Com automação |
|---|---:|---:|
| Tempo médio por execução | 40 minutos | 10 minutos |
| Tempo economizado | — | 30 minutos |
| Redução de tempo | — | 75% |

<sub>Valores médios descritos no estudo de caso. O tempo pode variar de acordo com a quantidade de relatórios e a necessidade de conferência.</sub>

## Arquitetura demonstrativa

```text
automacao-relatorios-python/
├── src/
│   └── calendario.py
├── tests/
│   └── test_calendario.py
├── data/
│   └── feriados.example.csv
├── docs/
│   ├── arquitetura.md
│   └── seguranca-e-limitacoes.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Tecnologias e recursos

<p>
  <img src="https://img.shields.io/badge/Python-35263d?style=for-the-badge&logo=python&logoColor=fbf4fa" alt="Python" />
  <img src="https://img.shields.io/badge/PyAutoGUI-35263d?style=for-the-badge&logo=python&logoColor=fbf4fa" alt="PyAutoGUI" />
  <img src="https://img.shields.io/badge/Tkinter-35263d?style=for-the-badge&logo=windowsterminal&logoColor=fbf4fa" alt="Tkinter" />
  <img src="https://img.shields.io/badge/Pyperclip-35263d?style=for-the-badge&logo=python&logoColor=fbf4fa" alt="Pyperclip" />
  <img src="https://img.shields.io/badge/CSV_/_JSON-35263d?style=for-the-badge&logo=files&logoColor=fbf4fa" alt="CSV e JSON" />
  <img src="https://img.shields.io/badge/Windows-35263d?style=for-the-badge&logo=windows&logoColor=fbf4fa" alt="Windows" />
</p>

- **Python:** linguagem principal.
- **PyAutoGUI:** interação automatizada com mouse e teclado.
- **Pyperclip:** apoio à colagem de texto na interface.
- **Tkinter:** construção de interfaces auxiliares.
- **CSV e JSON:** armazenamento de feriados e configurações demonstrativas.
- **datetime:** cálculo e manipulação de datas.
- **threading:** organização de execução de tarefas em interface desktop.

## Exemplo demonstrativo: calendário de dias úteis

O módulo `src/calendario.py` implementa uma regra reutilizável para encontrar o dia útil anterior, desconsiderando sábados, domingos e feriados cadastrados em arquivo CSV.

### Executar localmente

Requisitos: Python 3.10 ou superior.

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
python -m unittest discover -s tests -v
```

## Decisões técnicas e limitações

A automação por interface é útil quando o sistema não oferece uma API ou integração adequada para a tarefa. Entretanto, exige cuidados:

- A janela do ERP precisa estar no estado esperado.
- Coordenadas e resolução de tela podem afetar a execução.
- Alterações na interface podem exigir ajustes.
- O usuário deve evitar interferência no mouse e teclado durante a rotina.
- Uma execução automatizada precisa de validação dos arquivos gerados.
- Quando disponível, uma API ou integração nativa tende a ser mais robusta que automação por coordenadas.

## Segurança e privacidade

- Não inclua credenciais, tokens ou senhas no código.
- Não publique coordenadas de telas corporativas.
- Utilize somente dados fictícios ou anonimizados nos exemplos.
- Revise capturas de tela antes de publicá-las.
- Não reproduza nomes de relatórios, caminhos internos ou informações confidenciais.

Consulte [docs/seguranca-e-limitacoes.md](docs/seguranca-e-limitacoes.md) para mais detalhes.

## Autoria

**Bárbara Cabral Paschoalin**  
Análise de Dados · Business Intelligence · Automação

- [Portfólio](https://1959414-5.github.io/meu-portfolio/)
- [LinkedIn](https://www.linkedin.com/in/b%C3%A1rbara-paschoalin-980b52185/)
- [GitHub](https://github.com/1959414-5)

---

<p align="center">
  <sub>Automação aplicada a processos reais, com foco em eficiência, consistência e segurança.</sub>
</p>
