# -*- coding: cp936 -*-

import urllib
import re
import sys
import string
import os

#reload(sys);
#sys.setfaultencoding('utf8');

class Page:
        txt='unname';
        def __init__(self, fpage):
                self.txt=fpage;
        def get(self):
                exp=re.compile(r'<p>[^<>]*</p>');
                return re.findall(exp, self.txt);
	def gettitle(self):
		exp=re.compile(r'<title>[^<>]*</title>')
		return re.findall(exp, self.txt)
        def geturls(self):
                exp=re.compile('"http://'+r'[^"]*"');
                return re.findall(exp, self.txt);
        def geturls_t(self):
                exp=re.compile('href="'+r'[^"]*"');
                return re.findall(exp, self.txt);

def src_decode(self):
        """
        sina='sina';
        gbk='gbk';
        if (urlname=='sina'):
            return self.decode(gbk);
        if (urlname=='huanqiu'):
            return self.decode('utf8');
        return self.decode('utf8');
        """
        try:
                temp=self.decode('gbk');
        except:
                print ''
        else:
                return temp;
        try:
                temp=self.decode('utf8');
        except:
                print ''
        else:
                return temp;
        try:
                temp=self.decode('gb2312');
        except:
                print ''
        else:
                return temp;
        return '?';
        return self.decode('gbk');
        return self.decode('gb2312');
        return self.decode('utf8');
        if isinstance(self, unicode):
                 return self;
        #try self.decode('gb2312'):
        #        return temp;
        global codepatten;
        if codepatten=='gbk':
                return self.decode('gbk');
        if codepatten=='gb2312':
                return self.decode('gb2312');
        if codepatten=='utf8':
                return self.decode('utf8');
def biaodian(self):
        if( 0x0000<=ord(self) and ord(self)<=0x00FF ):
                return self;    #可恶的ASCII
        if(0xFF00<=ord(self) and ord(self)<=0xFFEF):
                return self;    #全角标点
        if(0x3000<=ord(self) and ord(self)<=0x303F):
                return self;    #CJK符号和标点
        #if(0x2000<=ord(self) and ord(self)<=0x206F):
        #        return self;
        #if(0x2070<=ord(self) and ord(self)<=0x209F):
        #        return self;
        return '';
def hanzi(self):
    if(0x4E00<=ord(self) and ord(self)<=0x9FBF):
        return self;
    return '';
def huanhang(self):
    if(self=='\n'):
        return self;
    return '';
def deln(self):
    return re.sub('\n', '', self);
def redo(t):
        global records;
        for i in records:
                if t==i :
                        return True;
        return False;
def in_list(t):
        global flist;
        for i  in flist:
                if t.count(i)>0:
                        return True;
        return False;
def add(t):
        global Lim;
        global records;
        global cl;
        global flist;
        global patten;
        #print t,'!';
        if cl==Lim or t.count(patten)==0:
                return;
        if redo(t) :
                return;
        if in_list(t):
                return;
        records[cl]=t;
        cl+=1;

def getUnicode(article):
        res=u'';
        
        for i in article:
                if i=='':
                        continue;
                i=re.sub('<[A-Za-z]*>', '', i);
                i=re.sub(r'</[A-Za-z]*>', '', i);
                i=re.sub('&[A-Za-z]*;', '', i);
                i=re.sub(' ', '', i);
                res+=i+'\n';  #添加换行
	return res

        
def MainOP(url0):
        global op;
        global cl;
        global records;
        global patten;
        global flist;
        #print patten;
        #print url0;
        #print url0.count(patten);
        """
        if url0.count(patten)==0:
                #print url0,'!';
                return;
        for i in flist:
                if url0.count(i)>0:
                        return;
        """
        #print "111";
        #page='';
        
        #url0=MainPage+num;
        print "Scanning: "+url0;
        try:
                src=urllib.urlopen(url0).read();
        except:
                return;
        #src=src.decode('gbk');
        src=src_decode(src);
        if src=='?':
                return;
        #print src;
        fpage=Page(src);
        article=fpage.get();
	title = fpage.gettitle();
        """
        urls=fpage.geturls();

        for i in urls:
                add(re.sub('"', '', i));
        """
        urls=fpage.geturls_t();

        for i in urls:
                i=re.sub('href=', '', i);
                i=re.sub('"', '', i);
                if i.count('http://')==0:
                        i=patten+i;
                add(i);
                #print i;

        final=getUnicode(article)
	final_title = getUnicode(title)
        codetype=sys.getdefaultencoding();

        if len(final)<10:
                return;
                
        global output_num
        global PATH
	file_name = PATH+str(output_num)+".txt"
        f=open(file_name, "w");
	print file_name
        print "Printing: "+url0;
        #print final;
	f.write(final_title.encode('utf8'))
        f.write(final.encode('utf8'));
        f.close();
        output_num+=1;
        
        #f.write(res.encode('utf8'));
        #print src;

def init():
        global Lim;
        global label_num;
        global label;
        global codetype;
        global PATH;
        PATH=os.getcwd()+"\output/";
        if not os.path.isdir(PATH):
                os.mkdir(PATH);
        """
        fin=open("label.txt","r");
        temp=fin.readline();
        while(temp and label_num<Lim):
                str0=deln(temp);
                pos=str0.find(' ');
                label[label_num]=str0[0: pos];
                codetype[label_num]=str0[pos+1: len(str0)];
                label_num+=1;
                #print str0[0:pos],str0[pos+1:len(str0)];
                temp=fin.readline();
        fin.close();
        """
        
def get_patten(url):
        global patten;
        global codepatten;
        global label;
        global codetype;
        global label_num;
        
        for i in range(0, label_num):
                if url.count(label[i])>0:
                        patten=label[i];
                        codepatten=codetype[i];
                        return;
def getlist():
        f=open("list.txt", "r");
        global flist;
        temp=deln(f.readline());
        while(temp):
                #print temp;
                flist.append(temp);
                temp=deln(f.readline());
        f.close();

def loop(url):
        global op;
        global cl;
        global Lim;
        global records;
        add(url);
        #print url;
        #for i in range(0, cl):
        #        print records[i];
        #print records[op];
        #MainOP(records[op]);
        while(op<cl and op<Lim):
                MainOP(records[op]);
                op+=1;

def get_front(url):
        global patten;
        exp=re.compile('http://'+r'[^/]*');
        patten=(re.findall(exp, url))[0];

##################################################################
##################################################################    

PATH="";
flist=[];
getlist();                              #获取网页屏蔽关键字名单

op=0;
cl=0;
pnum=100;                               #最多标签的个数
Lim=100000;                              #最多搜索的网页数
label_num=0;                            #记录标签、网页的个数
label=range(pnum);                        #标签、网页特征
codetype=range(pnum);                    #编码类型
records=range(Lim);                     #记录已搜索的网页
output_num=0;
patten='?';
codepatten='';

init();                                 #初始化
#for i in range(0, label_num):
#        print name[i],codetype[i];
         
if (len(sys.argv)==1) or ((len(sys.argv)==2) and (sys.argv[1]=='-r')):
    f1=open("url.txt", "r");            #读入参数
    #urlname=f1.readline();
    MainPage=f1.readline();
    f1.close();
else:
    #urlname=sys.argv[1];                #使用运行参数
    MainPage=sys.argv[1];
    
#f=open("result.txt", "w");

#urlname=deln(urlname);
MainPage=deln(MainPage);

get_patten(MainPage);                   #提取特征 patten codepatten

get_front(MainPage);                    #提取网页前缀 默认为 http://**** 到第一个/前的内容

#print patten,codepatten;
#Lim=1;
print patten;
if patten=='?':
        print 'patten not found!';
else:
        loop(MainPage);
        a=1;
#print op,cl;
#print len(records);
#print PATH,Lim;

input()

