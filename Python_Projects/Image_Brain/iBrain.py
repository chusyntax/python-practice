from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(
    execution_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()
