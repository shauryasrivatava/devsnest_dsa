class Solution(object):
    def groupAnagrams(self, strs):

        hashmap={}
        res=[]
        for i in strs:
            word=''.join(sorted(i))
            if word not in hashmap.keys():
                hashmap[word]=[i]
            else:
                hashmap[word].append(i)

        for j in hashmap:
            res.append(hashmap[j])
        return res
