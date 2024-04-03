from typing import List
from PIL import Image
from ultralytics import YOLO

class CaptchaSolver:
    # LETTERS: List[str] = ['A', 'B', 'C', 'D', 'E', 'F']
    LETTERS: List[str] = [0, 1, 2, 3, 4, 5]
    _image: Image.Image

    def __init__(self, image: Image.Image) -> None:
        self._image = image
    
    def predict(self) -> Image.Image:
        model = YOLO('training/models/margonemV3.pt')
        result = model.predict(self._image, conf=0.8) #add save=True, to save the predictions
        return result

    def get_answer(self, result) -> list:
        res = []
        for box in result[0].boxes:
            # print(int(box.cls.item()))
            data = box.data.tolist()[0]
            # print(data)
            center_x = (data[0] + data[2]) // 2
            center_y = (data[1] + data[3]) // 2

            # print(center_x, center_y)
            temp_x = 640//3
            total = 1
            while center_x > temp_x:
                total+=1
                temp_x += 640//3

            if center_y > 640//2:
                total = total+3
            
            if int(box.cls.item()) == 1: #checks if it's upsidedown (it's id 1)
                res.append(CaptchaSolver.LETTERS[total-1])
        return res