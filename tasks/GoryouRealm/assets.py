from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GoryouRealmAssets: 


	# Click Rule Assets
	# description 
	C_GR_C_1 = RuleClick(roi_front=(95,105,224,548), roi_back=(95,105,224,548), name="gr_c_1")
	# description 
	C_GR_C_2 = RuleClick(roi_front=(382,109,229,536), roi_back=(382,109,229,536), name="gr_c_2")
	# description 
	C_GR_C_3 = RuleClick(roi_front=(669,112,232,539), roi_back=(669,112,232,539), name="gr_c_3")
	# description 
	C_GR_C_4 = RuleClick(roi_front=(961,108,225,538), roi_back=(961,108,225,538), name="gr_c_4")


	# Image Rule Assets
	# 点击挑战 
	I_GR_FIRE = RuleImage(roi_front=(1097,582,100,100), roi_back=(1097,582,100,100), threshold=0.8, method="Template matching", file="./tasks/GoryouRealm/gr/gr_gr_fire.png")
	# description 
	I_GR_LOCK = RuleImage(roi_front=(559,564,27,32), roi_back=(559,564,27,32), threshold=0.8, method="Template matching", file="./tasks/GoryouRealm/gr/gr_gr_lock.png")
	# description 
	I_GR_UNLOCK = RuleImage(roi_front=(556,562,26,33), roi_back=(556,562,26,33), threshold=0.8, method="Template matching", file="./tasks/GoryouRealm/gr/gr_gr_unlock.png")


	# Ocr Rule Assets
	# 多少张票 
	O_GR_TICKET = RuleOcr(roi=(934,21,84,41), area=(934,21,84,41), mode="Digit", method="Default", keyword="", name="gr_ticket")


