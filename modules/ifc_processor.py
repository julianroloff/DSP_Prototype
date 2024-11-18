import ifcopenshell

def extract_window_data(ifc_file):
    import ifcopenshell
    from utils.logger import setup_logger

    logger = setup_logger()
    try:
        model = ifcopenshell.open(ifc_file)
        logger.info(f"IFC Schema: {model.schema}")

        windows = model.by_type("IfcWindow")
        logger.info(f"Number of Windows Found: {len(windows)}")

        window_data = []
        for window in windows:
            logger.info(f"Processing Window: ID={window.GlobalId}, Name={window.Name}")
            u_value = None

            if hasattr(window, "IsDefinedBy"):
                for definition in window.IsDefinedBy:
                    if hasattr(definition, "RelatingPropertyDefinition"):
                        props = definition.RelatingPropertyDefinition.HasProperties
                        for prop in props:
                            if prop.Name == "UValue":
                                u_value = prop.NominalValue.wrappedValue
            window_data.append({
                "id": window.GlobalId,
                "name": window.Name,
                "u_value": u_value
            })

        return window_data
    except RuntimeError as e:
        logger.error(f"Error processing IFC file: {e}")
        return []



