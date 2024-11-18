import streamlit as st
from modules.ifc_processor import extract_window_data
from modules.rdf_manager import create_rdf, load_regulation_data
from modules.validator import validate_windows
from utils.config import FUSEKI_ENDPOINT, BUILDING_DATA_PATH, REGULATIONS_PATH
from utils.csv_writer import save_results_to_csv

def main():
    st.title("Building Compliance Validator")

    # File upload
    uploaded_file = st.file_uploader("Upload IFC File", type=["ifc"])
    output_csv = "data/compliance_report.csv"

    if uploaded_file:
        st.info(f"Uploaded file: {uploaded_file.name}")

        # Save the uploaded file temporarily
        with open("data/temp.ifc", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Process the IFC file
        st.write("Extracting window data...")
        windows = extract_window_data("data/temp.ifc")
        st.write(f"Number of Windows Found: {len(windows)}")

        # Create RDF
        st.write("Creating RDF...")
        create_rdf(windows, BUILDING_DATA_PATH)

        # Load regulations
        st.write("Loading regulation data...")
        load_regulation_data(REGULATIONS_PATH)

        # Validate compliance
        st.write("Validating windows...")
        validate_windows(FUSEKI_ENDPOINT, csv_output=output_csv)
        st.success(f"Results saved to {output_csv}")

        # Show results
        with open(output_csv, "r") as csvfile:
            st.download_button(
                label="Download Compliance Report",
                data=csvfile,
                file_name="compliance_report.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()

