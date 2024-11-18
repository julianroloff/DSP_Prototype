from SPARQLWrapper import SPARQLWrapper, JSON
from utils.csv_writer import save_results_to_csv

def validate_windows(endpoint="http://localhost:3030/dataset/sparql", csv_output="data/compliance_report.csv"):
    """Validates windows against regulations."""
    sparql = SPARQLWrapper(endpoint)

    sparql.setQuery("""
        PREFIX ex: <http://example.com/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT ?window ?uValue ?regulation ?maxUValue
        WHERE {
            ?window a ex:Window ;
                    ex:uValue ?uValue .
            ?regulation a ex:Regulation ;
                         ex:appliesTo ex:Window ;
                         ex:maxUValue ?maxUValue .
            FILTER (xsd:float(?uValue) > xsd:float(?maxUValue))
        }
    """)

    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()

        if not results["results"]["bindings"]:
            print("All windows are compliant.")
        else:
            for result in results["results"]["bindings"]:
                print(f"Non-Compliant Window: {result['window']['value']}, "
                      f"U-Value: {result['uValue']['value']}, "
                      f"Regulation: {result['regulation']['value']}, "
                      f"Max Allowed: {result['maxUValue']['value']}")

            # Save results to CSV in the data directory
            save_results_to_csv(results, output_file=csv_output)
    except Exception as e:
        print("An error occurred while executing the query:", e)

