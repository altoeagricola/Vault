#!/usr/bin/env python3
"""
Integration tests for /monitorar-regulatorio skill
"""

import unittest
import json
from datetime import datetime, timedelta

from monitorar_regulatorio_integrated import MonitoringService
from vault_adapter import MockVaultAdapter


class TestMonitoringServiceIntegration(unittest.TestCase):
    """Test monitoring service with Vault adapter integration."""

    def setUp(self):
        """Set up test fixtures."""
        self.vault = MockVaultAdapter()
        self.service = MonitoringService(self.vault)

    def test_run_monitoring_json_format(self):
        """Test monitoring with JSON output."""
        result = self.service.run_monitoring(
            days_threshold=60,
            output_format="json"
        )

        # Parse JSON result
        data = json.loads(result)

        # Verify structure
        self.assertIn("run_timestamp", data)
        self.assertIn("days_threshold", data)
        self.assertIn("total_producers", data)
        self.assertIn("alerts", data)
        self.assertEqual(data["days_threshold"], 60)

    def test_run_monitoring_markdown_format(self):
        """Test monitoring with Markdown output."""
        result = self.service.run_monitoring(
            days_threshold=60,
            output_format="markdown"
        )

        # Verify Markdown structure
        self.assertIn("# Relatório", result)
        self.assertIn("## Resumo", result)
        self.assertIn("Documentos Vencendo", result)

    def test_run_monitoring_csv_format(self):
        """Test monitoring with CSV output."""
        result = self.service.run_monitoring(
            days_threshold=60,
            output_format="csv"
        )

        # Verify CSV structure
        lines = result.strip().split('\n')
        self.assertGreater(len(lines), 0)
        self.assertIn("producer_id", lines[0])  # Header
        self.assertIn("producer_name", lines[0])

    def test_run_monitoring_with_specific_producers(self):
        """Test monitoring with specific producer IDs."""
        result = self.service.run_monitoring(
            producer_ids=["prod_001"],
            days_threshold=60,
            output_format="json"
        )

        data = json.loads(result)
        self.assertEqual(data["total_producers"], 1)

    def test_run_monitoring_with_different_threshold(self):
        """Test monitoring with different day threshold."""
        # 30-day threshold should have fewer alerts than 60-day
        result_30 = self.service.run_monitoring(
            days_threshold=30,
            output_format="json"
        )
        data_30 = json.loads(result_30)

        result_60 = self.service.run_monitoring(
            days_threshold=60,
            output_format="json"
        )
        data_60 = json.loads(result_60)

        self.assertLessEqual(
            data_30["total_documents_expiring"],
            data_60["total_documents_expiring"]
        )

    def test_build_producer_objects(self):
        """Test conversion of Vault data to Producer objects."""
        vault_data = self.vault.get_producers()
        producers = MonitoringService._build_producer_objects(vault_data)

        self.assertGreater(len(producers), 0)
        for producer in producers:
            self.assertTrue(hasattr(producer, "producer_id"))
            self.assertTrue(hasattr(producer, "name"))
            self.assertTrue(hasattr(producer, "documents"))

    def test_format_markdown_output(self):
        """Test Markdown formatting."""
        result = self.service.run_monitoring(
            days_threshold=60,
            output_format="markdown"
        )

        # Check for expected Markdown elements
        self.assertIn("# Relatório", result)
        self.assertIn("## Resumo", result)
        self.assertIn("| Documento | Categoria |", result)

    def test_format_csv_output(self):
        """Test CSV formatting."""
        result = self.service.run_monitoring(
            days_threshold=60,
            output_format="csv"
        )

        lines = result.strip().split('\n')
        # Should have header + at least one data row
        self.assertGreaterEqual(len(lines), 2)

        # Check CSV columns
        header = lines[0]
        self.assertIn("producer_id", header)
        self.assertIn("expiration_date", header)
        self.assertIn("urgency", header)

    def test_error_handling_invalid_format(self):
        """Test error handling for invalid output format."""
        result = self.service.run_monitoring(
            days_threshold=60,
            output_format="invalid"
        )

        # Should return error JSON
        data = json.loads(result)
        self.assertIn("error", data)
        self.assertEqual(data["status"], "failed")

    def test_error_handling_invalid_producer_data(self):
        """Test handling of malformed producer data."""
        # This would be tested with a custom mock adapter
        # that returns invalid data
        pass


if __name__ == "__main__":
    unittest.main()
