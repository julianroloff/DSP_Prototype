from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

def create_rdf(windows, output_path="data/building_data.ttl"):
    """Generates RDF from extracted window data."""
    g = Graph()
    ex = Namespace("http://example.com/")
    g.bind("ex", ex)

    for window in windows:
        window_node = URIRef(ex[f"Window_{window['id']}"])
        g.add((window_node, RDF.type, ex.Window))
        g.add((window_node, ex.name, Literal(window['name'], datatype=XSD.string)))
        if window['u_value'] is not None:
            g.add((window_node, ex.uValue, Literal(window['u_value'], datatype=XSD.float)))

    g.serialize(output_path, format="turtle")
    print("Building data saved as RDF!")

def load_regulation_data(file_path):
    """Loads regulation data into an RDF graph."""
    g = Graph()
    g.parse(file_path, format="turtle")
    for subj, pred, obj in g:
        print(f"Subject: {subj}, Predicate: {pred}, Object: {obj}")
