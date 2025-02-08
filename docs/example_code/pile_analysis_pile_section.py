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

pile_section_list = model.getPileSections()

pile_section1 = pile_section_list[0]
pile_section2 = pile_section_list[1]

pile_section1.setName("Reinforced Concrete Section")
pile_section1.setColor(ColorPicker.Indigo)
pile_section1.PileAnalysis.setSectionType(SectionType.REINFORCED_CONCRETE)
pile_section1.PileAnalysis.ReinforcedConcrete.setCompressiveStrength(150000)
pile_section1.PileAnalysis.ReinforcedConcrete.setCrossSectionType(ReinforcedConcreteCrossSectionType.RECTANGULAR)
pile_section1.PileAnalysis.ReinforcedConcrete.CrossSection.Rectangular.setDepth(0.4)
pile_section1.PileAnalysis.ReinforcedConcrete.CrossSection.Rectangular.setWidth(0.4)

pile_section_1_ibeam_property = pile_section1.PileAnalysis.ReinforcedConcrete.CrossSection.ConcreteDesigner.IBeam
pile_section_1_ibeam_property.setUseIBeam(True)
pile_section_1_ibeam_property.setIBeamType(CanadianIBeamTypes.HP310X110)
pile_section_1_ibeam_property.setYieldStress(450000)
pile_section_1_ibeam_property.setElasticModulus(200000)

pile_section2.setName("Circular Concrete Section")
pile_section2.setColor(ColorPicker.Pale_Turquoise)
pile_section2.PileAnalysis.setSectionType(SectionType.ELASTIC)
pile_section2.PileAnalysis.Elastic.setYoungsModulus(30000)
pile_section2.PileAnalysis.Elastic.setCrossSectionType(ElasticCrossSectionType.CIRCULAR)
pile_section2.PileAnalysis.Elastic.CrossSection.Circular.setDiameter(1.5)

print(pile_section1.getName)
print(ColorPicker.getColorName(pile_section1.getColor()))
print(pile_section1.PileAnalysis.getSectionType())
print(pile_section1.PileAnalysis.ReinforcedConcrete.getCompressiveStrength())
print(pile_section1.PileAnalysis.ReinforcedConcrete.getCrossSectionType())
print(pile_section1.PileAnalysis.ReinforcedConcrete.CrossSection.Rectangular.getDepth())
print(pile_section1.PileAnalysis.ReinforcedConcrete.CrossSection.Rectangular.getWidth())

print(pile_section_1_ibeam_property.getUseIBeam())
print(pile_section_1_ibeam_property.getIBeamType())
print(pile_section_1_ibeam_property.getYieldStress())
print(pile_section_1_ibeam_property.getElasticModulus())

print(pile_section2.getName)
print(ColorPicker.getColorName(pile_section2.getColor()))
print(pile_section2.PileAnalysis.getSectionType())
print(pile_section2.PileAnalysis.Elastic.getYoungsModulus())
print(pile_section2.PileAnalysis.Elastic.getCrossSectionType())
print(pile_section2.PileAnalysis.Elastic.CrossSection.Circular.getDiameter())

model.save()
model.close()

rspile_modeler.closeApplication()