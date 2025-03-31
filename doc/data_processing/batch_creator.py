from dataproc.core import BatchCreator

values = {"amp": 5., "freq": 11, "duration": 5., "noise": .1}

batch = BatchCreator(metadata = values)
batch.create_data(ntests=11)
batch.to_csv(workdir = "./data/")
batch.dump_metadata(workdir = "./data/")
