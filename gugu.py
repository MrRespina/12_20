startDan = int(input("시작 단 수 :"))
endDan = int(input("끝낼 단 수 :"))
startGop = int(input("시작 곱 수 :"))
endGop = int(input("끝낼 곱 수 수 :"))
while startDan <= endDan: 

    gop = startGop
    while gop <=endGop:
        
        print(f'{startDan} * {gop} = {startDan * gop}')
        gop += 1
        
    print('*'*30)
    startDan += 1