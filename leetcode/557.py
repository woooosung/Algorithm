class Solution:
    def reverseWords(self, s: str) -> str:
        output_list = []
        output_list = s.split()
        for i in range(len(output_list)):
            temp_list = list(output_list[i])
            for j in range(int((len(temp_list)+1)/2)):
                temp = temp_list[j]
                temp_list[j] = temp_list[len(temp_list)-1-j]
                temp_list[len(temp_list)-1-j] = temp
            output_list[i] = ''.join(temp_list)
        return ' '.join(output_list)