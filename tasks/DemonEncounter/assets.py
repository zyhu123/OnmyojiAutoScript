from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class DemonEncounterAssets: 


	# Click Rule Assets
	# description 
	C_DM_BOSS_CLICK = RuleClick(roi_front=(593,274,100,100), roi_back=(593,274,100,100), name="dm_boss_click")


	# Image Rule Assets
	# 地震鲇 
	I_BOSS_NAMAZU = RuleImage(roi_front=(589,294,100,100), roi_back=(589,294,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_namazu.png")
	# 蜃气楼 
	I_BOSS_SHINKIRO = RuleImage(roi_front=(587,279,100,100), roi_back=(587,279,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_shinkiro.png")
	# 荒骷髅 
	I_BOSS_ODOKURO = RuleImage(roi_front=(596,287,100,100), roi_back=(596,287,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_odokuro.png")
	# 胧车 
	I_BOSS_OBOROGURUMA = RuleImage(roi_front=(588,285,100,100), roi_back=(588,285,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_oboroguruma.png")
	# 土蜘蛛 
	I_BOSS_TSUCHIGUMO = RuleImage(roi_front=(603,294,100,66), roi_back=(603,294,100,66), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_tsuchigumo.png")
	# 歌姬 
	I_BOSS_SONGSTRESS = RuleImage(roi_front=(592,323,67,61), roi_back=(592,323,67,61), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_songstress.png")
	# 集结挑战 
	I_BOSS_FIRE = RuleImage(roi_front=(1062,549,100,100), roi_back=(1062,549,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_fire.png")
	# description 
	I_BOSS_CONFIRM = RuleImage(roi_front=(671,400,175,61), roi_back=(671,400,175,61), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_confirm.png")
	# 已选中 
	I_BOSS_SELECTED = RuleImage(roi_front=(543,339,37,41), roi_back=(543,339,37,41), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_selected.png")
	# 还没选中 
	I_BOSS_NO_SELECT = RuleImage(roi_front=(544,337,37,43), roi_back=(544,337,37,43), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_no_select.png")
	# 集结 
	I_BOSS_GATHER = RuleImage(roi_front=(801,589,100,100), roi_back=(801,589,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_gather.png")
	# 战斗胜利 
	I_BOSS_WIN = RuleImage(roi_front=(380,43,100,100), roi_back=(380,43,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_win.png")
	# 白色退出 
	I_BOSS_BACK_WHITE = RuleImage(roi_front=(16,12,39,40), roi_back=(16,12,39,40), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/boss/boss_boss_back_white.png")


	# Click Rule Assets
	# 从下开始数第一个 
	C_DE_1 = RuleClick(roi_front=(1211,478,61,58), roi_back=(1211,478,61,58), name="de_1")
	# 2 
	C_DE_2 = RuleClick(roi_front=(1196,409,55,56), roi_back=(1196,409,55,56), name="de_2")
	# 3 
	C_DE_3 = RuleClick(roi_front=(1225,344,53,55), roi_back=(1225,344,53,55), name="de_3")
	# 第四个 
	C_DE_4 = RuleClick(roi_front=(1200,282,56,53), roi_back=(1200,282,56,53), name="de_4")


	# Image Rule Assets
	# 红色达摩 
	I_DE_RED_DHARMA = RuleImage(roi_front=(1216,215,32,33), roi_back=(1209,208,51,50), threshold=0.7, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_red_dharma.png")
	# 点击右下角的寻找封魔 
	I_DE_FIND = RuleImage(roi_front=(1136,593,100,100), roi_back=(1136,593,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_find.png")
	# 点击首领 
	I_DE_BOSS = RuleImage(roi_front=(1001,645,45,45), roi_back=(1001,645,45,45), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_boss.png")
	# 点击封魔极 
	I_DE_BOSS_BEST = RuleImage(roi_front=(900,644,45,50), roi_back=(900,644,45,50), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_boss_best.png")
	# 式神录 
	I_DE_SHI_RECORDS = RuleImage(roi_front=(789,639,48,48), roi_back=(789,639,48,48), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_shi_records.png")
	# 左下角小指针 
	I_DE_LOCATION = RuleImage(roi_front=(26,653,44,47), roi_back=(26,653,44,47), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_location.png")


	# Image Rule Assets
	# 右侧的气球 
	I_DE_BALLOON = RuleImage(roi_front=(1214,295,28,27), roi_back=(1198,269,81,266), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_balloon.png")
	# 右侧的宝箱 
	I_DE_BOX = RuleImage(roi_front=(1210,295,34,33), roi_back=(1183,278,96,277), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_box.png")
	# 挑战某一个后的封印图片 
	I_DE_DEFEAT_2 = RuleImage(roi_front=(1211,422,28,35), roi_back=(1211,422,28,35), threshold=0.7, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_defeat_2.png")
	# description 
	I_DE_DEFEAT_1 = RuleImage(roi_front=(1223,489,42,41), roi_back=(1223,489,42,41), threshold=0.7, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_defeat_1.png")
	# description 
	I_DE_DEFEAT_3 = RuleImage(roi_front=(1231,358,38,35), roi_back=(1231,358,38,35), threshold=0.7, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_defeat_3.png")
	# description 
	I_DE_DEFEAT_4 = RuleImage(roi_front=(1215,295,35,35), roi_back=(1215,295,35,35), threshold=0.7, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_defeat_4.png")
	# 已领取四次的奖励 
	I_DE_AWARD = RuleImage(roi_front=(1216,214,42,36), roi_back=(1195,198,74,67), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_award.png")
	# 信 
	I_DE_LETTER = RuleImage(roi_front=(1236,358,33,35), roi_back=(1177,261,100,294), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_letter.png")
	# 关闭封魔密信 
	I_LETTER_CLOSE = RuleImage(roi_front=(851,43,45,45), roi_back=(851,43,45,45), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_letter_close.png")
	# 小鬼王的挑战 
	I_DE_SMALL_FIRE = RuleImage(roi_front=(1064,549,100,100), roi_back=(1064,549,100,100), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_small_fire.png")
	# 神秘任务 
	I_DE_MYSTERY = RuleImage(roi_front=(1216,296,27,29), roi_back=(1192,278,85,261), threshold=0.8, method="Template matching", file="./tasks/DemonEncounter/demon/demon_de_mystery.png")


	# Ocr Rule Assets
	# 计数已经开启多少的 
	O_DE_COUNTER = RuleOcr(roi=(1204,685,48,34), area=(1204,685,48,34), mode="DigitCounter", method="Default", keyword="", name="de_counter")


	# Click Rule Assets
	# description 
	C_ANSWER_1 = RuleClick(roi_front=(430,264,440,67), roi_back=(430,264,440,67), name="answer_1")
	# description 
	C_ANSWER_2 = RuleClick(roi_front=(428,351,438,70), roi_back=(428,351,438,70), name="answer_2")
	# description 
	C_ANSWER_3 = RuleClick(roi_front=(434,435,437,65), roi_back=(434,435,437,65), name="answer_3")


	# Ocr Rule Assets
	# 1/3 
	O_LETTER_COUNT = RuleOcr(roi=(480,133,55,34), area=(480,133,55,34), mode="DigitCounter", method="Default", keyword="", name="letter_count")
	# 问题 
	O_LETTER_QUESTION = RuleOcr(roi=(427,164,447,100), area=(427,164,447,100), mode="Single", method="Default", keyword="", name="letter_question")
	# 回答一 
	O_LETTER_ANSWER_1 = RuleOcr(roi=(424,261,450,74), area=(424,261,450,74), mode="Single", method="Default", keyword="", name="letter_answer_1")
	# 回答二 
	O_LETTER_ANSWER_2 = RuleOcr(roi=(428,350,438,74), area=(428,350,438,74), mode="Single", method="Default", keyword="", name="letter_answer_2")
	# 回答三 
	O_LETTER_ANSWER_3 = RuleOcr(roi=(428,439,443,72), area=(428,439,443,72), mode="Single", method="Default", keyword="", name="letter_answer_3")


