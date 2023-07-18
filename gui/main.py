
import json
import os
import streamlit as st
def load_data():
    
    uploaded_file = st.file_uploader("Choose a file, or continue with the default one")
    if uploaded_file!=None:
        with open(uploaded_file.name,"r",encoding="utf-8") as f:
            json_data=json.load(f)
        return json_data
    else:
        with open("example.json","r",encoding="utf-8") as f:
            json_data=json.load(f)
        return json_data




def read_articles(filename):
    
    with open(filename, 'r', encoding="utf-8") as f:
        # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
        dic=json.load(f)
        print(dic["articles"][0]["title"])
        data=dic
        return data



def get_inputs(hints):
    keys = []
    for hint in hints:
        tmp=st.text_input(hint)
        # TODO: 读取一个用户输入并且存储到 keys 当中
        keys.append(str(tmp))
    
    return keys


def replace(article, keys):
    for i in range(len(keys)):
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        oldstr="{{"+str(i+1)+"}}"
        article["article"]=article["article"].replace(oldstr,keys[i])
    return article
    

def selectarticle(articles):
    namelist=[]
    for tmparticle in articles:
        namelist.append(tmparticle["title"])


    option = st.selectbox(
        'Choose which article?',
        namelist)

    st.write('You selected:', option)
    for tmparticle in articles:
        if tmparticle["title"] == option:
            article=tmparticle
            break
    return article
def test(keys,hints):
    for key in keys:
        if key==None:
            return 0
    if len(keys)!=len(hints):
        return 0
    return 1
def showans(article):
    if st.button("Comfirm"):
        st.subheader("Your answer:")
        st.write(article)
        text_contents = article
        st.download_button('Download your ans', text_contents)

def functionselect():
    st.title("Welcome to the Game!")
    option = st.selectbox(
        'Choose mode',
        ('Start game', 'Create game'))
    if option=='Start game':
        return 1
    else:
        return 0

def gameset():
    lanoption = st.selectbox(
        'Choose language',
        ('zh', 'en'))
    title=st.text_input("Input the title:")
    content=st.text_input("Input the content:")
    path=""
    try:
        num=int(st.text_input("How many hints"))
        hints=[]
        for _ in range(0,num):
            hint=st.text_input(f"Input the {_} hint")
            hints.append(str(hint))
        path=st.text_input("Where to store your json file? Exsisting or New is acceptable",placeholder="Full path ( including the name of your json file )")
    except:
        st.write("")
    if st.button("Confirm") and path.endswith(".json"):
        obj={"title":title,"article":content,"hints":hints}
        item_list=[]
        try:
            if not os.path.exists(path):
                os.system(r"touch {}".format(path))
            else:
                with open(path,'r') as f:
                    load_dict = json.load(f)
                    load_dict=load_dict
                    if load_dict["language"]=="zh":
                        lanoption="zh"
                    num_item = len(load_dict["articles"])
                    for i in range(num_item):
                        id = load_dict["articles"][i]['title']
                        text = load_dict["articles"][i]['article']
                        text_hint = load_dict["articles"][i]['hints']
                        item_dict = {'title':id, 'article':text,'hints':text_hint}
                        item_list.append(item_dict)
            item_list.append(obj)
            full_list={"language":lanoption,"articles":item_list}
            with open(path, 'w', encoding='utf-8') as f2:
                json.dump(full_list, f2, ensure_ascii=False)
        
            st.subheader("Your have already created a new game, now enjoy it!")
        except:
            st.warning("Something is wrong!")
    else:
        st.warning("Please check your input!")

    

    

if __name__ == "__main__":
    op=1
    op=functionselect()
    if op==1:
        data=load_data()
        articles = data["articles"]
        article=selectarticle(articles)
        keys=get_inputs(article["hints"])
        article=replace(article,keys)
        if test(keys,article["hints"])==1:
            showans(article["article"])
    else:
        gameset()
        


