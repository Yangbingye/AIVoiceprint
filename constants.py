# coding=utf-8

DATASET_DIR = 'audio/LibriSpeechSamples/npy/'
TEST_DIR = 'audio/LibriSpeechSamples/npy/'
WAV_DIR = 'audio/LibriSpeechSamples/wav/'
KALDI_DIR = ''
GUESS_DIR = 'guess/npy/'

BATCH_SIZE = 16        #must be even
TRIPLET_PER_BATCH = 3

SAVE_PER_EPOCHS = 200
TEST_PER_EPOCHS = 200
CANDIDATES_PER_BATCH = 640       # 18s per batch
TEST_NEGATIVE_No = 99


NUM_FRAMES = 160   # 299 - 16*2
SAMPLE_RATE = 16000
TRUNCATE_SOUND_SECONDS = (0.2, 1.81)  # (start_sec, end_sec)
ALPHA = 0.2
HIST_TABLE_SIZE = 10
NUM_SPEAKERS = 143
DATA_STACK_SIZE = 10

CHECKPOINT_FOLDER = 'checkpoints'
BEST_CHECKPOINT_FOLDER = 'best_checkpoint'
PRE_CHECKPOINT_FOLDER = 'pretraining_checkpoints'
GRU_CHECKPOINT_FOLDER = 'gru_checkpoints'

LOSS_LOG= CHECKPOINT_FOLDER + '/losses.txt'
TEST_LOG= CHECKPOINT_FOLDER + '/acc_eer.txt'

PRE_TRAIN = True

COMBINE_MODEL = True

DICT = {0: '暗裔剑魔·亚托克斯', 1: '九尾妖狐·阿狸', 2: '离群之刺·阿卡丽', 3: '牛头酋长·阿利斯塔', 4: '殇之木乃伊·阿木木', 5: '冰晶凤凰·艾尼维亚', 6: '黑暗之女·安妮', 7: '寒冰射手·艾希', 8: '铸星龙王·奥瑞利安·索尔', 9: '沙漠皇帝·阿兹尔', 10: '星界游神·巴德', 11: '蒸汽机器人·布里茨', 12: '复仇焰魂·布兰德', 13: '弗雷尔卓德之心·布隆', 14: '皮城女警·凯特琳', 15: '青钢影·卡蜜尔', 16: '魔蛇之拥·卡西奥佩娅', 17: '虚空恐惧·科加斯', 18: '英勇投弹手·库奇', 19: '诺克萨斯之手·德莱厄斯', 20: '皎月女神·黛安娜', 21: '祖安狂人·蒙多医生', 22: '荣耀行刑官·德莱文', 23: '时间刺客·艾克', 24: '蜘蛛女皇·伊莉丝', 25: '痛苦之拥·伊芙琳', 26: '探险家·伊泽瑞尔', 27: '末日使者·费德提克', 28: '无双剑姬·菲奥娜', 29: '潮汐海灵·菲兹', 30: '正义巨像·加里奥', 31: '海洋之灾·普朗克', 32: '德玛西亚之力·盖伦', 33: '迷失之牙·纳尔', 34: '酒桶·古拉加斯', 35: '法外狂徒·格雷福斯', 36: '战争之影·赫卡里姆', 37: '大发明家·黑默丁格', 38: '海兽祭司·俄洛伊', 39: '刀锋舞者·艾瑞莉娅', 40: '翠神·艾翁', 41: '风暴之怒·迦娜', 42: '德玛西亚皇子·嘉文四世', 43: '武器大师·贾克斯', 44: '未来守护者·杰斯', 45: '戏命师·烬', 46: '暴走萝莉·金克斯', 47: '虚空之女·卡莎', 48: '复仇之矛·卡莉丝塔', 49: '天启者·卡尔玛', 50: '死亡颂唱者·卡尔萨斯', 51: '虚空行者·卡萨丁', 52: '不详之刃·卡特琳娜', 53: '正义天使·凯尔', 54: '影流之镰·凯隐', 55: '狂暴之心·凯南', 56: '虚空掠夺者·卡兹克', 57: '永猎双子·千珏', 58: '暴怒骑士·克烈', 59: '深渊巨口·克格莫', 60: '诡术妖姬·乐芙兰', 61: '盲僧·李青', 62: '曙光女神·蕾欧娜', 63: '冰霜女巫·丽桑卓', 64: '圣枪游侠·卢锡安', 65: '仙灵女巫·璐璐', 66: '光辉女郎·拉克丝', 67: '熔岩巨兽·墨菲特', 68: '虚空先知·玛尔扎哈', 69: '扭曲树精·茂凯', 70: '无极剑圣·易', 71: '赏金猎人·厄运小姐', 72: '齐天大圣·孙悟空', 73: '铁铠冥魂·莫德凯撒', 74: '堕落天使·莫甘娜', 75: '唤潮鲛姬·娜美', 76: '沙漠死神·内瑟斯', 77: '深海泰坦·诺提勒斯', 78: '万花通灵·妮蔻', 79: '狂野女猎手·奈德丽', 80: '雪原双子·努努和威朗普', 81: '狂战士·奥拉夫', 82: '发条魔灵·奥莉安娜', 83: '山隐之焰·奥恩', 84: '战争之王·潘森', 85: '圣锤之毅·波比', 86: '血港鬼影·派克', 87: '德玛西亚之翼·奎因', 88: '幻翎·洛', 89: '披甲龙龟·拉莫斯', 90: '虚空遁地兽·雷克塞', 91: '荒漠屠夫·雷克顿', 92: '傲之追猎者·雷恩加尔', 93: '放逐之刃·锐雯', 94: '机械公敌·兰博', 95: '符文法师·瑞兹', 96: '北地之怒·瑟庄妮', 97: '恶魔小丑·萨科', 98: '暮光之眼·慎', 99: '龙血武姬·希瓦娜', 100: '炼金术士·辛吉德', 101: '亡灵战神·赛恩', 102: '战争女神·希维尔', 103: '水晶先锋·斯卡纳', 104: '琴瑟仙女·娑娜', 105: '众星之子·索拉卡', 106: '诺克萨斯统领·斯维因', 107: '解脱者·塞拉斯', 108: '暗黑元首·辛德拉', 109: '河流之王·塔姆', 110: '岩雀·塔莉娅', 111: '刀锋之影·泰隆', 112: '瓦罗兰之盾·塔里克', 113: '迅捷斥候·提莫', 114: '魂锁典狱长·锤石', 115: '麦林炮手·崔丝塔娜', 116: '巨魔之王·特朗德尔', 117: '蛮族之王·泰达米尔', 118: '卡牌大师·崔斯特	', 119: '瘟疫之源·图奇', 120: '兽灵行者·乌迪尔', 121: '无畏战车·厄加特', 122: '惩戒之箭·韦鲁斯', 123: '暗夜猎手·薇恩', 124: '邪恶小法师·维迦', 125: '虚空之眼·维克兹', 126: '皮城执法官·蔚', 127: '机械先驱·维克托', 128: '猩红收割者·弗拉基米尔', 129: '雷霆咆哮·沃利贝尔', 130: '祖安巨兽·沃里克', 131: '逆羽·霞', 132: '远古巫灵·泽拉斯', 133: '德邦总管·赵信', 134: '疾风剑豪·亚索', 135: '牧魂人·约里克', 136: '生化魔人·扎克', 137: '影流之主·劫', 138: '爆破鬼才·吉格斯', 139: '时光守护者·基兰', 140: '暮光星灵·佐伊', 141: '荆棘之兴·婕拉'}

