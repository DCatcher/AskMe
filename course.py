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
        def get_td(self, p, q):
                exp=re.compile(p+r'[^/]*'+q);
                temp=re.findall(exp, self.txt);
                #print len(temp),'???'
                for i in range(0,len(temp)):
                    temp[i]=re.sub(p, '', temp[i]);
                    temp[i]=re.sub(q, '', temp[i]);
                    temp[i]=re.sub('\n', '', temp[i]);
                    temp[i]=re.sub('  ', '', temp[i]);
                return temp;
        def get_hw(self):
                exp=re.compile('<td valign="top" bgcolor="#f7f3ef">'+r'[^t]*'+'</td>');
                temp=re.findall(exp, self.txt);
                for i in range(0, len(temp)):
                    temp[i]=re.sub('<td valign="top" bgcolor="#f7f3ef">', '', temp[i]);
                    temp[i]=re.sub('</td>', '', temp[i]);
                    temp[i]=re.sub('\n', '', temp[i]);
                    temp[i]=re.sub('  ', '', temp[i]);
                return temp;
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
        if (urlname=='sina
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
def Print(self):
    for i in self:
        print i;
def clean(temp):
    temp=re.sub('&nbsp;', '', temp);
    temp=re.sub('<'+r'.*'+'>', '', temp);
    return temp;

def get(temp, t):
    try:
        k=temp[t];
    except:
        k='';
    return k;
        
def MainOP(url0):
        global op;
        global cl;
        global records;
        global patten;
        global flist;
        global output_num;

        print "Scanning: "+url0;
        try:
                src=urllib.urlopen(url0).read();
        except:
                return;
        #src=src.decode('gbk');
        src=src_decode(src);
        if src=='?':
                return;
        if src.count(u'没有这一课程的信息！')>0:
                return;
        source=Page(src);
        #print src;
        cname=source.get_td('<p>&nbsp;', '</p>');
        name=source.get_td('<td valign="middle" colspan="5">', '</td>');
        tel=source.get_td('<td valign="top" colspan="5" bgcolor="#f7f3ef">', '</td>');
        address=source.get_td('<td valign="top" colspan="5">', '</td>');
        book=source.get_td('<td valign="middle" colspan="5" align="center" bgcolor="#f7f3ef">', '</td>');
        point=source.get_td('<td valign="top" width="56">', '</td>');
        leng=source.get_td('<td valign="top" width="65">', '</td>');
        test=source.get_td('<td width="78" valign="top">', '</td>');
        homework=source.get_td('<td valign="top" bgcolor="#f7f3ef">', '</td>');
        homeworkn=source.get_hw();
        openw=source.get_td('<td colspan="5" valign="top">', '</tr>');
        tuse=source.get_td('<td colspan="5" bgcolor="#f7f3ef">', '</td>');
        suse=source.get_td('<td colspan="5">', '</td>');
        if len(cname)==0:
            return;
        ##print(src);
        final=[];
        final.append(u'课程名：'+get(cname, 0));
        final.append(u'教师：'+get(name, 0));
        final.append(u'联系方式：'+get(tel, 0));
        final.append(get(address, 0));
        #print tel[0];
        final.append(get(tel, 1));
        final.append(u'课程简介：'+get(address, 1));
        final.append(u'教材名称：'+get(book, 0));
        final.append(u'学分:'+get(point, 0));
        final.append(u'课时:'+get(leng, 0));
        final.append(u'考察方式：'+get(test, 0));
        final.append(u'课件及讲义数：'+get(homework ,0));
        final.append(u'讨论文章数：'+get(homework, 1));
        #final.append(u'
        final.append(u'布置作业/提交作业：'+get(homeworkn, 2));
        final.append(u'课程开发范围：'+get(openw, 0));
        final.append(u'任课老师使用功能：'+get(tuse, 0));
        final.append(u'对选本课程学生开放功能：'+get(suse, 0));
        final.append(u'对校外用户开放功能：'+get(tuse, 1));
        final.append(u'对guest用户开放功能：'+get(suse, 1));
        #print len(homework);        
        #Print(temp);
        #print len(cname);
        #Print(name);
        #Print(tuse);
        #Print(suse);
        #Print(final);

        f=open(PATH+str(output_num+1)+".txt", "w");
        print "Printing: "+url0;
        #print final;
        for i in final:
            i=clean(i);
            f.write(i.encode('utf8')+'\n');
        f.write(url0);
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


##################################################################
##################################################################    

PATH="";
flist=[];

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
"""
         
if (len(sys.argv)==1) or ((len(sys.argv)==2) and (sys.argv[1]=='-r')):
    f1=open("url.txt", "r");            #读入参数
    #urlname=f1.readline();
    MainPage=f1.readline();
    f1.close();
else:
    #urlname=sys.argv[1];                #使用运行参数
    MainPage=sys.argv[1];
"""
    
#f=open("result.txt", "w");

#urlname=deln(urlname);
#MainPage=deln(MainPage);

#print patten,codepatten;
#Lim=1;
print patten;

website='http://learn.tsinghua.edu.cn/learn/courseinfo.jsp?course_id=';

for i in range(100000, 200000):
    num=str(i);
    while len(num)<6:
        num='0'+num;
    MainOP(website+num);

#MainOP(MainPage);
#print op,cl;
#print len(records);
#print PATH,Lim;



