def totext(completeaddress):
    
    initialtext = "Hi. your search for the postalcode " + completeaddress['cep'] + "returned"
    streetname = "Street name is " + completeaddress['logradouro'] + ","
    suburbname = "Suburb name is " + completeaddress['bairro'] + ","
    cityname = "City name is " + completeaddress['cidade'] + "," 
    stateidentifier = "state identifier is " + completeaddress['uf']
    
    return initialtext + streetname + suburbname + cityname + stateidentifier
