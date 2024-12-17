class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        counts = [0]*26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        
        largest_chars = [-(i+1) for i in range(26) if counts[i] != 0] #one based indexing to allow for ordering
        heapq.heapify(largest_chars)
        
        ans = ""
        waiting = -1
        
        while largest_chars:
            first_largest = -heapq.heappop(largest_chars) - 1
            
            #use up first largest as much as we can
            repeat = 0
            while repeat < repeatLimit and counts[first_largest] > 0:
                ans += chr(ord('a') + first_largest)
                repeat += 1
                counts[first_largest] -= 1
            
            #no more of firt largest
            if counts[first_largest] == 0:
                continue
            #otherwise we can break this wit the second largest
            else:
                if not largest_chars:
                    return ans
                second_largest = -heapq.heappop(largest_chars) - 1
                ans += chr(ord('a') + second_largest)
                counts[second_largest] -= 1
                
                #add back in
                if counts[second_largest] > 0:
                    heapq.heappush(largest_chars, -(second_largest + 1))
                    
                #dont forget first largest
                heapq.heappush(largest_chars, -(first_largest +1))
        
        
        return ans

        