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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\DrivenPile.rspile2")

pile_section_list = model.getPileTypes()

pile_type1 = pile_section_list[0]

pile_type1.setName("Driven Pile Type 1")
pile_type1.setColor(ColorPicker.Indigo)
pile_type1.Driven.Sections.setCrossSectionType(DrivenPileTypeCrossSection.TAPERED)
pile_type1.Driven.Sections.setTaperAngle(0.3)
pile_type1.Driven.Sections.setPileSegmentsByLength(1.2, [["Timber Pile Section", 20]])

model.save()
model.close()

rspile_modeler.closeApplication()