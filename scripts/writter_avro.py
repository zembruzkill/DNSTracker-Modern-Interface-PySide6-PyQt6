import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

class AvroWriter():
    def __init__(self, schema_file: str, output: str) -> None:
        self.schema_file = schema_file
        self.output = output
        self.schema = avro.schema.parse(open(os.path.join(base_dir, self.schema_file), "rb").read())
        
    def write(self, data: dict) -> None:
        print("write", data)
        writer = DataFileWriter(open(os.path.join(base_dir, self.output), "a+b"), DatumWriter(), self.schema)
        writer.append(data)
        writer.close()
    
    def read(self) -> None:
        reader = DataFileReader(open(os.path.join(base_dir, self.output), "rb"), DatumReader())
        for record in reader:
            print(record)
        reader.close()
        
avrow = AvroWriter('../avro_files/schema.avsc', '../avro_files/collections/queries.avro')
avrow.read()