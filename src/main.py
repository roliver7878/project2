import addressfind
import addresstotext
import converttoaudio


# This is my main method
def main():
    # here we ask for postalCode from user
    cepcodevalue = input('Write here your postal code: ')
    # the function above send the postalcode writed by User
    # addressfind use a free api for serach the address by postalcode
    completeaddress = addressfind.find(cepcodevalue) 
    # function above convert ( parse ) the Json Address to text
    # this text returned will used to converted in audio 
    text = addresstotext.totext(completeaddress)
    # at last, the text is converted in audio
    converttoaudio.convert(text)


if __name__ == "__main__":
    main()
