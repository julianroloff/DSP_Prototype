import ifcopenshell

# Create a new IFC file
ifc = ifcopenshell.file(schema="IFC4")

# Add a project
project = ifc.createIfcProject(GlobalId="1", Name="Sample Project")
ifc.add(project)

# Add a site
site = ifc.createIfcSite(GlobalId="2", Name="Sample Site")
ifc.add(site)

# Create a relationship between the project and the site
ifc.createIfcRelAggregates(
    GlobalId="3",
    RelatingObject=project,
    RelatedObjects=[site]
)

# Add a building
building = ifc.createIfcBuilding(GlobalId="4", Name="Sample Building")
ifc.add(building)

# Create a relationship between the site and the building
ifc.createIfcRelAggregates(
    GlobalId="5",
    RelatingObject=site,
    RelatedObjects=[building]
)

# Add a window
window = ifc.createIfcWindow(GlobalId="6", Name="Sample Window")
ifc.add(window)

# Create a relationship between the building and the window
ifc.createIfcRelAggregates(
    GlobalId="7",
    RelatingObject=building,
    RelatedObjects=[window]
)

# Define property sets for the window
property_set = ifc.createIfcPropertySet(
    GlobalId="8",
    Name="Pset_WindowCommon",
    HasProperties=[
        ifc.createIfcPropertySingleValue(
            Name="UValue",
            NominalValue=ifc.createIfcReal(1.8),  # Example UValue
            Unit=None,
        )
    ],
)
ifc.add(property_set)

# Link the property set to the window
ifc.createIfcRelDefinesByProperties(
    GlobalId="9",
    RelatingPropertyDefinition=property_set,
    RelatedObjects=[window]
)

# Save the IFC file
ifc.write("sample_building.ifc")
print("IFC file generated: sample_building.ifc")
