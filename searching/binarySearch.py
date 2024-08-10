from jovian.pythondsa import evaluate_test_case



def binarySearch(cards,query):
    lo,hi = 0,len(cards)-1

    while lo < hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid-1
        elif mid_number > query:
            lo = mid+1

    return -1
            
test = {
    "input":{
        'cards':list(range(10000000,0,-1)),
        'query': 2},
    "output": 9999998
}         


test1 = {
    "input":{
        'cards': [13,11,7,7,4,3,1,0],
        'query': 7},
    "output": 2
}
evaluate_test_case(binarySearch,test)
