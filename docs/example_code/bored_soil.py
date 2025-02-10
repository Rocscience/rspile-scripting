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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\BoredPile.rspile2")

soil_property_list = model.getSoilProperties()

soil1 = soil_property_list[0]
soil2 = soil_property_list[1]

soil1.setName("Sandy Clayey Silt (Till)")
soil1.setUnitWeight(21)
soil1.BoredProperties.setBoredSoilType(BoredType.COHESIVE)
soil1.BoredProperties.setUseReductionFactors(True)
soil1.BoredProperties.setSkinResistanceLoss(15)
soil1.BoredProperties.setEndBearingLoss(10)
soil1.BoredProperties.Cohesive.setCohesiveMethod(CohesiveMethod.TOTAL_STRESS)
soil1.BoredProperties.Cohesive.TotalStress.setAlpha(0.7)
soil1.BoredProperties.Cohesive.TotalStress.setUndrainedShearStrength(100)
soil1.BoredProperties.Cohesive.TotalStress.setBearingCapacityFactorNc(8)
soil1.BoredProperties.Cohesive.TotalStress.setSkinFrictionLimit(15000)
soil1.BoredProperties.Cohesive.TotalStress.setEndBearingLimit(150000)

soil2.setName("Shale Bedrock")
soil2.setUnitWeight(24.1)
soil2.BoredProperties.setBoredSoilType(BoredType.WEAK_ROCK)
soil2.BoredProperties.setUseReductionFactors(False)
soil2.BoredProperties.WeakRock.setUnconfinedCompressiveStrength(6000)
soil2.BoredProperties.WeakRock.setSkinFrictionLimit(15000)
soil2.BoredProperties.WeakRock.setEndBearingLimit(150000)
soil2.BoredProperties.WeakRock.SkinResistance.setSkinResistanceMethod(SkinResistanceMethod.KULHAWY_PHOON)
soil2.BoredProperties.WeakRock.SkinResistance.KulhawyAndPhoon.setChi(2.5)
soil2.BoredProperties.WeakRock.TipResistance.setTipResistanceMethod(TipResistanceMethod.TOMLINSON_WOODWARD)
soil2.BoredProperties.WeakRock.TipResistance.TomlinsonAndWoodward.setInternalFrictionAngle(30)

print(soil1.getName())
print(soil1.getUnitWeight())
print(soil1.BoredProperties.getBoredSoilType())
print(soil1.BoredProperties.getUseReductionFactors())
print(soil1.BoredProperties.getSkinResistanceLoss())
print(soil1.BoredProperties.getEndBearingLoss())
print(soil1.BoredProperties.Cohesive.getCohesiveMethod())
print(soil1.BoredProperties.Cohesive.TotalStress.getAlpha())
print(soil1.BoredProperties.Cohesive.TotalStress.getUndrainedShearStrength())
print(soil1.BoredProperties.Cohesive.TotalStress.getBearingCapacityFactorNc())
print(soil1.BoredProperties.Cohesive.TotalStress.getSkinFrictionLimit())
print(soil1.BoredProperties.Cohesive.TotalStress.getEndBearingLimit())

print(soil2.getName())
print(soil2.getUnitWeight())
print(soil2.BoredProperties.getBoredSoilType())
print(soil2.BoredProperties.getUseReductionFactors())
print(soil2.BoredProperties.WeakRock.getUnconfinedCompressiveStrength())
print(soil2.BoredProperties.WeakRock.getSkinFrictionLimit())
print(soil2.BoredProperties.WeakRock.getEndBearingLimit())
print(soil2.BoredProperties.WeakRock.SkinResistance.getSkinResistanceMethod())
print(soil2.BoredProperties.WeakRock.SkinResistance.KulhawyAndPhoon.getChi())
print(soil2.BoredProperties.WeakRock.TipResistance.getTipResistanceMethod())
print(soil2.BoredProperties.WeakRock.TipResistance.TomlinsonAndWoodward.getInternalFrictionAngle())

model.save()
model.close()

rspile_modeler.closeApplication()