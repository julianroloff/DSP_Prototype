from modules.ifc_processor import extract_window_data
from modules.rdf_manager import create_rdf, load_regulation_data
from modules.validator import validate_windows
from utils.config import FUSEKI_ENDPOINT, REGULATIONS_PATH
from utils.logger import setup_logger
from utils.cli_parser import parse_args

logger = setup_logger()

def main():
    args = parse_args()

    # Step 1: Extract window data from IFC
    logger.info(f"Extracting window data from IFC file: {args.ifc}")
    windows = extract_window_data(args.ifc)

    # Step 2: Create RDF from window data
    logger.info(f"Creating RDF for building data: {args.output}")
    create_rdf(windows, args.output)

    # Step 3: Load regulation data
    logger.info(f"Loading regulation data from: {REGULATIONS_PATH}")
    load_regulation_data(REGULATIONS_PATH)

    # Step 4: Validate windows
    logger.info("Validating windows against regulations...")
    validate_windows(FUSEKI_ENDPOINT, csv_output=args.csv_output)

if __name__ == "__main__":
    main()
