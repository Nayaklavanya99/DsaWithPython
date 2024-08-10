from jovian.pythondsa import evaluate_test_case

def test_location(cards,query,mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1>=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def binarySearch(cards,query):
    lo,hi = 0,len(cards)-1

    while lo <= hi:
        mid = (lo+hi)//2
        result = test_location(cards,query,mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi=mid-1
        elif result == 'right':
            lo=mid+1

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
