# -*-coding: utf-8 -*-
# import pymysql
#
# conn = pymysql.connect(host="localhost", user="root", password="root", database="spider", charset="utf8")
# cursor = conn.cursor()
#
# table_list = ['busizhiyu123_fans', 'busizhiyu123_follow', 'flyandrun_fans', 'flyandrun_follow', 'four4leaves_fans', 'four4leaves_follow', 'fxh1057441307_fans', 'fxh1057441307_follow', 'haomin994_fans', 'hyc1079518944_fans', 'hyc1079518944_follow', 'liuxingjie1235_fans', 'liuxingjie1235_follow', 'shaojingjing1687_fans', 'shaojingjing1687_follow', 'shouji132230567090_fans', 'shouji132230567090_follow', 'syw143_fans', 'syw143_follow', 'w761758249_fans', 'w761758249_follow', 'w924989836_fans', 'w924989836_follow', 'weishizhua3068_fans', 'weishizhua3068_follow', 'xiexing78951236_fans', 'xiexing78951236_follow', 'xwb374215559_fans', 'xwb374215559_follow']
#
#
# sum = []
#
# for index,name in enumerate(table_list):
#
#     sql = '''
#     select name from {}
#     '''.format(name)
#     cursor.execute(sql)
#     d = cursor.fetchall()
#     for item in d:
#         sum.append(item[0])





# from collections import Counter
# import time
#
# print(sum)
# print(len(sum))
#
# result = Counter(sum)
# print(result)
# print(len(result))


result = {'wyw': 22, '跟不上': 22, '刘星杰': 20, '-----筱悠': 20, '魏': 19, '非凡': 18, '追风少年Wq': 18, '李志国': 18, '薛进财': 18, '邵晶晶': 17, '天爱LOVE': 17, '陈晓': 17, 'Ps暗夜精灵': 16, 'hanjingjing': 16, '景承萱': 16, '刘宛蓉': 16, '冯兴浩': 15, '谢星': 15, 'LUO4444': 14, '刘克楠': 14, '冷残影': 13, '财哥': 13, '槐米': 13, '于建恒': 13, '兽兽姐': 12, '郁义': 12, '陈乐': 12, '张憬': 12, '王辉': 12, '尚永旺': 12, '时光吹老了少年的梦': 12, '暗香': 11, '邓克繁': 11, '刘寰清': 11, '王飚': 11, '扬': 11, '刘昊民': 11, '陈科东': 11, '泛滥小青年': 11, '天上掉下来的小傻瓜': 11, '受伤后的坚强': 10, '陶维东': 10, '孙靖': 10, '王玉娇': 10, '赵帅奇': 9, 'kaikei': 9, '宋颖颖': 9, '曹璐': 9, '简爱ing': 9, '石祯珍': 9, '微博精灵': 9, '-璇子': 9, 'Monica': 9, 'XWB': 9, '张天福': 9, '李文瑞': 8, '思念': 8, '任学舜': 8, '刘兴武': 8, '吴映利': 8, '李艳绒': 8, '茄子': 8, '杨新宇': 8, '杨勇': 8, '张晓雪': 8, '心月': 8, '哑缺': 8, '凯凯': 8, '释': 8, '路小雪': 8, '张力': 8, '高国强': 7, '潘玉': 7, '死掉发动': 7, '笨': 7, '贺富鹏': 7, '亁道夫': 7, '含泪的微笑': 7, '魏哲': 7, '莫言': 7, '宋鹏': 7, '放肆': 7, '昊昊': 7, '王世琪': 7, '苏墨白': 7, '7': 7, '虎志信': 7, '张文瑞': 7, '高': 7, '蓝枫': 7, '苏晋安': 7, '差等生L': 7, '奋斗': 7, '扯不清的暧昧': 6, '王萌': 6, '相言': 6, '晴': 6, '郭懿': 6, '月神夜': 6, '沈仪': 6, '张有鹏': 6, '刘文凯': 6, '董昊': 6, '自怨自艾': 6, '紫金零': 6, 'NewDivide': 6, '阳光': 6, '丶小新没蜡笔': 6, 'Candy未待续': 6, '爱吃小布丁': 6, 'Sun': 6, '白瑞': 6, '李航': 6, '付磊': 6, '韦应鹏': 6, '周晓': 6, '玮': 6, '007': 6, '李欣': 6, '赵彤祝华晨宇生日快乐': 6, '夏钰翔': 6, '张春苗': 6, 'love劼儿宝贝': 6, '繁华落幕丶写不完的温柔': 6, '张振平': 6, '徐志淑': 6, '雷双瑜': 6, '田精忠': 6, '魏文菁': 6, '鳞': 6, '裴艳文': 6, '侯雨轩': 6, '谈继魁': 6, '关文武': 6, '康熙后裔': 5, '小晓清': 5, '吴斌': 5, 'CoColovec': 5, '守望那片天': 5, '姜思劼': 5, '王稷尧': 5, '芃芃': 5, '花瞳迷离': 5, '君子乾乾': 5, '舒皖清': 5, 'zqj': 5, '丁宝': 5, '贾玉涵': 5, '猫猫': 5, '蹲街-式寂寞': 5, '杨哲': 5, '夕亦残潋若丶': 5, '金小玉': 5, '刘翔': 5, '胡福东': 5, '小不着调的vR3': 5, '崔敬文': 5, '包捷': 5, '834394774': 5, '小磊': 5, '阳日直狮': 5, '徐明明': 5, '张东莉': 5, '王桉': 5, '刘志炜': 5, '夏洛': 5, '阳阳': 5, '黄耀娥': 5, '李强': 5, '谁是人间未归客': 5, '李朔': 5, '张程程': 5, 'kkkk': 5, '王诗奇': 5, '王鹏程': 5, '方朕文婧': 5, '末上光': 5, '流水简单': 5, '强': 5, '李世强': 5, '帆帆': 5, '张程飞': 5, '陌北城': 5, '张天宇': 5, 'StarKids': 4, '石云太': 4, '王立': 4, '冯昱才': 4, '袁鹏涛': 4, '徐鹏': 4, '黄玉琛': 4, '浮若年华': 4, '李波': 4, '张奋德': 4, '戴菲菲': 4, '古傲狂生': 4, '白箐儿': 4, '樱花上的蝶': 4, '丁慧': 4, '张宇伟': 4, '司航': 4, '胡富珺': 4, '陈天丁': 4, '涛涛': 4, '谢娜': 4, 'QQ音乐': 4, '听说我们不曾落泪': 4, 'momoG': 4, 'BiNsMaRt': 4, '1-2-3': 4, '薛巍巍': 4, '去无的止境': 4, '甘璐': 4, '王兴斌': 4, '她比烟花寂寞': 4, '艹尼玛': 4, '劉先森': 4, '鬼鬼': 4, '刘国民': 4, '张俊楠': 4, '-果果-': 4, '高菲': 4, '累可以不爱': 4, '张国鑫': 4, '嫣': 4, '王明威': 4, '张杰': 4, '邵芮': 4, '武双': 4, '南宫破域': 4, '申婉儒': 4, '找不到合适的伞我宁可淋雨': 4, '王嘉路': 4, '李客': 4, '李凯': 4, '王陆虎': 4, '13-水工八班王天健': 4, '装逼有罪': 4, '刘玮': 4, 'rxd': 4, '马耀乾': 4, '如果不曾遇见你': 4, '赵': 4, '方丈': 4, '123456qwe': 4, '岳潇煜': 4, '一粒砂': 4, '王菲': 4, '祁君彦': 4, '苏珊Zhangyuron': 4, '抱抱': 4, '张裕沁': 4, '李诗豪': 4, '肖涛涛': 4, 'MENG浩': 4, '逍遥': 4, '贺国琪': 4, '陈洁': 4, '盼': 4, 'kiss': 4, '李睿豪': 4, '焦婉滢': 4, '宋娜': 4, '李映辉': 4, 'Gentle-X': 4, '陈凯': 4, '段樱玲': 4, 'feel厮守': 4, '安小白BZJ': 4, '李珍': 4, '帝国': 4, '王振': 4, '如果深情是死罪我愿意': 4, '丁丁': 4, '梦': 3, '晓蕊': 3, '李娇': 3, 'CC': 3, '非凡业务': 3, '乱-': 3, 't': 3, '陈博': 3, '盒饭': 3, '但露灏': 3, '苏苏': 3, '吕国玲': 3, '小袁yjy': 3, '李源': 3, '徐志刚': 3, '于博文': 3, '蔡康永': 3, '王哲': 3, '何炅': 3, '史璐': 3, '郭敬明': 3, '赵可珂': 3, '郝雪': 3, '蒲旭光': 3, '李雅琦': 3, '哲哲': 3, '秦时月': 3, '王立群': 3, '心尘': 3, '陈相如': 3, '简': 3, '雅': 3, '雷朝杰': 3, '琪': 3, '苏婕': 3, '秦瑶瑶': 3, '胖大海': 3, '赵凌霄': 3, '卢凯': 3, '糖糖': 3, '李阳': 3, '刘定国': 3, '懂得多了--快乐就少了': 3, '旅途中的棺材': 3, '瑞瑞': 3, '冯敏': 3, '高科珍': 3, '柯芳': 3, '李娜': 3, '弑': 3, '骚情人': 3, '赵通通': 3, '张玉荣': 3, '迁徙': 3, '赵晓艳': 3, '马得俊': 3, '太多': 3, '王鸿鈺': 3, '口水宝宝': 3, '王燕': 3, '张雅': 3, '慕容紫英': 3, '我的左手边是你的右手': 3, '榕子': 3, '贝坚强': 3, '少女': 3, '高明庆桑': 3, 'Royal_皇朝丿月落': 3, 'canbb': 3, '张涵之': 3, '曾天博': 3, '白少': 3, '王璇': 3, '落落': 3, '刘国锋': 3, '杨淑琴': 3, '叶子': 3, '守望你-永远的-萌宠': 3, '瀻卩': 3, '高海澎': 3, '马耀远': 3, 'tialian': 3, '王宏生': 3, '郭洁': 3, '誓言不过是一时的快乐': 3, '涛': 3, '安分守己': 3, '相信我': 3, 'bbbbb': 3, '文美玲': 3, 'leo': 3, '高文扬': 3, '兰儿': 3, '武伟': 3, '张泰莉': 3, '田甜': 3, '林丹': 3, '顾改改': 3, '邢富林': 3, 'zhaoleilei': 3, '周生军': 3, '张仲源': 3, 'To_The_Old': 3, '疯子': 3, '我就是我': 3, '张兆才': 3, 'MJ': 3, '云': 3, '张天文': 3, '陈家小子说他很专情': 3, '王兴媛': 3, '李志威': 3, '路国中': 3, '蔡振科': 3, '好孩子': 3, '少年残像': 3, '靳昕': 3, '李文洁': 3, '赤那张宝元': 3, '王昭荣': 3, '王斌斌': 3, '听我听你': 3, '莫紫爱': 3, '南宫尛沫': 3, '柠七': 3, '逗比女神': 3, '高燕': 3, '牛燕': 3, '新颜': 3, '李曼': 3, '亮': 3, '乃宇璇': 3, '张镕晨': 3, '南国旧梦': 3, '张程俊': 3, '小石头': 3, '小清新': 3, '宋文前': 3, '陈霏': 3, '唐春莉': 3, '吕瑨': 3, '昕': 2, '王金娥': 2, '张晓斌': 2, '杜鹏立': 2, '李': 2, 'LeeGZ': 2, '金色童年': 2, '辉太狼': 2, 'JerryStark': 2, '高清宇': 2, '刘志远': 2, '牛彦翔': 2, '曾俊宁': 2, '流年湮没青春': 2, '各自安好': 2, '琳薇児': 2, '微笑流眼泪': 2, '臣臣': 2, '滕亚婕': 2, '小毛': 2, '安泽晨': 2, '张靖林': 2, '风中忆': 2, '殷庆龙': 2, '达拉丶': 2, 'wlln王': 2, '達籽': 2, '张韶涵': 2, '贾银凯': 2, '罗昕': 2, 'ella': 2, 'NBA2KOL': 2, '曹颖': 2, '姜敏': 2, '腾讯应用精选': 2, '张小美': 2, '妖人': 2, 'QQ旅游': 2, '爱妻爱家': 2, '张宇': 2, '彤彤': 2, '徐胖胖': 2, '刘芳舟': 2, '王明轩': 2, '小魚': 2, '花谢-草寂': 2, '郭跃': 2, 'QQ产品团队': 2, '房祖名': 2, '未央': 2, '腾讯微博应用频道': 2, '舒淇': 2, '卓文萱': 2, 'C罗': 2, '赵四米': 2, '杜岳滢': 2, '朱斌': 2, '朱晋': 2, '张晓琳': 2, '李连杰': 2, '腾讯游戏频道': 2, '段旭': 2, '高毅云': 2, '张扬': 2, '苏钰': 2, '语涵天禧': 2, '愿望': 2, '龙': 2, '王虎': 2, '杨杰': 2, '正鹏': 2, '孙湘毅': 2, '骗子': 2, 'Juice': 2, 'Cookie': 2, '韩洋': 2, '李小米': 2, '薛新健': 2, '聂子怡': 2, 'Dtwice7': 2, '何毛毛': 2, '冯兴业': 2, '王yu': 2, '李长蕊': 2, '一个二货的女人': 2, 'Royal_皇朝丿花心': 2, '裴乐': 2, '郝春虹': 2, '苏小小': 2, '何招靖': 2, '冯向才': 2, '瑞典包包': 2, '俊杰': 2, '牛进智': 2, '郝勇臣': 2, '张宇阳': 2, '魏万鑫': 2, '你是我坚持的半途而废': 2, '郝丽丽': 2, '安朵': 2, '达令': 2, '冯新旭': 2, '张心怡': 2, '小乞丐': 2, '狄明春': 2, '舞夜精灵之禁': 2, '假面': 2, 'wamsfa': 2, '曾经骚动不安只是因为年轻': 2, '曾晓玉': 2, 'tu': 2, '双翼助材影视传媒': 2, '展翅的雄鹰': 2, '欢欢': 2, '旗': 2, '李东岳': 2, '冯芯': 2, '酒暖回忆思念瘦': 2, '马婷婷': 2, '赵媛媛': 2, '哥是潮流的垫底': 2, '温浅': 2, '上善若水': 2, '东方不败': 2, '小白数码欢迎来电咨询': 2, '月光下的星星': 2, '上官烨雄': 2, '胡晓俊': 2, '晨曦吻过彩虹得脸': 2, '高丞相': 2, '隨遇而安': 2, '黄菡': 2, '淡如水': 2, '康辉': 2, '孫燕姿': 2, '杜靖峰': 2, '张璇': 2, '韩寒': 2, '嗨-我cao': 2, '谁心疼': 2, '李祯': 2, '李文': 2, '崔瀚文': 2, '路阳中': 2, '天无边': 2, '潍宸': 2, '奶嘴': 2, '秦天': 2, '李玉珍': 2, '范': 2, '李小宁': 2, '没有我的世界': 2, '丶安诺熙': 2, '李昊岩': 2, '余馨瑶': 2, '叶艳燕': 2, '丫头': 2, '何英彪': 2, '回忆': 2, '谁说自己的路一定孤独': 2, '杨静': 2, '王甜甜': 2, '永远有多远': 2, '陈涛': 2, '蓉': 2, '武卓': 2, '冷若萱': 2, '韩小娜': 2, '蕾丫': 2, '小七哥Kyrene': 2, '商小壮': 2, '钟楼怪人俞卡西': 2, '老树': 2, '绿色的夜': 2, '同一片天空之下': 2, '李龙': 2, '星星下的流年': 2, '阿伟': 2, '李嘉欣Michele': 2, '34': 2, 'Qiu': 2, '杨幂': 2, '奎': 2, '张春明': 2, '何永强': 2, '奇古拉': 2, '赵普': 2, '37': 2, '吴巧玲': 2, '王旭': 2, '代sir': 2, '刘一博': 2, '得不到的我宁愿不要': 2, '国庆': 2, '王天玲': 2, '岳生安': 2, '郭瑶': 2, '陈景雅': 2, '马亮': 2, 'tao': 2, '成砚雄': 2, '蒲为国': 2, 'hepeng5235': 2, '贺小龙': 2, '雪人': 2, '张永广': 2, '王亚东': 2, '展学琪': 2, '灰太狼': 2, '蕾': 2, '杨玉江': 2, '贾存强': 2, '张玲': 2, '小左': 2, '高永忠': 2, '熊熊': 2, 'xqgyl': 2, '小-叶-子-': 2, '小城恋口': 2, '田野': 2, '尚永新': 2, '乃正钢': 2, '刘兴旺': 2, '银魂': 2, '幽芷若兰': 2, '你过得快乐吗': 2, '周勇': 2, '傅婕': 2, 'lixiao': 2, '你承认我不承认': 2, '漠萤': 2, 'nuan': 2, '石祯元': 2, 'Curtain': 2, '冷色系孤独': 2, '展宗康': 2, '黎明将要来临': 2, '陈璐': 2, '杨金水': 2, '周爱': 2, '电脑管家': 2, 'H丶': 2, 'QQ农牧场': 2, '陈彦霖': 2, '啸': 2, '会': 2, '黑': 2, '傻瓜': 2, '李萌': 2, '冯家庆': 2, '雪': 2, '世界很大我是怪人': 2, '文': 2, '蛋': 2, '浮夸_': 2, '杨承': 2, '雅芸楠': 2, '昱': 2, '高振宇': 2, '小柿子': 2, '贱的彻底疯的蛋疼': 2, '张振玲': 2, '假寐-汪': 2, '吕其邦': 2, '12345': 2, '李智慧': 2, '刘永红': 2, '毛蛋儿': 2, '无所谓': 2, '辰疯': 2, '牛大春': 2, 'liugengone1': 2, 'TY': 2, '赵宏伟': 2, '冯林': 2, '杨洲': 2, '亚宏': 2, '破事别往心里搁': 2, 'Mr_徐': 2, '海英': 2, '陈锡美': 2, '守望的天空': 2, '刘心萍': 2, '缪海薇': 2, '董玉霞': 2, '陈玲': 2, '谢超': 2, '刘浩': 2, '柴朋振': 2, '孙晶': 2, '黄方瑞': 2, '谭广富': 2, '颜筱青': 2, '拾光': 2, '石下松': 2, '薇薇': 2, '王娜': 2, '是念旧是怀旧忆久亦旧': 2, '何国明': 2, '不再': 2, '白志翔': 2, '焦常顺': 2, '谢发轩': 2, '他她': 2, '邓亚莲': 2, '我姓欧': 2, '涛声依旧': 2, '潘光盛云': 2, 'WFX': 2, '彬彬': 2, '张学友': 2, '搞笑语录雷人平台': 2, '孟长安': 2, 'y-蓝雪': 2, '小鱼儿': 2, 'kennan': 2, '女孩露出你的知性美': 2, '艾先伦': 2, '梁明志': 2, '卢德彦': 2, '杨': 2, '小玲': 2, '郑洁': 2, '陈鹏解梦': 2, '张伟': 2, '丹丹': 2, '杨十妹': 2, '语诺': 2, '尚永玲': 2, '尚永琛': 2, '斯科拉Scola': 2, '杨威': 2, '平安崆峒': 2, '八一张博': 2, '流年萤火': 2, '王会': 2, '小蔷': 2, '陈跃文': 2, '波': 2, '--梦--de': 2, '愛Ni': 2, '丿小沫丶丨': 2, '丿Tuu丶小冷丨': 2, '贺亚顺': 2, '牛素花': 2, '王晓军': 2, '卢彬杰': 2, '恋上桃子的傻阿狸_': 2, '蝶舞': 2, '桂桂': 2, '利利': 2, '杨乐': 2, '杨振东': 2, '鲲先森不帅': 2, 'zofxrhzr': 2, '骚骚': 2, '孙斌': 2, '卫先森': 2, '宋天生': 2, '张玉婷': 2, 'bzj': 2, '平凡的平凡': 2, 'FT': 2, '二大爷': 2, '二爷': 2, 'mmmmmm花姑娘': 2, '吴晓飞': 2, '小执着': 2, '小丑': 2, '城影': 2, '张玲玲': 2, '魏家虎': 2, '尚立成': 2, '金小晓': 2, '陈志杰': 2, '老K': 2, '陈永婧': 2, '刘阳': 2, '占几分自私': 2, '罗常青': 2, '贺': 2, '卫延年': 2, '王晶': 2, '我爱大肯': 2, '温惠国': 2, '钰婷': 2, '吴宇': 2, '仁者自仁': 2, '王瑞': 2, '王杰': 2, '杨峰': 2, 'wangya': 2, '赵志童': 2, '姬成': 2, 'ZCF': 2, 'langya': 2, '王勋': 2, '缱丶某': 2, '秀秀': 2, '刘亚栋': 2, '在于---': 2, '被伤过的心': 2, '谢永蔚': 2, '最是离殇': 2, '丁雪凌': 2, '吴瑞': 2, '蒋晓峰': 2, '段煜': 2, '墨阳': 2, '亚亚': 2, '阿强': 2, '何昱': 2, '王昱': 2, '米永博': 2, '咏': 2, '陈玉哲': 2, '忘夏---依旧殇': 2, '呵小贱': 2, '轲': 2, '小伟': 2, '杨璟': 2, 'Sweety丶小任性': 2, '金峰': 2, '谢明': 2, '颉来强': 2, 'shelly': 2, '旧时光-': 2, '李Ga滨': 2, '吴宝毓': 2, '马耀序': 2, '孙佑': 2, '王尚丽': 2, '吕国平': 2, '小紫紫': 2, '李那': 2, '颉富强': 2, '王雨': 2, '小邋蹋': 2, '倩浅情歌': 2, '王小康': 2}

li = []
for j,k in result.items():
    for num in range(k):
        li.append(j)

for i in li:
    print(i)
