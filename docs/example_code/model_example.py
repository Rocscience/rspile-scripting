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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\ExampleModel.rspile2")

soil_property = model.getSoilProperties()[0]
pile_section = model.getPileSections()[0]
pile_type = model.getPileTypes()[0]

soil_property.setName("Silty Sand")
pile_section.setName("Concrete Pile")
pile_type.setName("Pile Type 1A")

model.save()

soil_property.setColor(ColorPicker.Gold)
pile_section.setColor(ColorPicker.Indigo)
pile_type.setColor(ColorPicker.Light_Blue)

model.save(rf"{current_dir}\example_models\ExampleModelSaveAs.rspile2")
model.compute()
model.close()

rspile_modeler.closeApplication()