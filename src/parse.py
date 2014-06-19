# open file .
#find out part between header and footer .
# for each in part:
#find out if they are unique
# remove lines which start with >
# Create a list of conversation based on subject
import re;
import loadable;


def getmedata(text):   

    FIELD = loadable.FIELD;
    REXP = loadable.REXP;
    
    string = '';
    for field,rexpr in zip(FIELD,REXP):
        string+=re.escape(field)+rexpr;

    #string = re.escape(FIELD[0])+REXP[0]+re.escape(FIELD[1])+REXP[1]
    print string
    ID = re.escape(FIELD[0])+REXP[0];
    start=[];end=[];
    res={};
    match = re.findall(string, text);
    print match

    for each in match:
        s = text.find(each);
        val_id = re.search(ID,each);
        print "VALID "+val_id.group(0);
        start.append(s);
        end.append(s+len(each));
        for (st,ed) in zip(end[:-1],start[1:]):
            info=[];
            print 'hello'
            for each in text[st:ed].split('\n'):            
                if each is '' :
                    continue;
                if each[0] is '>' :
                    continue;
                info.append(each);
            res[str(val_id.group(0))]=info;
    
    return res;
            
            



        
        
path = "/home/poochi/Desktop/Project/utility/mailingList.txt"
f = open(path,"r");
text = f.read();
f.close()
result = getmedata(text);
print result[result.keys()[0]];

