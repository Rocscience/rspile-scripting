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

pile_section_list = model.getPileTypes()

pile_type1 = pile_section_list[0]
pile_type2 = pile_section_list[1]

pile_type1.setName("Pile Type A806")
pile_type1.setColor(ColorPicker.Indigo)
pile_type1.PileAnalysis.Sections.setCrossSectionType(PileAnalysisPileTypeCrossSection.UNIFORM)
pile_type1.PileAnalysis.Sections.setPileSegmentsByLength(1, [["Reinforced Concrete Section", 15]])

pile_type1.PileAnalysis.Orientation.setRotationAngle(5)
pile_type1.PileAnalysis.Orientation.setOrientationType(OrientationType.ALPHA_BETA)
pile_type1.PileAnalysis.Orientation.AlphaBeta.setAlphaAngle(30)
pile_type1.PileAnalysis.Orientation.AlphaBeta.setBetaAngle(80)	

pile_type2.setName("Pile Type C094")
pile_type2.setColor(ColorPicker.Light_Grey)
pile_type2.PileAnalysis.Sections.setCrossSectionType(PileAnalysisPileTypeCrossSection.TAPERED)
pile_type2.PileAnalysis.Sections.setTaperAngle(0.3)
pile_type2.PileAnalysis.Sections.setPileSegmentsByBottomElevation(2, [["Reinforced Concrete Section", -5], ["Circular Concrete Section", -10]])
pile_type2.PileAnalysis.Orientation.setRotationAngle(0)
pile_type2.PileAnalysis.Orientation.setOrientationType(OrientationType.VECTOR)
pile_type2.PileAnalysis.Orientation.Vector.setVector([1, 1, -1])

print(pile_type1.getName())
print(ColorPicker.getColorName(pile_type1.getColor()))
print(pile_type1.PileAnalysis.Sections.getCrossSectionType())
print(pile_type1.PileAnalysis.Sections.getPileSegmentsByLength())
print(pile_type1.PileAnalysis.Orientation.getRotationAngle())
print(pile_type1.PileAnalysis.Orientation.getOrientationType())
print(pile_type1.PileAnalysis.Orientation.AlphaBeta.getAlphaAngle())
print(pile_type1.PileAnalysis.Orientation.AlphaBeta.getBetaAngle())

print(pile_type2.getName())
print(ColorPicker.getColorName(pile_type2.getColor()))
print(pile_type2.PileAnalysis.Sections.getCrossSectionType())
print(pile_type2.PileAnalysis.Sections.getTaperAngle())
print(pile_type2.PileAnalysis.Sections.getPileSegmentsByBottomElevation())
print(pile_type2.PileAnalysis.Orientation.getRotationAngle())
print(pile_type2.PileAnalysis.Orientation.getOrientationType())
print(pile_type2.PileAnalysis.Orientation.Vector.getVector())

model.save()
model.close()

rspile_modeler.closeApplication()