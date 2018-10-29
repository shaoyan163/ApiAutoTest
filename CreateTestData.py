# coding=utf-8
import random
import time


def create_user():
    start = time.time()
    count = 1000  # 一千万条数据
    beginId = 200010000
    with open(r"E:\Desktop\a\userInfo.txt", "w") as fp:
        for i in range(1, count+1):
            id = str(i)
            userId = beginId + i
            name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 4)).replace('', '')
            sex = str(random.choice(['男', '女']))
            weight = str(random.randrange(10, 99))
            address = str(random.choice(['北京', '上海', '深圳', '广州', '杭州']))
            insert_t_user_weight = (
                            "INSERT INTO t_user_weight VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s');"
            % (id, userId, name, sex, weight, address, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                       )
            insert_t_user_weight = insert_t_user_weight + '\n'
            # print(insert_t_user_weight)
            fp.write(insert_t_user_weight)

        print('共创建%d条sql耗时：'% count, time.time() - start)


if __name__ == "__main__":
        create_user()
