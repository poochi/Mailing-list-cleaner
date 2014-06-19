FIELD = ['Message:',
         'Date:',
         'From:',
         'Subject:',
         'To:',
         'Cc:',
         'Message-ID',
         'Content-Type:'
         
         ];
REXP = ['[ 0-9]+[\r\n]*',
        '[ \+0-9,\(\)a-zA-z_\t:\-@\.<>/;=\"\?]+[\r\n]'*(len(FIELD)-1)
        
        
 ]






##         'Subject:',
##         'To:',



##        '[ \+0-9,\(\)a-zA-z_\t:-@\.<>\n]+[\r\n]*',
##        '[ \+0-9,\(\)a-zA-z_\t:-@\.<>\n]+[\r\n]*',
##        '[ \+0-9,\(\)a-zA-z_\t:-@\.<>\n]+[\r\n]*',
##        '[ \+0-9,\(\)a-zA-z_\t:-@\.<>\n]+[\r\n]*'
