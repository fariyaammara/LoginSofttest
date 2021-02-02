'''def brackets(expression):
   all_br = ['()', '{}', '[]']
   while any(x in expression for x in all_br):
      for br in all_br:
         expression = expression.replace(br, '')
   return not expression

# calling the function
input_string = "([]{}()"
if brackets(input_string):
   print(input_string,"balanced")
else:
   print(input_string,"Not balanced")
'''

input="((A=2 &&B=3)||(C=4&&D=5))"
while(input.startswith("(")):
    dict={}
    listing=[]
    exp1,exp2=input.split("||")
    print("numb1",exp1)
    print("numb2",exp2)
    exp3,exp4=exp1.split("&&")
    exp5,exp6=exp2.split("&&")
    dummy_check=[")","("]
    fil_exp3=exp3.replace("((","")
    fil_exp4=exp4.replace(")","")
    fil_exp5=exp5.replace("(","")
    fil_exp6=exp6.replace("))","")
    list_get1=fil_exp3.split("=")
    list_get2=fil_exp4.split("=")
    list_get3=fil_exp5.split("=")
    list_get4=fil_exp6.split("=")
    innerdict={}
    innerdict["and"]={
        list_get1[0]:list_get1[1],
        list_get2[0]:list_get2[1]
    },
    {
        list_get3[0]:list_get3[1],
        list_get4[0]:list_get4[1]
    }
    listing.append(innerdict)
    dict["or"]=innerdict
    print(dict)
    '''for i in dummy_check:
        if(i in exp3 or (i in exp4) or (i in exp5) or (i in exp6)):
            replace(i)
    print("1",exp3)
    print("2",exp4)
    print("3",exp5)
    print("4",exp6)'''
    '''listing.append(exp1)
    listing.append(exp2)
    print("i am list",listing)
    for i in listing:
        print("TTTTTTTTTTT",i)
        get_another_dict={}
        val_fetch_list=[]
        val_fetch_list=i.split("&&")
        #val_fetch_list.replace("(","")
        print("val_fetch_list",val_fetch_list)
        brack_list=["(",")"]'''
    if(input.endswith(")")):
        break