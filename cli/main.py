import argparse
import json
import random
import streamlit as st
def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-n", "--name", help="文章名字", required=False)
    
    args = parser.parse_args()
    
    return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    
    with open(filename, 'r', encoding="utf-8") as f:
        # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
        dic=json.load(f)
        print(dic["articles"][0]["title"])
        data=dic
        return data



def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        print(f"请输入{hint}:",end=" ")
        # TODO: 读取一个用户输入并且存储到 keys 当中
        key=input()
        keys+=key

    return keys


def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        oldstr="{{"+str(i+1)+"}}"
        article["article"]=article["article"].replace(oldstr,keys[i])
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换
    return article
    

def selectarticle(args,articles):
    if args.name==None:
        count=0
        for articletmp in articles:
            count+=1
        num=random.randint(0,count-1)
        article=articles[num]
        print("未指定文章，已经为你随机选择文章:","<",article["title"],">",sep=" ")
    else:
        flag=0
        count=0
        for articletmp in articles:
            count+=1
            if articletmp["title"]==args.name:
                flag=1
                break
        if flag==1:
            article=articletmp
            print("已经为你选择文章",article["title"],sep=": ")
        else:
            
            num=random.randint(0,count-1)
            article=articles[num]
            print("该文章不存在，已经为你随机选择文章",article["title"],sep=": ")
    
    return article
    

if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]
    article=selectarticle(args,articles)
    keys=get_inputs(article["hints"])
    article=replace(article,keys)
    print(article["article"])
    
        

    # TODO: 给出合适的输出，提示用户输入
    # TODO: 获取用户输入并进行替换
    # TODO: 给出结果



