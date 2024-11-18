import csv

def save_results_to_csv(results, output_file="data/compliance_report.csv"):
    """Saves SPARQL query results to a CSV file in the data directory.

    Args:
        results (dict): SPARQL query results in JSON format.
        output_file (str): Path to the CSV file.
    """
    import os

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Window", "U-Value", "Regulation", "Max Allowed"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results["results"]["bindings"]:
            writer.writerow({
                "Window": result['window']['value'],
                "U-Value": result['uValue']['value'],
                "Regulation": result['regulation']['value'],
                "Max Allowed": result['maxUValue']['value']
            })
    print(f"Results saved to {output_file}")

