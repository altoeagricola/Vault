#!/usr/bin/env python3
"""
Vault Data Adapter - Interface for querying producer/client records from Vault

This module provides a flexible interface for accessing Vault data,
with implementations for different data sources (file-based, API-based, etc.)
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime
import json
import os


class VaultAdapter(ABC):
    """Abstract base class for Vault data sources."""

    @abstractmethod
    def get_producers(self, producer_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """
        Get producer records from Vault.

        Args:
            producer_ids: Optional list of specific producer IDs to fetch.
                         If None, returns all producers.

        Returns:
            List of producer dictionaries with structure:
            {
                "producer_id": str,
                "name": str,
                "type": str ("producer" | "client" | "partner"),
                "documents": [
                    {
                        "document_type": str,
                        "issue_date": str (ISO 8601),
                        "expiration_date": str (ISO 8601),
                        "category": str,
                        "notes": str (optional)
                    }
                ]
            }
        """
        pass


class FileSystemVaultAdapter(VaultAdapter):
    """
    File-system based Vault adapter.

    Reads producer data from JSON files organized in the Vault structure:
    Products/CRM/producers/{producer_id}.json
    """

    def __init__(self, vault_root: str):
        """
        Initialize file-system adapter.

        Args:
            vault_root: Root path to the Vault directory
        """
        self.vault_root = vault_root
        self.producers_dir = os.path.join(vault_root, "Products/CRM/producers")

    def get_producers(self, producer_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Get producer records from Vault JSON files."""
        producers = []

        if not os.path.exists(self.producers_dir):
            raise FileNotFoundError(f"Producers directory not found: {self.producers_dir}")

        # If specific IDs requested, fetch those
        if producer_ids:
            for pid in producer_ids:
                filepath = os.path.join(self.producers_dir, f"{pid}.json")
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        producers.append(json.load(f))
        else:
            # Fetch all producer files
            for filename in os.listdir(self.producers_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.producers_dir, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            producers.append(json.load(f))
                    except json.JSONDecodeError:
                        print(f"Warning: Could not parse {filename}")
                        continue

        return producers


class MarkdownVaultAdapter(VaultAdapter):
    """
    Markdown-based Vault adapter.

    Parses producer data from Markdown files with frontmatter (YAML metadata).
    Format:
    ---
    producer_id: prod_001
    name: João Silva
    type: producer
    documents:
      - document_type: CNH
        expiration_date: 2026-06-10
        category: identity
    ---
    """

    def __init__(self, vault_root: str):
        """
        Initialize Markdown adapter.

        Args:
            vault_root: Root path to the Vault directory
        """
        self.vault_root = vault_root
        self.producers_dir = os.path.join(vault_root, "Areas", "Connections", "Producers")

    def get_producers(self, producer_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Get producer records from Vault Markdown files."""
        producers = []

        if not os.path.exists(self.producers_dir):
            raise FileNotFoundError(f"Producers directory not found: {self.producers_dir}")

        # Fetch markdown files
        for filename in os.listdir(self.producers_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(self.producers_dir, filename)
                try:
                    producer_data = self._parse_markdown(filepath)
                    if producer_data and (not producer_ids or producer_data.get("producer_id") in producer_ids):
                        producers.append(producer_data)
                except Exception as e:
                    print(f"Warning: Could not parse {filename}: {e}")
                    continue

        return producers

    @staticmethod
    def _parse_markdown(filepath: str) -> Optional[Dict[str, Any]]:
        """Parse Markdown file with YAML frontmatter."""
        try:
            import yaml
        except ImportError:
            raise ImportError("PyYAML required for Markdown parsing. Install with: pip install pyyaml")

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                data = yaml.safe_load(yaml_content)
                return data

        return None


class MockVaultAdapter(VaultAdapter):
    """Mock Vault adapter for testing - returns sample data."""

    def get_producers(self, producer_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Return mock producer data for testing."""
        today = datetime.now()
        mock_data = [
            {
                "producer_id": "prod_001",
                "name": "João Silva",
                "type": "producer",
                "documents": [
                    {
                        "document_type": "CNH",
                        "issue_date": "2020-05-15",
                        "expiration_date": (today.replace(day=10, month=6)).isoformat(),
                        "category": "identity",
                        "notes": "Documento de identidade"
                    },
                    {
                        "document_type": "CCIR",
                        "issue_date": "2023-03-01",
                        "expiration_date": (today.replace(day=1, month=3) - __import__('datetime').timedelta(days=60)).isoformat(),
                        "category": "financial",
                        "notes": "Já vencido"
                    }
                ]
            },
            {
                "producer_id": "prod_002",
                "name": "Maria Santos",
                "type": "client",
                "documents": [
                    {
                        "document_type": "Contrato de Fomento",
                        "issue_date": "2025-06-01",
                        "expiration_date": (today.replace(month=8, day=31) + __import__('datetime').timedelta(days=60)).isoformat(),
                        "category": "fomento"
                    }
                ]
            }
        ]

        if producer_ids:
            return [p for p in mock_data if p["producer_id"] in producer_ids]
        return mock_data


def get_vault_adapter(vault_type: str = "filesystem", vault_root: Optional[str] = None) -> VaultAdapter:
    """
    Factory function to get appropriate Vault adapter.

    Args:
        vault_type: Type of adapter ("filesystem", "markdown", "mock")
        vault_root: Root path to Vault (required for filesystem and markdown)

    Returns:
        VaultAdapter instance
    """
    if vault_type == "filesystem":
        if not vault_root:
            raise ValueError("vault_root required for filesystem adapter")
        return FileSystemVaultAdapter(vault_root)
    elif vault_type == "markdown":
        if not vault_root:
            raise ValueError("vault_root required for markdown adapter")
        return MarkdownVaultAdapter(vault_root)
    elif vault_type == "mock":
        return MockVaultAdapter()
    else:
        raise ValueError(f"Unknown vault_type: {vault_type}")
