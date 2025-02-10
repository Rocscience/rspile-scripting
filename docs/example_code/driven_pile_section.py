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

pile_section_list = model.getPileSections()

pile_section1 = pile_section_list[0]
pile_section2 = pile_section_list[1]

pile_section1.setName("Timber Pile Section")
pile_section1.setColor(ColorPicker.Rose)
pile_section1.DrivenCapacity.setCrossSectionType(DrivenCrossSectionType.TIMBER_PILE)
pile_section1.DrivenCapacity.Timber.setDiameterOfPile(0.6)

pile_section2.setName("H Pile Section")
pile_section2.setColor(ColorPicker.Gold)
pile_section2.DrivenCapacity.setCrossSectionType(DrivenCrossSectionType.H_PILE)
pile_section2.DrivenCapacity.HPile.setHPileTypeMetric(HPileTypeMetric.HP_360x132)
pile_section2.DrivenCapacity.HPile.setHPilePerimeter(HPilePerimeter.H_BOX_PERIMETER)
pile_section2.DrivenCapacity.HPile.setHPileArea(HPileArea.H_PILE_AREA)

print(pile_section1.getName)
print(ColorPicker.getColorName(pile_section1.getColor()))
print(pile_section1.DrivenCapacity.getCrossSectionType())
print(pile_section1.DrivenCapacity.Timber.getDiameterOfPile())

print(pile_section2.getName)
print(ColorPicker.getColorName(pile_section2.getColor()))
print(pile_section2.DrivenCapacity.getCrossSectionType())
print(pile_section2.DrivenCapacity.HPile.getHPileTypeMetric())
print(pile_section2.DrivenCapacity.HPile.getHPilePerimeter())
print(pile_section2.DrivenCapacity.HPile.getHPileArea())

model.save()
model.close()

rspile_modeler.closeApplication()