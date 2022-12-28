#get latest version from 2 version strings
#2.0 & 2.0.0.0 are same
#S='0.0' & T='0.0.2' =>T is latest
#S='2.0.0.0' & T='2.0' => Same versions
#S='2.0' & T='0.0.0.10' => S is latest

def print_latest_version(S: str, T: str) -> str:
    #split to make list
    s2 = list(map(int, S.split('.')))
    t2 = list(map(int, T.split('.')))

    #make same size
    mx = max(len(s2), len(t2))
    s2.extend([0] * (mx - len(s2)))
    t2.extend([0] * (mx - len(t2)))

    #if len(s2)>len(t2):
    #    #for i in range(len(t2),len(s2)): t2.append(0)
    #    t2.extend([0] * (len(s2) - len(t2)))
    #elif len(t2)>len(s2):
    #    #for i in range(len(s2),len(t2)): s2.append(0)
    #    s2.extend([0] * (len(t2) - len(s2)))
    print(s2, t2)

    #compare lists
    mx = max(zip(s2 ,t2))
    return 'S is latest' if mx[0]>mx[1] else 'T is latest' if mx[1]>mx[0] else 'Same versions'

    '''
    for i in range(len(s2)):
        if s2[i]>t2[i]: return 'S is latest'
        elif t2[i]>s2[i]: return 'T is latest'
    return 'Same versions'
    '''

S='0.0'
T='0.0.2'
print(print_latest_version(S, T))

S='2.0.0.0'
T='2.0'
print(print_latest_version(S, T))

S='2.0'
T='0.0.0.10'
print(print_latest_version(S, T))

