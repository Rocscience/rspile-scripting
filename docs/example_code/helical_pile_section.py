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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\HelicalPile.rspile2")

pile_section_list = model.getPileSections()

pile_section1 = pile_section_list[0]

pile_section1.setName("Hollow Section")
pile_section1.setColor(ColorPicker.Lime)
pile_section1.HelicalCapacity.setCrossSectionType(HelicalCrossSectionType.SQUARE_HOLLOW)
pile_section1.HelicalCapacity.SquareHollow.setOuterSideLength(0.2)
pile_section1.HelicalCapacity.SquareHollow.setThickness(0.02)


print(pile_section1.getName())
print(ColorPicker.getColorName(pile_section1.getColor()))
print(pile_section1.HelicalCapacity.getCrossSectionType())
print(pile_section1.HelicalCapacity.SquareHollow.getOuterSideLength())
print(pile_section1.HelicalCapacity.SquareHollow.getThickness())

model.save()
model.close()

rspile_modeler.closeApplication()