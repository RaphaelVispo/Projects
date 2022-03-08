
#general encrpytion for messages and bio
def encryption(string):
    encryptedstring=""
    enlist=encryptions.keys()

    for letter in string:
        if letter not in enlist:
            encryptedstring+=letter
            continue
        else:
            encryptedstring+=encryptions[letter]

    return encryptedstring

#general encrption for messages and bio
def decryption(string):
    decryptedstring=""
    delist=decryptions.keys()

    for letter in string:
        if letter not in delist:
            decryptedstring+=letter
            continue
        else:
            decryptedstring+=decryptions[letter]

    return decryptedstring



'''encrytion and decrytion for messeges and bio'''

encryptions={
'a':'1',  'b':'A',   'c':'B',   'd':'2',   'e':'X',
'f':'3',  'g':'q',   'h':'Y',   'i':'Z',   'j':'y',
'k':'a',  'l':'0',   'm':'r',   'n':'C',   'o':'D',
'p':'s',  'q':'E',   'r':'F',   's':'W',   't':'6',
'u':'+',  'v':'5',   'w':'b',   'x':'>',   'y':'p',
'z':'e',  'A':'z',   'B':'~',   'C':'o',   'D':'c',
'E':'%',  'F':'N',   'G':'O',   'H':'8',   'I':'9',
'J':'*',  'K':'!',   'L':'#',   'M':'n',   'N':'P',
'O':'G',  'P':'$',   'Q':'d',   'R':'M',   'S':'^',
'T':')',  'U':'L',   'V':'u',   'W':'(',   'X':'Q',
'Y':'V',  'Z':'U',   '0':'t',   '1':'<',   '2':'f',
'3':'=',  '4':'H',   '5':'l',   '6':'-',   '7':'T',
'8':'v',  '9':'7',   '@':' ',   '~':'_',   '!':'m',
'#':'x',  '$':'g',   '%':'&',   '^':'j',   '&':'K',
'*':',',  '(':'S',   ')':'R',   '_':'i',   '-':'J',
'+':'w',  '=':'I',   '<':'h',   '>':'k',   ' ': '@', 
',':'.',  '.':'/',   '/':'?',   '?':'\\', '\\': '|',
'|':'[',  '[':']',   ']':'{',   '{':'}',  '}' :'`',
'`':'\'', '\'':'\"','\"':';',   ';':'4'   
}

decryptions={
'1':'a',  'A':'b',  'B':'c',  '2':'d',  'X':'e', 
'3':'f',  'q':'g',  'Y':'h',  'Z':'i',  'y':'j',
'a':'k',  '0':'l',  'r':'m',  'C':'n',  'D':'o',
's':'p',  'E':'q',  'F':'r',  'W':'s',  '6':'t',
'+':'u',  '5':'v',  'b':'w',  '>':'x',  'p':'y',
'e':'z',  'z':'A',  '~':'B',  'o':'C',  'c':'D',
'%':'E',  'N':'F',  'O':'G',  '8':'H',  '9':'I',
'*':'J',  '!':'K',  '#':'L',  'n':'M',  'P':'N',
'G':'O',  '$':'P',  'd':'Q',  'M':'R',  '^':'S',
')':'T',  'L':'U',  'u':'V',  '(':'W',  'Q':'X',
'V':'Y',  'U':'Z',  't':'0',  '<':'1',  'f':'2', 
'=':'3',  'H':'4',  'l':'5',  '-':'6',  'T':'7', 
'v':'8',  '7':'9',  ' ':'@',  '_':'~',  'm':'!', 
'x':'#',  'g':'$',  '&':'%',  'j':'^',  'K':'&', 
',':'*', 'S':'(',  'R':')',  'i':'_',  'J':'-',
'w':'+',  'I':'=',  'h':'<',  'k':'>',  '@':' ',
'.': ',', '/':'.',  '?':'/', '\\':'?', '|':'\\',
'[': '|', ']':'[',  '{': ']', '}': '{', '`':'}', 
"\'":'`', '\"':"\'",';':'\"', '4':';'
}