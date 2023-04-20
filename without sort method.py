l=[12,34,11,3,9,88,71,14]
n_l=[]
while l:
    m_l=l[0]
    for i in l:
        if i >m_l:
            m_l=i
    n_l.append(m_l)
    l.remove(m_l)
print(n_l)
    