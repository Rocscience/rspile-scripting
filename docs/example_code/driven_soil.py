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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\DrivenPile.rspile2")

soil_property_list = model.getSoilProperties()

soil1 = soil_property_list[0]
soil2 = soil_property_list[1]

soil1.setName("Gravelly Sand")
soil1.setUnitWeight(20.5)
soil1.DrivenProperties.setDrivenSoilType(DrivenType.COHESIONLESS)
soil1.DrivenProperties.setDrivingStrengthLoss(25)
soil1.DrivenProperties.Cohesionless.setInternalFrictionAngleSkinFrictionMethod(InternalFrictionAngleMethod.USE_FRICTION_ANGLE)
soil1.DrivenProperties.Cohesionless.setSkinFrictionAngle(35)
soil1.DrivenProperties.Cohesionless.setInternalFrictionAngleEndBearingMethod(InternalFrictionAngleMethod.USE_SPT_N_VALUES)
soil1.DrivenProperties.Cohesionless.EndBearingSPTTable.setSPTTable([(0, 9),(0.8,15),(1.5,15),(3.0,32),(4.6, 45),(6.1, 100),(12, 100)])

soil2.setName("Clayey Silt")
soil2.setUnitWeight(19.3)
soil2.DrivenProperties.setDrivenSoilType(DrivenType.COHESIVE)
soil2.DrivenProperties.setDrivingStrengthLoss(22)
soil2.DrivenProperties.Cohesive.setUndrainedShearStrength(120)
soil2.DrivenProperties.Cohesive.setAdhesionType(AdhesionType.OVERLYING_SANDS)

print(soil1.getName())
print(soil1.getUnitWeight())
print(soil1.DrivenProperties.getDrivenSoilType())
print(soil1.DrivenProperties.getDrivingStrengthLoss())
print(soil1.DrivenProperties.Cohesionless.getInternalFrictionAngleSkinFrictionMethod())
print(soil1.DrivenProperties.Cohesionless.getSkinFrictionAngle())
print(soil1.DrivenProperties.Cohesionless.getInternalFrictionAngleEndBearingMethod())
print(soil1.DrivenProperties.Cohesionless.EndBearingSPTTable.getSPTTable())

print(soil2.getName())
print(soil2.getUnitWeight())
print(soil2.DrivenProperties.getDrivenSoilType())
print(soil2.DrivenProperties.getDrivingStrengthLoss())
print(soil2.DrivenProperties.Cohesive.getUndrainedShearStrength())
print(soil2.DrivenProperties.Cohesive.getAdhesionType())

model.save()
model.close()

rspile_modeler.closeApplication()