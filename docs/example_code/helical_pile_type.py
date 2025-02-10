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

pile_section_list = model.getPileTypes()

pile_type1 = pile_section_list[0]

pile_type1.setName("Circular Concrete Pile")
pile_type1.setColor(ColorPicker.Red)
pile_type1.Helical.Sections.setPileSegmentsByLength(1.2, [["Hollow Section", 10.01]])

helices = pile_type1.Helical.Sections.Helices
helices.setHeightReductionFactor(1.4)
#add identical 9 helices at a spacing of 0.5m each
helices.setHelicesBySpacing(6, [0.3, 0.1], ([[0.3, 0.1, 0.5] for i in range(8)]))

print(pile_type1.getName())
print(ColorPicker.getColorName(pile_type1.getColor()))
print(pile_type1.Helical.Sections.getPileSegmentsByLength())
print(pile_type1.Helical.Sections.Helices.getHelicesBySpacing())

model.save()
model.close()

rspile_modeler.closeApplication()