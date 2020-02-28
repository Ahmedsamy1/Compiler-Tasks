def calc(inp, transitions):
    statesStack = []
    currentState = '0'

    for i in inp:
        currentState = transitions[currentState][int(i)]
        statesStack.insert(0, currentState)

    return statesStack


# dfa = '0,0,1,00;1,2,1,01;2,0,3,10;3,3,3,11#0,1,2'
# dfa = '0,0,1,000;1,0,1,111#1'
# dfa = '0,0,3,000;1,2,3,001;2,2,4,010;3,1,4,011;4,2,4,100#2,4'
# dfa = '0,1,0,11;1,1,2,10;2,1,3,01;3,1,0,00#2,3'
dfa = '0,1,0,00;1,1,2,01;2,3,2,10;3,3,3,11#1,2'

dfa = dfa.split('#')

description = dfa[0].split(';')
acceptedStates = dfa[1].split(',')
transitions = {}
stateNames = {}

while True:
    resultStr = ''

    for i in range(len(description)):
        tran = []
        descriptionSplit = description[i].split(',')
        tran.append(descriptionSplit[1])
        tran.append(descriptionSplit[2])
        stateNames[str(i)] = descriptionSplit[3]
        transitions[str(i)] = tran

    inp = input("Please enter the test string: ")

    while True:
        statesStack = calc(inp, transitions)
        nextString = ''

        foundAccepted = False
        for i in range(len(statesStack)):
            if statesStack[i] in acceptedStates:
                resultStr += stateNames[statesStack[i]]
                foundAccepted = True
                break
            else:
                nextString = inp[-i - 1] + nextString

        if nextString == '' and foundAccepted:
            break
        if not foundAccepted:
            resultStr += stateNames[statesStack[0]]
            break
        inp = nextString
    print(resultStr)
