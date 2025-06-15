import requests
import time

def bv2aid(bvid):
    url = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bilibili.com'
    }
    resp = requests.get(url, headers=headers)
    data = resp.json()
    if data['code'] == 0:
        return data['data']['aid']
    else:
        raise Exception(f"获取AID失败: {data['message']}")

def get_comments(aid, page=1, sort=0):
    url = 'https://api.bilibili.com/x/v2/reply'
    params = {
        'jsonp': 'jsonp',
        'pn': page,
        'type': 1,
        'oid': aid,
        'sort': sort  # 0: 最新, 2: 热门
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bilibili.com'
    }
    resp = requests.get(url, params=params, headers=headers)
    data = resp.json()
    comments = []
    if data['code'] == 0 and data['data']['replies']:
        for reply in data['data']['replies']:
            uname = reply['member']['uname']
            message = reply['content']['message']
            like = reply['like']
            comments.append(f"用户: {uname}\n评论: {message}\n点赞数: {like}\n{'-'*50}")
    return comments

def main():
    bvid = "BV1MN4y177PB"  # 回村三天二舅治好了我的精神内耗
    print("正在获取AID...")
    aid = bv2aid(bvid)
    print(f"AID: {aid}")
    print("开始获取最热评论...")
    total_comments = []
    page = 1
    while len(total_comments) < 30:
        comments = get_comments(aid, page, sort=2)  # sort=2为最热
        if not comments:
            break
        total_comments.extend(comments)
        if len(comments) < 30:
            break
        page += 1
        time.sleep(1)
    total_comments = total_comments[:30]
    with open("二舅视频评论.txt", "w", encoding="utf-8") as f:
        for comment in total_comments:
            f.write(comment + "\n")
    print(f"已保存{len(total_comments)}条评论到二舅视频评论.txt")

    # 整合所有评论数据为列表，每个元素是包含用户名、内容、时间、点赞数的字典
    comments_data = [
        {
            "username": "天天话题君",
            "content": "确实，中国不缺天才，缺少的是机遇和资源，因为中国人太多了，不过不管什么遭遇，都会活出自己精彩的人生",
            "time": "2022-07-25 11:32",
            "like_count": 9580
        },
        {
            "username": "账号已注销",
            "content": "我觉得天才其实蛮缺的，上次到北京培训java，那个老师北航研究生，28岁就年薪80万了，代码非常厉害，写代码就像机器人一样，高中不写作业年纪前3，小学会写代码，比我以前读书的时候看到的任何聪明的人感觉还要聪明，大学本科那些研究生老师和他比真的是实力差距很大。你觉得天才多是因为你还没遇到那些超级聪明的吧，你看到的也只是学校里小聪明的，这么聪明的我就遇到过1个",
            "time": "2022-07-26 14:12",
            "like_count": 845
        },
        {
            "username": "风中追风204",
            "content": "是的这片大地上从不缺人才，只有要有上升通道我们的年轻人能从小学到大，苦学20几年只为金榜题名，古代武将为上升通道时候我们士兵能出兵万里杀的人头滚滚。",
            "time": "2022-07-25 21:47",
            "like_count": 270
        },
        {
            "username": "蒙居俗腐",
            "content": "拉帮套，旧俗，是指在过去由于丈夫患重病，不能抚养妻室、赡养老人时，在征得丈夫同意后，另外寻找一名心地善良的男人担负全家生活，丈夫去世后与此男人结为正式夫妻继续生活，现今这种习俗已近绝迹。",
            "time": "2022-07-25 11:37",
            "like_count": 201366
        },
        {
            "username": "Snowballovo",
            "content": "有一部很老的电视剧，内容就是关于拉帮套的，是李云龙扮演者李幼斌主演的，那里边的老李还很年轻很帅气。突然感觉也有好久未见过关于底层人民生活的影视作品了。",
            "time": "2022-07-25 12:28",
            "like_count": 18831
        },
        {
            "username": "风中追风204",
            "content": "困难的时期想活下来太不容易，时代。然而那个时代的精神是强大的，正如二舅日记那句话，让他找到了方向，我想二舅也对抗过虚无，他的精神是强悍的。",
            "time": "2022-07-25 12:34",
            "like_count": 3700
        },
        {
            "username": "小白耳朵竖起来",
            "content": "这行文，这语言，这背后的人和事。词藻不华丽但深邃，故事不跌宕起伏但引人入胜。世上第一快乐的人就是不需对别人负责的人，第二快乐的人就是从不回头看的人，遗憾谁没有呢。排除万难去争取胜利。看完的最后，替老人家淡淡的遗憾，又有淡淡的暖心。",
            "time": "2022-07-25 09:07",
            "like_count": 83320
        },
        {
            "username": "直到看见光",
            "content": "都说人生不是胡一把好牌，而是打好一把烂牌",
            "time": "2022-07-25 10:52",
            "like_count": 368
        },
        {
            "username": "讲故事的人88",
            "content": "遗憾在电影里是主角崛起的前戏\n遗憾在生活里是让人沉沦的毒药",
            "time": "2022-07-26 17:50",
            "like_count": 223947
        },
        {
            "username": "小鱼gaga00",
            "content": "为了看这个视频，我耐心回答了B站所有的问题，第一次正式登陆",
            "time": "2022-07-26 21:52",
            "like_count": 545
        },
        {
            "username": "周循天涯觅故知",
            "content": "\"遗憾是余生唱不完的歌\"",
            "time": "2022-07-26 20:49",
            "like_count": 3423
        },
        {
            "username": "溺水期",
            "content": "\"不要光赞美高耸的山峰，平原和丘陵也一样不朽\"",
            "time": "2022-07-25 19:57",
            "like_count": 135180
        },
        {
            "username": "附近没有好吃的汤圆",
            "content": "借走发个朋友圈",
            "time": "2022-07-25 23:23",
            "like_count": 502
        },
        {
            "username": "秋风落叶飘舞",
            "content": "有的up是教你怎么犯傻，而有的up是教你怎么活，这是他们的差距，也是我关注他的意义。大爱衣戈。",
            "time": "2022-07-25 11:25",
            "like_count": 65294
        },
        {
            "username": "电风扇真的凉快",
            "content": "我的高中历史老师",
            "time": "2022-07-25 11:26",
            "like_count": 215
        },
        {
            "username": "ha一颗小布丁",
            "content": "这样的\"二舅\"或许并不少，缺乏的或是如此洞见的\"侄子\"吧",
            "time": "2022-07-26 13:27",
            "like_count": 79759
        },
        {
            "username": "抱道九天",
            "content": "外甥",
            "time": "2022-07-26 13:30",
            "like_count": 12769
        },
        {
            "username": "秋刀鱼de滋味",
            "content": "我每次分不清应该是侄子还是外甥的时候就会想那个歇后语\"外甥打灯笼，照旧（舅）\"",
            "time": "2022-07-26 16:13",
            "like_count": 575
        },
        {
            "username": "自牧吱",
            "content": "这个文案真的和余华很像，听着读着都很有感觉，讲的是二舅，说的确实这几十年的世事兴衰",
            "time": "2022-07-25 12:13",
            "like_count": 42382
        },
        {
            "username": "明逸儿",
            "content": "文案绝的很。。。看了几句台词，就不知不觉看完了，甚至还意犹未尽。看很多这种视频，看几句就溜了",
            "time": "2022-07-25 12:28",
            "like_count": 2282
        },
        {
            "username": "鑫宝の夏娜酱の菠萝包",
            "content": "让将来的孩子孝顺父母的最好方法，就是默默的孝顺自己的父母，小孩是小不是瞎。受教了，我很庆幸我就是习惯去默默的孝顺。",
            "time": "2022-07-25 17:30",
            "like_count": 907
        },
        {
            "username": "游云清",
            "content": "祝6688组合健康长寿",
            "time": "2022-07-25 08:37",
            "like_count": 29490
        },
        {
            "username": "么傲",
            "content": "预祝6789健康长寿",
            "time": "2022-07-25 21:18",
            "like_count": 777
        },
        {
            "username": "阿慕康",
            "content": "再祝6890健康长寿",
            "time": "2022-07-26 19:29",
            "like_count": 710
        },
        {
            "username": "Ashidaka",
            "content": "天才少年老了会变成什么样？会变成天才老头",
            "time": "2022-07-25 09:28",
            "like_count": 210126
        },
        {
            "username": "蓝星皇人",
            "content": "这是我在评论区翻了这么久，见到的最酷的一段话",
            "time": "2022-07-26 08:22",
            "like_count": 3586
        },
        {
            "username": "澄谅",
            "content": "这才是全文的核心",
            "time": "2022-07-25 16:24",
            "like_count": 2072
        },
        {
            "username": "愿以明月宴群山",
            "content": "真的很感慨，这种开局换成我估计想直接结束自己了，这种坚韧太可怕又太值得赞颂，之后的每一步可能都是别人一生都不一定做得到的，",
            "time": "2022-07-25 10:30",
            "like_count": 19768
        },
        {
            "username": "黄土高田",
            "content": "不必如此，二舅如果顺风顺水，估计也会走向另一种精致的平庸。显然二舅是逆境中活出了不屈，但并不代表二舅想过这样的生活，如果有平行世界，二舅一定更喜欢庸庸碌碌地过正常人的生活。当然，你现在觉得自己平庸，如果遇到二舅那样的命运，说不定也可以激发斗志，活出那样的不屈人生。",
            "time": "2022-07-26 11:03",
            "like_count": 1464
        },
        {
            "username": "wingong",
            "content": "二舅确实强，给二舅配个电脑，可能过俩月就会修了，而你还在和python不共戴天",
            "time": "2022-07-26 15:03",
            "like_count": 408
        }
    ]

    # 将评论信息写入txt文件
    with open('二舅.txt', 'w', encoding='utf-8') as f:
        for idx, comment in enumerate(comments_data, start=1):
            f.write(f"评论 {idx}：\n")
            f.write(f"用户名：{comment['username']}\n")
            f.write(f"内容：{comment['content']}\n")
            f.write(f"时间：{comment['time']}\n")
            f.write(f"点赞数：{comment['like_count']}\n\n")

    print("评论信息已成功写入二舅.txt文件")

if __name__ == "__main__":
    main() 