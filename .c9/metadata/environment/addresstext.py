{"filter":false,"title":"addresstext.py","tooltip":"/addresstext.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["def totext(completeaddress):","    ","    initialtext = \"Hi. your search for the postalcode \" + completeaddress['cep'] + \"returned\"","    streetname = \"Street name is \" + completeaddress['logradouro'] + \",\"","    suburbname = \"Suburb name is \" + completeaddress['bairro'] + \",\"","    cityname = \"City name is \" + completeaddress['cidade'] + \",\" ","    stateidentifier = \"state identifier is \" + completeaddress['uf']","    ","    return initialtext + streetname + suburbname + cityname + stateidentifier",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":0},"end":{"row":9,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1601741191819,"hash":"16ee39341c674eee0e78d2f804c48e1dd2026bf1"}