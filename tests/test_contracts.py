import unittest

from src.utilities import SourceContract


class SourceContractTest(unittest.TestCase):
    def test_source_contract_requires_business_key(self) -> None:
        contract = SourceContract(
            name="purchase_orders",
            grain="one row per purchase order",
            business_keys=(),
            event_time_column="updated_at",
            arrival_time_column="ingested_at",
            change_mode="cdc",
        )

        with self.assertRaisesRegex(ValueError, "business key"):
            contract.validate()


if __name__ == "__main__":
    unittest.main()
