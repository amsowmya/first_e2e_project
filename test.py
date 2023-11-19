from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj = CustomData(1.34,62.5,57.0,7.0,7.05,4.38,'Premium','G','SI2')

data = custdataobj.get_data_as_dataframe()
print(data)