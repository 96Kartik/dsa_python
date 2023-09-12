# Given a set of N jobs where each jobi has a deadline and profit associated with it.
# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. 
# We earn the profit associated with job if and only if the job is completed by its deadline.
# Find the number of jobs done and the maximum profit.
# Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

# Example 1:
# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).
# ######################
# Example 2:
# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).

import heapq    

#Function to find the maximum profit and the number of jobs done.
def jobScheduling(Jobs,n):
    jobs_list = list(Jobs)
    jobs_list.sort(key=lambda x: x[1])

    max_heap = []
    max_profit = 0
    job_order = []
    for i in range(n - 1, -1, -1):
        if i == 0:
            slots_available = jobs_list[i][1]
        else:
            slots_available = jobs_list[i][1] - jobs_list[i - 1][1]
        
        heapq.heappush(max_heap, (-jobs_list[i][2], jobs_list[i][1], jobs_list[i][0]))
        while slots_available > 0 and len(max_heap) > 0:
            (profit, deadline, job_id) = heapq.heappop(max_heap) 
            max_profit += -profit
            job_order.append(job_id)
            slots_available -= 1
    
    return {"max_profit": max_profit, "job_order": job_order}

# Runner Code

test_jobs_set_1 = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
test_jobs_set_2 ={(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}

print("########### Job Scheduling Problem Test Cases ############")
print("Input: ", test_jobs_set_1)
print("Output: ", jobScheduling(test_jobs_set_1, len(test_jobs_set_1)))
print("#########")
print("Input: ", test_jobs_set_2)
print("Output: ", jobScheduling(test_jobs_set_2, len(test_jobs_set_2)))
