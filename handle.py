# ---coding:utf-8----
import sqlite3
import os


class Handle(object):
    # setting dir
    dir = r"E:\PyCharm 2017.2.2\mypro_3.6\user_dic\\"
    db_dir = r"E:\PyCharm 2017.2.2\mypro_3.6\\"

    # 翻译
    def trans(self, word):
        conn = sqlite3.connect(self.db_dir+"free_dic.db")
        c = conn.cursor()
        c.execute("select cn from dictTB where en='%s';" % word)
        v = c.fetchall()
        if len(v) == 0:
            return [('没这词哦，大佬！')]
        conn.close()
        return v

    # 添加字典
    def dic_add(self, file, dic_name):
        file.save(self.dir + dic_name)
        return 1

    def dic_ls(self):
        dic_list = os.listdir(self.dir)
        return dic_list

    # 删除字典
    def dic_del(self, dic_name):
        os.remove(self.dir + dic_name)
        return True

    # 获取字典内容(返回str)
    def dic_content(self, dic_name):
        dic_obj = open(self.dir + dic_name)
        try:
            dic_con = dic_obj.read()
        finally:
            dic_obj.close()
        return dic_con

    # 返回给定字典的英文LIST和中文翻译LIST
    def dic_cnlist(self, dic_name):
        dic_str = self.dic_content(dic_name)
        if dic_str[-1] == "\n":
            dic_str.rstrip("\n")
        en_list = dic_str.split('\n')
        cn_list = []
        for item in en_list:
            cn_t = self.trans(item)
            cn_str = "".join(cn_t[0])
            cn_word = cn_str.replace('\\n', '-------------------')
            cn_list.append(cn_word)
        return en_list, cn_list
