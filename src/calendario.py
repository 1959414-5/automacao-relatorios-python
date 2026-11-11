"""Funções demonstrativas para cálculo de dias úteis.

Este módulo é independente do sistema ERP corporativo.
Não contém configurações, caminhos ou calendários internos.
"""
from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Iterable


DATE_FORMAT = "%Y-%m-%d"


def carregar_feriados(caminho: str | Path) -> set[date]:
    """Carrega feriados de CSV com coluna obrigatória 'data' (YYYY-MM-DD).

    Linhas vazias são ignoradas. Datas inválidas geram ValueError com indicação
    da linha para facilitar a correção do arquivo.
    """
    arquivo = Path(caminho)
    if not arquivo.is_file():
        raise FileNotFoundError(f"Arquivo de feriados não encontrado: {arquivo}")

    feriados: set[date] = set()
    with arquivo.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or "data" not in reader.fieldnames:
            raise ValueError("O CSV precisa conter a coluna obrigatória 'data'.")

        for numero_linha, row in enumerate(reader, start=2):
            valor = (row.get("data") or "").strip()
            if not valor:
                continue
            try:
                feriados.add(datetime.strptime(valor, DATE_FORMAT).date())
            except ValueError as exc:
                raise ValueError(
                    f"Data inválida na linha {numero_linha}: {valor!r}. "
                    f"Use o formato {DATE_FORMAT}."
                ) from exc

    return feriados


def eh_dia_util(data: date, feriados: Iterable[date] = ()) -> bool:
    """Retorna True para dias de segunda a sexta que não sejam feriados."""
    return data.weekday() < 5 and data not in set(feriados)


def ultimo_dia_util_anterior(
    data_referencia: date, feriados: Iterable[date] = ()
) -> date:
    """Retorna o dia útil imediatamente anterior à data informada."""
    calendario = set(feriados)
    candidato = data_referencia - timedelta(days=1)

    while candidato.weekday() >= 5 or candidato in calendario:
        candidato -= timedelta(days=1)

    return candidato
