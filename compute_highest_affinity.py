# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo"). 
    user_dic = {}
    pair_dic = {}
    max_pair = ()
    max_num = 0
    '''
    if max_num == -1:
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
        max_num = 100
    '''

    for ind in range(len(user_list)):
        #if user_dic.has_key(user_list[ind]):
        if user_list[ind] in user_dic:
            for i in user_dic[user_list[ind]]:
                if site_list[i]!=site_list[ind]:
                    # curr pair
                    if site_list[ind] < site_list[i]:
                        curr_pair = (sit_list[ind], site_list[i])
                    else:
                        curr_pair = (site_list[i], site_list[ind])

                    if curr_pair not in pair_dic:
                        pair_dic[curr_pair] = set()
                    pair_dic[curr_pair].add(user_list[ind])
                    if len(pair_dic[curr_pair]) > max_num:
                        max_num = len(pair_dic[curr_pair])
                        max_pair = curr_pair
        else:
            user_dic[user_list[ind]] = [ind]        
    
        
    return max_pair
