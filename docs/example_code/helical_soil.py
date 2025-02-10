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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\HelicalPile.rspile2")

soil_property_list = model.getSoilProperties()

soil1 = soil_property_list[0]
soil2 = soil_property_list[1]

soil1.setName("Sand (Fill)")
soil1.setUnitWeight(21)
soil1.HelicalProperties.setHelicalSoilType(HelicalType.COHESIONLESS)
soil1.HelicalProperties.Cohesionless.setInternalFrictionAngle(28)
soil1.HelicalProperties.Cohesionless.setFrictionAngleBetweenShaftAndSoil(20)
soil1.HelicalProperties.Cohesionless.setCoefficientOfLateralEarthPressureForShaft(1)

soil2.setName("Silty Clay")
soil2.setUnitWeight(19)
soil2.HelicalProperties.setHelicalSoilType(HelicalType.COHESIVE)
soil2.HelicalProperties.Cohesive.setUndrainedShearStrength(72)
soil2.HelicalProperties.Cohesive.setNcPrime(8)
soil2.HelicalProperties.Cohesive.setAdhesionFactorForShaft(1)


print(soil1.getName())
print(soil1.getUnitWeight())
print(soil1.HelicalProperties.getHelicalSoilType())
print(soil1.HelicalProperties.Cohesionless.getInternalFrictionAngle())
print(soil1.HelicalProperties.Cohesionless.getFrictionAngleBetweenShaftAndSoil())
print(soil1.HelicalProperties.Cohesionless.getCoefficientOfLateralEarthPressureForShaft())

print(soil2.getName())
print(soil2.getUnitWeight())
print(soil2.HelicalProperties.getHelicalSoilType())
print(soil2.HelicalProperties.Cohesive.getUndrainedShearStrength())
print(soil2.HelicalProperties.Cohesive.getNcPrime())
print(soil2.HelicalProperties.Cohesive.getAdhesionFactorForShaft())

model.save()
model.close()

rspile_modeler.closeApplication()