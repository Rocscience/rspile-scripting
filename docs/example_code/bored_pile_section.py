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

pile_section_list = model.getPileSections()

pile_section1 = pile_section_list[0]

pile_section1.setName("Circular Section")
pile_section1.setColor(ColorPicker.Light_Grey)
pile_section1.BoredCapacity.setConcreteCylinderStrength(100)
pile_section1.BoredCapacity.setCrossSectionType(BoredCrossSectionType.CIRCULAR)
pile_section1.BoredCapacity.Circular.setDiameter(1.2)

print(pile_section1.getName())
print(ColorPicker.getColorName(pile_section1.getColor()))
print(pile_section1.BoredCapacity.getCrossSectionType())
print(pile_section1.BoredCapacity.Circular.getDiameter())

model.save()
model.close()

rspile_modeler.closeApplication()