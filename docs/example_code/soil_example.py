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

soil_property_list = model.getSoilProperties()

soil1 = soil_property_list[0]
soil2 = soil_property_list[1]

soil1.setName("Glacial Till")
soil1.setColor(ColorPicker.Indigo)
soil1.setHatch(HatchStyle.HORIZONTAL)
soil1.setUseDatumDependency(True)
soil1.setUseSaturatedUnitWeight(True)
soil1.setUnitWeight(21.0)
soil1.setSaturatedUnitWeight(22.0)

print(soil1.getName())
print(ColorPicker.getColorName(soil1.getColor()))
print(soil1.getHatch())
print(soil1.getUseDatumDependency())
print(soil1.getUseSaturatedUnitWeight())
print(soil1.getUnitWeight())
print(soil1.getSaturatedUnitWeight())

soil2.setName("Sandy Clay")
soil2.setColor(ColorPicker.Gold)
soil2.setHatch(HatchStyle.VERTICAL)
soil2.setUseDatumDependency(False)
soil2.setUseSaturatedUnitWeight(False)
soil2.setUnitWeight(19.5)

print(soil2.getName())
print(ColorPicker.getColorName(soil2.getColor()))
print(soil2.getHatch())
print(soil2.getUseDatumDependency())
print(soil2.getUseSaturatedUnitWeight())
print(soil2.getUnitWeight())

model.save()
model.close()

rspile_modeler.closeApplication()