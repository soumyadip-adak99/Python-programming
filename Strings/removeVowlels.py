def method_1(input_str):
    restul = [] 
    for i in range(len(input_str)):
        ch = input_str[i]
        if (ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' 
            or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U'):
            continue
        else:
            restul.append(ch)
             
    print(''.join(restul)) 


def method_2(input_str):
    result = []
    
    for ch in input_str:
        if ch in 'aeiouAEIOU':
            continue
        else:
            result.append(ch)
            
    print(''.join(result))
    
def method_3(input_str):
    result = []
    
    vowles = set('aeiouAEIOU')
    
    for ch in input_str:
        if ch not in vowles:
            result.append(ch)
            
    print(''.join(result))
  
  
if __name__ == "__main__":
    input_string ="kamon acho"
    method_1(input_string)
    method_2(input_string)
    method_3(input_string)
        