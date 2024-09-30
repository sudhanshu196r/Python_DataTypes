
def ans():
    ans=[]



def main():
    st1 = 'google.com'
    ans_dict = {}
    for i in st1:
        if i == '.':
            continue
        elif i not in ans_dict:
            ans_dict[i]=1
        else:
            ans_dict[i]+=1

    new_dict = sorted(ans_dict.items(), key=lambda x:x[1], reverse=True)

    str_dict= str(new_dict)
    str_ans = ''
    
    for ele in new_dict:
        str_ans= str_ans+str(ele[0])+str(ele[1])

    print(str_ans)

    
    # print(ans_dict.items())
    print(new_dict)

    li = [1,2,3,2,4,1,5,6,8,5]
    unique = []
    c=0
    for ele in li:
        if ele not in unique:
            unique.append(ele)
        else:
            c+=1
            if c==1:
                unique.append(ele)

    print(unique)

if __name__=="__main__":
    main()
