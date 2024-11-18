import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Validate building data against regulations.")
    parser.add_argument("--ifc", required=True, help="Path to the IFC file.")
    parser.add_argument("--output", default="data/building_data.ttl", help="Path to save the RDF file.")
    parser.add_argument("--csv_output", default="data/compliance_report.csv", help="Path to save the CSV compliance report.")
    return parser.parse_args()

