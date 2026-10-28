from abc import ABC, abstractmethod

class AIModel(ABC):
    @abstractmethod
    def predict(self, data):
        pass
class TextModel(AIModel):
    def predict(self, data):
        return f"Processing Text: {data}"
class ImageModel(AIModel):
    def predict(self, data):
        return f"Processing Image: {data}"
class ModelManager:
    def __init__(self, model):
        self.model = model
    def run(self, data):
        return self.model.predict(data)

# textmodel = TextModel()
# print(textmodel.predict("Hello AI"))
# imagemodel = ImageModel()
# print(imagemodel.predict("photo.png"))
# madelmanager = ModelManager()
# print(madelmanager.run("AI Engineer"))                                
text_model = TextModel()
image_model = ImageModel()

text_manager = ModelManager(text_model)
image_manager = ModelManager(image_model)

print(text_manager.run("AI Engineer"))
print(image_manager.run("photo.png"))