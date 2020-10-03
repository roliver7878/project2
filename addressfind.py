import pycep_correios

def find(addresscode):
    completeaddress = pycep_correios.get_address_from_cep(addresscode)

    print(completeaddress['logradouro'])
    print(completeaddress['bairro'])
    print(completeaddress['cidade'])
    print(completeaddress['uf'])
    print(completeaddress['cep'])

    return completeaddress


