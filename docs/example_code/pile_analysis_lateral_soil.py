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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\LatAxPileAnalysis.rspile2")

soil_property_list = model.getSoilProperties()

soil1 = soil_property_list[0]
soil2 = soil_property_list[1]

soil1.setName("Sandy Silt")
soil1.setUnitWeight(19.6)
soil1.setUseDatumDependency(True)
soil1.LateralProperties.setLateralType(LateralType.SILT)
silt_props = soil1.LateralProperties.Silt

silt_props.setCohesion(0)
silt_props.setFrictionAngle(28)
silt_props.setInitialStiffness(30000)
silt_props.Datum.setDatum(LateralSiltDatumProperties.COHESION, 5)
silt_props.Datum.setDatum(LateralSiltDatumProperties.FRICTION_ANGLE, 35)
silt_props.Datum.setDatum(LateralSiltDatumProperties.INITIAL_STIFFNESS, 60000)

soil2.setName("Massive Rock")
soil2.setUnitWeight(26)
soil2.LateralProperties.setLateralType(LateralType.MASSIVE_ROCK)
bedrock_props = soil2.LateralProperties.MassiveRock

bedrock_props.setUniaxialCompressiveStrength(150000)
bedrock_props.setGeologicalStrengthIndex(75)
bedrock_props.setIntactRockConstant(12)
bedrock_props.setModulusType(ModulusType.USE_INTACT_ROCK_MODULUS)
bedrock_props.setIntactRockModulus(22000000)
bedrock_props.setPoissonRatio(0.35)

print(soil1.getName())
print(soil1.getUnitWeight())
print(soil1.LateralProperties.getLateralType())
print(soil1.LateralProperties.Silt.getCohesion())
print(soil1.LateralProperties.Silt.getFrictionAngle())
print(soil1.LateralProperties.Silt.getInitialStiffness())
print(soil1.LateralProperties.Silt.Datum.getDatum(LateralSiltDatumProperties.COHESION))
print(soil1.LateralProperties.Silt.Datum.getDatum(LateralSiltDatumProperties.FRICTION_ANGLE))
print(soil1.LateralProperties.Silt.Datum.getDatum(LateralSiltDatumProperties.INITIAL_STIFFNESS))

print(soil2.getName())
print(soil2.getUnitWeight())
print(soil2.LateralProperties.getLateralType())
print(soil2.LateralProperties.MassiveRock.getUniaxialCompressiveStrength())
print(soil2.LateralProperties.MassiveRock.getGeologicalStrengthIndex())
print(soil2.LateralProperties.MassiveRock.getIntactRockConstant())
print(soil2.LateralProperties.MassiveRock.getModulusType())
print(soil2.LateralProperties.MassiveRock.getIntactRockModulus())
print(soil2.LateralProperties.MassiveRock.getPoissonRatio())

model.save()
model.close()

rspile_modeler.closeApplication()