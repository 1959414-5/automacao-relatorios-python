"""Testes unitários do calendário demonstrativo."""
import csv
import tempfile
import unittest
from datetime import date
from pathlib import Path

from src.calendario import (
    carregar_feriados,
    eh_dia_util,
    ultimo_dia_util_anterior,
)


class CalendarioTests(unittest.TestCase):
    def test_dia_de_semana_sem_feriado_e_util(self):
        self.assertTrue(eh_dia_util(date(2026, 11, 9)))

    def test_fim_de_semana_nao_e_util(self):
        self.assertFalse(eh_dia_util(date(2026, 11, 14)))
        self.assertFalse(eh_dia_util(date(2026, 11, 15)))

    def test_feriado_nao_e_util(self):
        feriados = {date(2026, 11, 10)}
        self.assertFalse(eh_dia_util(date(2026, 11, 10), feriados))

    def test_calcula_dia_util_anterior_considerando_feriado_e_fim_de_semana(self):
        feriados = {date(2026, 11, 9)}
        resultado = ultimo_dia_util_anterior(date(2026, 11, 10), feriados)
        self.assertEqual(resultado, date(2026, 11, 6))

    def test_carrega_csv_de_feriados(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            caminho = Path(temp_dir) / "feriados.csv"
            with caminho.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(["data", "descricao"])
                writer.writerow(["2026-11-20", "Feriado fictício"])

            self.assertEqual(
                carregar_feriados(caminho),
                {date(2026, 11, 20)},
            )

    def test_rejeita_data_invalida_no_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            caminho = Path(temp_dir) / "feriados.csv"
            caminho.write_text("data\n31/12/2026\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                carregar_feriados(caminho)


if __name__ == "__main__":
    unittest.main()
