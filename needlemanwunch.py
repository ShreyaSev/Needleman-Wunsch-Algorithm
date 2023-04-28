import numpy as np

def getMatrix(x,y,gap):

    matrix = []
    for i in range(len(x)+1):
        sub_matrix = []
        for j in range(len(y)+1):
            sub_matrix.append(0)
        matrix.append(sub_matrix)

    for i in range(len(x)+1):
        matrix[i][0] = gap*i
    for i in range(len(y)+1):
        matrix[0][i] = gap * i
    return matrix


def getTracebackMatrix(x,y):

    tback = []
    for i in range(len(x)+1):
        sub_matrix = []
        for j in range(len(y)+1):
            sub_matrix.append(0)
        tback.append(sub_matrix)
    
    tback[0][0] = 'done'

    for i in range(1,len(x)+1):
        tback[i][0] = 'up'
    for i in range(1,len(y)+1):
        tback[0][i] = 'left'

    return tback

def scoringFunction(x,y,i,j,matrix,gap,match_score, mismatch):
    match = 0
    temp = -1
    t_temp = ''
    if x[i-1] == y[j-1] :
        match = True
    else:
        match = False
    #print(match)
    if match == True :
        #print(matrix[i-1][j-1] + match)
        return (matrix[i-1][j-1] + match_score), 'diag'
    else:
        temp = np.argmax(((matrix[i-1][j-1] + mismatch), (matrix[i][j-1] + gap), (matrix[i-1][j]+ gap)))
        if temp == 0:
            t_temp = 'diag'
        elif temp == 1:
            t_temp = 'left'
        else:
            t_temp = 'up'
        return max(matrix[i-1][j-1] + mismatch, matrix[i][j-1] + gap, matrix[i-1][j]+ gap), t_temp

def fillmatrix(matrix, traceback_matrix, gap, match, mismatch,x,y):
    for i in range(1,len(x)+1):
        for j in range (1,len(y)+1):
            matrix[i][j],t_temp = scoringFunction(x,y,i,j,matrix,gap, match, mismatch)
            traceback_matrix[i][j] = t_temp
    return matrix,traceback_matrix

def traceback(traceback_matrix, x, y):
    s1 = ''
    s2 = ''

    max_i = len(x) 
    max_j = len(y) 

    i = max_i
    j = max_j

    arr = ''
    
    temp = 1
    while(True):
        if temp==1:
            s2+=x[i-1]
            s1+=y[j-1]
            i-=1
            j-=1
        
        elif temp==0:
            s2+='-'
            s1+=y[j-1]
            j-=1
        
        elif temp==2:
            s2+=x[i-1]
            s1+='-'
            i-=1


        if traceback_matrix[i+1][j+1] == 'diag':
            temp=1
        
        elif traceback_matrix[i+1][j+1] == 'up':
            temp = 2

        elif traceback_matrix[i+1][j+1] == 'left':
            temp = 0
        
        if x[i-1] == y[j-1]:
            temp = 1
            
        
        
        if (i<1 and j<1):
            break

    for i in range(len(s1)):
        if s1[i]==s2[i]:
            arr+='|'
        else:
            arr += ' '  
    return s1, s2,arr
        


def sequence_alignment():
    y = input('Enter sequence 1: ')
    x = input('Enter sequence 2: ')
    gap = eval(input('Enter gap penalty: '))
    match_score = eval(input('Enter match score: '))
    mismatch = eval(input('Enter mismatch score: '))
    m = getMatrix(x,y,gap)
    t = getTracebackMatrix(x,y)
    m,t = fillmatrix(m,t,gap,match_score,mismatch,x,y)


    s1, s2 ,arr = traceback(t,x,y)
    print('The global sequence alignment is: ')
    print (s1[::-1])
    print (arr[::-1])
    print (s2[::-1])


if __name__=='__main__':
    sequence_alignment()