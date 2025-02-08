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
model = rspile_modeler.openFile(rf"{current_dir}\example_models\PrestressedConcreteSection.rspile2")

pile_section_list = model.getPileSections()

pile_section_1 = pile_section_list[0]

pile_section_1.setName("Prestressed Concrete Section")
pile_section_1.PileAnalysis.setSectionType(SectionType.PRESTRESSED_CONCRETE)
pile_section_1.PileAnalysis.PrestressedConcrete.setCompressiveStrength(150000)
pile_section_1.PileAnalysis.PrestressedConcrete.setCrossSectionType(PrestressedConcreteCrossSectionType.RECTANGULAR)
pile_section_1.PileAnalysis.PrestressedConcrete.CrossSection.Rectangular.setDepth(0.4)
pile_section_1.PileAnalysis.PrestressedConcrete.CrossSection.Rectangular.setWidth(0.4)

section_1_reinforcement = pile_section_1.PileAnalysis.PrestressedConcrete.CrossSection.ConcreteDesigner.Reinforcement
if len(section_1_reinforcement.getReinforcementPatterns()) == 0:
	section_1_reinforcement.addReinforcementPattern("Custom Reinforcement")

reinforcement_pattern_1 = section_1_reinforcement.getReinforcementPatterns()[0]
reinforcement_pattern_1.setName("Custom Pattern")
reinforcement_pattern_1.setStrandType(StrandType.GRADE_270_KSI_LOLAX)
reinforcement_pattern_1.setStrandSize(StrandSize.SIZE_270_3_8_7_WIRE)
reinforcement_pattern_1.setReinforcementPatternType(ReinforcementPatternType.RADIAL)
reinforcement_pattern_1.Radial.setNumberOfBars(9)
reinforcement_pattern_1.Radial.setAngleFromXAxis(15)
reinforcement_pattern_1.Radial.setRebarLocationRefPoint(RebarReferencePointMethod.COVER_DEPTH)
reinforcement_pattern_1.Radial.setCoverDepth(50)

print(pile_section_1.getName())
print(pile_section_1.PileAnalysis.getSectionType())
print(pile_section_1.PileAnalysis.PrestressedConcrete.getCompressiveStrength())
print(pile_section_1.PileAnalysis.PrestressedConcrete.getCrossSectionType())
print(pile_section_1.PileAnalysis.PrestressedConcrete.CrossSection.Rectangular.getDepth())
print(pile_section_1.PileAnalysis.PrestressedConcrete.CrossSection.Rectangular.getWidth())

print(reinforcement_pattern_1.getName())
print(reinforcement_pattern_1.getStrandType())
print(reinforcement_pattern_1.getStrandSize())
print(reinforcement_pattern_1.getReinforcementPatternType())
print(reinforcement_pattern_1.Radial.getNumberOfBars())
print(reinforcement_pattern_1.Radial.getAngleFromXAxis())
print(reinforcement_pattern_1.Radial.getRebarLocationRefPoint())
print(reinforcement_pattern_1.Radial.getCoverDepth())

model.save()
model.close()

rspile_modeler.closeApplication()