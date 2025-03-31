from src.demos.data_creation import DataCreator
from src.demos.recognize_amplitude_frequence import recognize_amplitude_frequence

###initialising variables
amp=1
freq=1
noise=0.01
duration=100.

####initialising class with variables
dc=DataCreator(amp,freq,noise,duration)

print(f"Initialising DataCreator with amp:{amp}, freq:{freq}, noise:{noise}, duration:{duration} \n Class:{dc}")

#Trying TO_CSV without create_data
#dc.To_CSV()

###Using method create_data
dc.create_data()

#print(dc.data)


###Using method TO_CSV to get the csv dataframe
dc.To_CSV()


Data=dc.data
#print(Data)
###

###Using function recognize_amplitude_frequence


from argparse import ArgumentParser

parser = ArgumentParser("Test")
parser.add_argument(
    "-i",
    "--input",
    type=str,
    dest="input",
    help="input csv",
    required=True,
    default="data.csv",
)

args = parser.parse_args()

Data_csv=args.input

recognize_amplitude_frequence(Data_csv)