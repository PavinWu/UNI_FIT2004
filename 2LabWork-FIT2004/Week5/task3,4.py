def best_job(job_matrix):
    """
    job_matrix contains three columns: [start_time, end_time, profit]
    Each row corresponds to a single job.
    
    start time is sorted
    """
    max_profit = [job_matrix[0][2]]     # first job's profit
    optimal_profit = 0
    optimal_profit_i = 0
    for i in range(1, len(job_matrix)):
        # max job profit without overlaps
        possible_profit = 0
        crnt_max_past_profit = 0
        crnt_start_time = job_matrix[i][0]
        for i_earlier_job in range(i-1, -1, -1):
            if crnt_start_time >= job_matrix[i_earlier_job][1]:    # if not overlap
                if job_matrix[i_earlier_job][2] >= crnt_max_past_profit:    # find max amongst past profits
                    possible_profit += job_matrix[i_earlier_job][2]
                    crnt_max_past_profit = job_matrix[i_earlier_job][2]
                    crnt_start_time = job_matrix[i_earlier_job][0]
            # In this step we search through all available past "valid" (non-overlap start time) ...
            # solutions (maximum profit).
            # We won't need to search again recursively for past ones since a part of 
        
        max_profit.append(possible_profit + job_matrix[i][2])
        
        """
        # don't need this if we backtrack with max_profit list (our connection to the past)
        if optimal_profit <= max_profit[-1]:       # determine where the last max profit is
            optimal_profit = max_profit[-1]
            optimal_profit_i = len(max_profit)- 1  # can't store -1 since -1 always mean last    
        """
        
    optimal_profit = max(max_profit)
    
    return max_profit
    

def best_job_backtrack(job_matrix, max_profit_list):
    """
    
    #job_list = []
    #while i > 0:
    #    job_list.append(i+1)    # number of jobs start from 1, but index starts at 0
    Backtrack: store last i => from last i, search for max past valid job => 
                from last past valid job, search for the previous past valid job
                until reach 0 (or until ...): Is there a better way?
                (Does this way even work?)
    
    Remember how we use stored max to backtrack? Do we do the same here?
    
    Since start time is sorted, we don't have to worry about the job that's supposed to be 
    in the list, coming after the current max job.
    """
    job_list = []
    crnt_max_profit = max(max_profit_list)
    # crnt_max_start_time = job_matrix[-2][0]     # start time of 2nd last item is guaranteed to be latest but one.
    i = len(max_profit_list) - 1
    while i >= 0:
        if crnt_max_profit == max_profit_list[i]: 
            if len(job_list) == 0:
                crnt_max_start_time = job_matrix[i][0]
            else:
                if job_matrix[i][1] <= crnt_max_start_time:     # stop time <= largest start time (= so it takes last one too)
                    crnt_max_start_time = job_matrix[i][0]
            job_list.append(i + 1)    # job starts from 1, but index starts from 0
            crnt_max_profit -= job_matrix[i][2]    # portion of max_profit received from job i taken out
        i -= 1
    return reverse(job_list)
  
    
def reverse(list):
    """
    reverse a list
    """
    l = len(list) - 1
    #for i in range(len(list)):     # This will reverse twice => same thing!
    for i in range(len(list)//2):   # if odd, don't need to reverse middle. Otherwise, go.
        list[i], list[l - i] = list[l - i], list[i]
    return list
            

if __name__ == "__main__":
    job_matrix = [[1, 10, 50],
                  [8, 12, 100],
                  [10, 45, 100],
                  [18, 55, 150],
                  [50, 60, 50]]
    best_profit_list = best_job(job_matrix)
    print(best_profit_list)
    best_job_list = best_job_backtrack(job_matrix, best_profit_list)
    
    print("Number of jobs are:", end = ' ')
    for job in best_job_list:
        print(job, end = ' ')
    
                
