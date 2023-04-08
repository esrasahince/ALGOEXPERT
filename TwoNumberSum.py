def twoNumberSum(array, targetSum):
    array.sort();
    beginptr=0;
    lastptr=len(array)-1
    for i in range(len(array)):
        if array[beginptr]+array[lastptr]==targetSum:
            return [array[beginptr],array[lastptr]]
        if array[beginptr]+array[lastptr]>targetSum:
            lastptr-=1;
        else:
            beginptr+=1;
    return []   
  
