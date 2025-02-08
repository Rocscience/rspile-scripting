from rspile_scripting.RSPileModeler import RSPileModeler
from rspile_scripting.enums import *
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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\LatAxPileAnalysis.rspile2")

soil_property_list = model.getSoilProperties()

soil1 = soil_property_list[0]
soil2 = soil_property_list[1]

soil1.setName("Sand")
soil1.setUnitWeight(19)
soil1.AxialProperties.setAxialType(AxialType.DRILLED_SAND)
soil1.AxialProperties.DrilledSand.setUltimateEndBearingResistance(12000)
soil1.AxialProperties.DrilledSand.setUltimateShearResistance(9000)

soil2.setName("Clay")
soil2.setUnitWeight(19.7)
soil2.AxialProperties.setAxialType(AxialType.API_CLAY)
soil2.AxialProperties.APIClay.setUndrainedShearStrength(45)
soil2.AxialProperties.APIClay.setRemoldedShearStrength(25)
soil2.AxialProperties.APIClay.setMaximumUnitSkinFriction(12000)
soil2.AxialProperties.APIClay.setMaximumUnitEndBearingResistance(10000)
soil2.setUseDatumDependency(True)
soil2.AxialProperties.APIClay.Datum.setDatum(AxialAPIClayDatumProperties.UNDRAINED_SHEAR_STRENGTH, 120)
soil2.AxialProperties.APIClay.Datum.setDatum(AxialAPIClayDatumProperties.REMOLDED_SHEAR_STRENGTH, 65)

print(soil1.getName())
print(soil1.getUnitWeight())
print(soil1.AxialProperties.getAxialType())
print(soil1.AxialProperties.DrilledSand.getUltimateEndBearingResistance())
print(soil1.AxialProperties.DrilledSand.getUltimateShearResistance())

print(soil2.getName())
print(soil2.getUnitWeight())
print(soil2.AxialProperties.getAxialType())
print(soil2.AxialProperties.APIClay.getUndrainedShearStrength())
print(soil2.AxialProperties.APIClay.getRemoldedShearStrength())
print(soil2.AxialProperties.APIClay.getMaximumUnitSkinFriction())
print(soil2.AxialProperties.APIClay.getMaximumUnitEndBearingResistance())

print(soil2.AxialProperties.APIClay.Datum.getDatum(AxialAPIClayDatumProperties.UNDRAINED_SHEAR_STRENGTH))
print(soil2.AxialProperties.APIClay.Datum.getDatum(AxialAPIClayDatumProperties.REMOLDED_SHEAR_STRENGTH))

model.save()
model.close()

rspile_modeler.closeApplication()