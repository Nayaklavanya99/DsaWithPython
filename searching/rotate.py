from jovian.pythondsa import evaluate_test_cases

def count_rotation(nums):
    pos=1
    while(pos < len(nums)):
        if(pos >0 and nums[pos] < nums[pos-1] ):
            return pos
        pos +=1

    return 0

test_cases = [
    {'input':{'nums' : [19,25,29,3,5,6,7,9,11,14]  },'output': 3},
    {'input':{'nums' : [4,5,6,7,8,1,2,3]  },'output': 5},
    {'input':{'nums' : [1,2,3,4,5]  },'output': 0},
    {'input':{'nums' : [7,3,5]  },'output': 1}
              
]
evaluate_test_cases(count_rotation,test_cases)