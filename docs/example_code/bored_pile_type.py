from rspile_scripting.RSPileModeler import RSPileModeler
from rspile_scripting.enums import *
from rspile_scripting.Utilities.ColorPicker import ColorPicker
import os, inspect

#TODO: Remove load_dotenv and overridePathToExecutable in startApplication prior to publish.
from dotenv import load_dotenv
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RSPileModeler.startApplication(
	overridePathToExecutable=os.getenv("PATH_TO_RSPILE_CPP_REPO") + "\\Build\\Debug_x64\\RSPile.exe", 
	port=60044
	)

rspile_modeler = RSPileModeler(60044)
model = rspile_modeler.openFile(rf"{current_dir}\example_models\BoredPile.rspile2")

pile_section_list = model.getPileTypes()

pile_type1 = pile_section_list[0]

pile_type1.setName("Circular Concrete Pile")
pile_type1.setColor(ColorPicker.Red)
pile_type1.Bored.Sections.setCrossSectionType(BoredPileTypeCrossSection.BELL)
pile_type1.Bored.Sections.setPileSegmentsByLength(1.2, [["Circular Section", 32]])

bell = pile_type1.Bored.Sections.Bell
bell.setLengthAboveBell(0.5)
bell.setAngle(45)
bell.setBaseThickness(0.2)
bell.setBaseDiameterDefinitionType(BaseDiamaterDefinitionType.VALUE)
bell.setBaseDiameter(3)

model.save()
model.close()

rspile_modeler.closeApplication()