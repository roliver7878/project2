import addressfind
import converttoaudio

# This is my main method
def main():
  cepcodevalue = input("Write here your postal code: " )
  address = addressfind.find(cepcodevalue) 
  converttoaudio(address)

if __name__ == "__main__":
    main()
