
def saveDictionary(filename='dict.txt'):
    import pandas as pd
    import re
    url = 'https://www.cpubenchmark.net/CPU_mega_page.html'
    
    tables = pd.read_html(url)
    table = tables[3].values.tolist()[::2] 
    print(table[100])   
    #[print('{}: {}'.format(item[0], item[2])) for item in table if re.search('AM3', str(item[9]))]
    #k = dict([ (pattern.findall(item[0])[0],item[1]) for item in table if pattern.search(item[0]) ])
    #z = dict([ (patternAMD.findall(item[0])[0],item[2]) for item in table if re.search('AM3', str(item[9])) and patternAMD.search(item[0]) ])
    z = dict([ (item[0], [item[2], item[9]]) for item in table ])
    with open(filename,'w') as f:
        f.write(str(z))
        
    return z
        
def loadDictionary(filename='dict.txt', sockets=['AM3', 'AM2']):
    from numpy import nan
    import re
    with open(filename, 'r') as f:
        d = eval(f.read())
    z = dict( [key, d[key]] for key in d for socket in sockets if re.search(socket, str(d[key][1])) )
    
    return z

if __name__ == '__main__':
    import re
    iseries = re.compile('i[3579]\s*-*\s*\d{3,4}\s*[(p)ktcsbehr(hq)(te)(eq)(kf)]*', re.I)
    pentium = re.compile('g\s*\d{3,4}\s*[(te)t]*', re.I)
    xeons   = re.compile('[elx]3*\s*-*\s*\d{4}[lg]*', re.I)
    athlonx = re.compile('x[234p6]\s\d{3,4}[etu\+]*', re.I)
    athlon = re.compile('(?<!fx-)(?<!fx)(?<!\w)(?<!fx\s)(?<!x[234p6]\s)[(le)(gp)(be)]*-*\d{4}[\+eb]*(?!\w)', re.I)
    fxs = re.compile('fx\s*-*\s*b*\d{4}e*', re.I)
    xnbs = re.compile('x[234]\sb\d{2}e*', re.I)
    
    amds = [fxs, athlonx, athlon, xnbs]
    intels = [iseries, pentium, xeons]
    
    #TODO
    # 1. sub signs according to rules for each socket
    # 2. change search to == .upper()
    #saveDictionary()
    k = loadDictionary(sockets = ['1151', '1150', '1155', '1156'])
    #k = loadDictionary(sockets = ['AM3', 'AM3+', 'AM2+'])
    z = {}
    with open('names.txt', 'r') as f:
        names = f.readlines()
    names = [item.rstrip('\n') for item in names]
        
    
    [print(item) for item in k]
    print(names[-2])
    
    
    for key in k:
        for pattern in amds:
            if pattern.search(key):
                #print('{}: \033[0;32m {} \x1b[0m'.format(key, pattern.findall(key) ))
                pass
                z[pattern.findall(key)[0]] = k[key]
                break
    #print(z)
        #[print('{}: \033[0;32m {} \x1b[0m'.format(key, pattern.findall(key) )) for pattern in amds]
         

    #re.findall("([i,I,g,G,E,X,e,x]\d*\s*-*\s*\d{3}\d*[P,p,k,K,t,T,s,S]*)", element['name'])
    #print( re.findall("(i\d.\d{3}.)", 'Intel Core i5 3470 3,20GHz 100% sprawny'))

