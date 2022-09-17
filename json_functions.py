import json

class json_functions:

    def __init__(self) -> None:
        pass
        
    def open_json(self,localisation):
        with open(f"./{localisation}.json") as file:
            self.temp_dict = file.read()
            self.dict = json.loads(self.temp_dict)
            return self.dict

    @staticmethod
    def save_json(localisation,data)->None:
        json_object = json.dumps(data, indent=4)
        with open(f"{localisation}.json", "w") as outfile:
            outfile.write(json_object)
        pass

