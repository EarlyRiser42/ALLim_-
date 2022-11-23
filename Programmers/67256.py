def get_distance(keypad, num1, num2):
    distance = abs(keypad[num1][0]-keypad[num2][0]) + abs(keypad[num1][1]-keypad[num2][1])
    return distance

def solution(numbers, hand):
    keypad = {'1':(0,0), '2':(0,1), '3':(0,2),
              '4':(1,0), '5':(1,1), '6':(1,2),
              '7':(2,0), '8':(2,1), '9':(2,2),
              '*':(3,0), '0':(3,1), '#':(3,2)}
    answer = ''
    left, right = '*', '#'
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left = i
        elif i in [3,6,9]:
            answer += 'R'
            right = i
        else:
            left_distance = get_distance(keypad, str(left), str(i))
            right_distance = get_distance(keypad, str(right), str(i))
            if left_distance > right_distance:
                answer += 'R'
                right = i
            elif left_distance == right_distance:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
            else:
                answer += 'L'
                left = i
    return answer