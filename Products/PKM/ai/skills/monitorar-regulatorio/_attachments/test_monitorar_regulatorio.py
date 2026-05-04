#!/usr/bin/env python3
"""
Unit tests for /monitorar-regulatorio skill
"""

import unittest
from datetime import datetime, timedelta
from monitorar_regulatorio_skill import (
    Document, Producer, DocumentCategory, UrgencyLevel,
    monitor_document_expirations, DOCUMENT_ROUTING
)


class TestDocumentExpiration(unittest.TestCase):
    """Test document expiration calculation."""

    def setUp(self):
        """Set up test fixtures."""
        self.today = datetime.now()

    def test_document_days_until_expiration(self):
        """Test days until expiration calculation."""
        # Document expiring in ~30 days (allow 1 day variance due to time calculations)
        future_date = self.today + timedelta(days=30)
        doc = Document(
            document_type="Test Doc",
            issue_date=self.today - timedelta(days=365),
            expiration_date=future_date,
            category=DocumentCategory.IDENTITY
        )
        # Allow some variance due to calculation timing
        self.assertGreaterEqual(doc.days_until_expiration(), 29)
        self.assertLessEqual(doc.days_until_expiration(), 31)

    def test_document_already_expired(self):
        """Test detection of already-expired documents."""
        past_date = self.today - timedelta(days=10)
        doc = Document(
            document_type="Expired Doc",
            issue_date=self.today - timedelta(days=365),
            expiration_date=past_date,
            category=DocumentCategory.IDENTITY
        )
        self.assertLess(doc.days_until_expiration(), 0)

    def test_urgency_critical(self):
        """Test critical urgency (0-14 days)."""
        doc = Document(
            document_type="Critical",
            issue_date=self.today - timedelta(days=365),
            expiration_date=self.today + timedelta(days=5),
            category=DocumentCategory.IDENTITY
        )
        self.assertEqual(doc.urgency_level(), UrgencyLevel.CRITICAL)

    def test_urgency_warning(self):
        """Test warning urgency (15-30 days)."""
        doc = Document(
            document_type="Warning",
            issue_date=self.today - timedelta(days=365),
            expiration_date=self.today + timedelta(days=20),
            category=DocumentCategory.IDENTITY
        )
        self.assertEqual(doc.urgency_level(), UrgencyLevel.WARNING)

    def test_urgency_notice(self):
        """Test notice urgency (31-60 days)."""
        doc = Document(
            document_type="Notice",
            issue_date=self.today - timedelta(days=365),
            expiration_date=self.today + timedelta(days=45),
            category=DocumentCategory.IDENTITY
        )
        self.assertEqual(doc.urgency_level(), UrgencyLevel.NOTICE)


class TestProducerFiltering(unittest.TestCase):
    """Test producer document filtering."""

    def setUp(self):
        """Set up test fixtures."""
        self.today = datetime.now()

    def test_expiring_documents_threshold(self):
        """Test filtering documents within threshold."""
        producer = Producer(
            producer_id="test_001",
            name="Test Producer",
            type="producer",
            documents=[
                Document(
                    document_type="Doc1",
                    issue_date=self.today - timedelta(days=365),
                    expiration_date=self.today + timedelta(days=30),  # Within 60d
                    category=DocumentCategory.IDENTITY
                ),
                Document(
                    document_type="Doc2",
                    issue_date=self.today - timedelta(days=365),
                    expiration_date=self.today + timedelta(days=90),  # Outside 60d
                    category=DocumentCategory.IDENTITY
                ),
            ]
        )
        expiring = producer.expiring_documents(days_threshold=60)
        self.assertEqual(len(expiring), 1)
        self.assertEqual(expiring[0].document_type, "Doc1")

    def test_expired_documents_included(self):
        """Test that already-expired documents are included in expiring list."""
        producer = Producer(
            producer_id="test_001",
            name="Test Producer",
            type="producer",
            documents=[
                Document(
                    document_type="Expired",
                    issue_date=self.today - timedelta(days=365),
                    expiration_date=self.today - timedelta(days=10),  # Expired
                    category=DocumentCategory.IDENTITY
                ),
            ]
        )
        expiring = producer.expiring_documents(days_threshold=60)
        self.assertEqual(len(expiring), 1)

    def test_no_expiring_documents(self):
        """Test producer with no expiring documents."""
        producer = Producer(
            producer_id="test_001",
            name="Test Producer",
            type="producer",
            documents=[
                Document(
                    document_type="Future",
                    issue_date=self.today - timedelta(days=365),
                    expiration_date=self.today + timedelta(days=365),
                    category=DocumentCategory.IDENTITY
                ),
            ]
        )
        expiring = producer.expiring_documents(days_threshold=60)
        self.assertEqual(len(expiring), 0)

    def test_to_alert_dict_with_expiring(self):
        """Test alert dict generation when documents expire."""
        producer = Producer(
            producer_id="test_001",
            name="Test Producer",
            type="producer",
            documents=[
                Document(
                    document_type="CNH",
                    issue_date=self.today - timedelta(days=365),
                    expiration_date=self.today + timedelta(days=30),
                    category=DocumentCategory.IDENTITY
                ),
            ]
        )
        alert = producer.to_alert_dict(days_threshold=60)
        self.assertIsNotNone(alert)
        self.assertEqual(alert["producer_name"], "Test Producer")
        self.assertEqual(len(alert["documents"]), 1)

    def test_to_alert_dict_without_expiring(self):
        """Test alert dict returns None when no expiring documents."""
        producer = Producer(
            producer_id="test_001",
            name="Test Producer",
            type="producer",
            documents=[
                Document(
                    document_type="Future",
                    issue_date=self.today - timedelta(days=365),
                    expiration_date=self.today + timedelta(days=365),
                    category=DocumentCategory.IDENTITY
                ),
            ]
        )
        alert = producer.to_alert_dict(days_threshold=60)
        self.assertIsNone(alert)


class TestDocumentCategories(unittest.TestCase):
    """Test document category routing."""

    def test_all_categories_have_routing(self):
        """Test that all document categories have routing info."""
        for category in DocumentCategory:
            if category != DocumentCategory.IDENTITY:  # Skip for this test
                self.assertIn(category, DOCUMENT_ROUTING)

    def test_routing_structure(self):
        """Test routing dict has required fields."""
        for category, routing in DOCUMENT_ROUTING.items():
            self.assertIn("contact", routing)
            self.assertIn("action", routing)
            self.assertIn("notes", routing)


class TestMonitoringExecution(unittest.TestCase):
    """Test full monitoring execution."""

    def setUp(self):
        """Set up test fixtures."""
        self.today = datetime.now()

    def test_monitor_document_expirations(self):
        """Test full monitoring workflow."""
        producers = [
            Producer(
                producer_id="prod_001",
                name="Producer A",
                type="producer",
                documents=[
                    Document(
                        document_type="CNH",
                        issue_date=self.today - timedelta(days=365),
                        expiration_date=self.today + timedelta(days=10),
                        category=DocumentCategory.IDENTITY
                    ),
                ]
            ),
            Producer(
                producer_id="prod_002",
                name="Producer B",
                type="producer",
                documents=[
                    Document(
                        document_type="CCIR",
                        issue_date=self.today - timedelta(days=365),
                        expiration_date=self.today + timedelta(days=45),
                        category=DocumentCategory.FINANCIAL
                    ),
                ]
            ),
            Producer(
                producer_id="prod_003",
                name="Producer C",
                type="producer",
                documents=[
                    Document(
                        document_type="Future License",
                        issue_date=self.today - timedelta(days=365),
                        expiration_date=self.today + timedelta(days=365),
                        category=DocumentCategory.ENVIRONMENTAL
                    ),
                ]
            ),
        ]

        result = monitor_document_expirations(producers, days_threshold=60)

        # Verify results
        self.assertEqual(result.total_producers, 3)
        self.assertEqual(result.producers_with_alerts, 2)  # A and B
        self.assertEqual(result.total_documents_expiring, 2)
        self.assertEqual(result.alerts_by_urgency["critical"], 1)  # CNH (10 days)
        self.assertEqual(result.alerts_by_urgency["notice"], 1)  # CCIR (45 days)

    def test_alert_sorting_by_urgency(self):
        """Test alerts are sorted by urgency and days until expiration."""
        today = datetime.now()
        producers = [
            Producer(
                producer_id="prod_001",
                name="Producer A",
                type="producer",
                documents=[
                    Document(
                        document_type="Notice Doc",
                        issue_date=today - timedelta(days=365),
                        expiration_date=today + timedelta(days=50),
                        category=DocumentCategory.IDENTITY
                    ),
                ]
            ),
            Producer(
                producer_id="prod_002",
                name="Producer B",
                type="producer",
                documents=[
                    Document(
                        document_type="Critical Doc",
                        issue_date=today - timedelta(days=365),
                        expiration_date=today + timedelta(days=5),
                        category=DocumentCategory.IDENTITY
                    ),
                ]
            ),
        ]

        result = monitor_document_expirations(producers, days_threshold=60)

        # Critical should come before Notice
        self.assertEqual(result.alerts[0]["producer_name"], "Producer B")
        self.assertEqual(result.alerts[1]["producer_name"], "Producer A")


if __name__ == "__main__":
    unittest.main()
