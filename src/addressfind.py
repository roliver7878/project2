import pycep_correios

def find(cepcodevalue):
    # explica aqui o que È os correios e que essa api È fornceida por eles de graÁa
    completeaddress = pycep_correios.get_address_from_cep(cepcodevalue)
    
    # os cÛdigos abaixo mostra no console o resultado como funcionalidade de log
    print(completeaddress['logradouro'])
    print(completeaddress['bairro'])
    print(completeaddress['cidade'])
    print(completeaddress['uf'])
    print(completeaddress['cep'])
   
    return completeaddress

