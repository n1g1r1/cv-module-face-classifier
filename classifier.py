
def classify(recognizer, image):

    label_id, confidence = recognizer.predict(image)

    return label_id, confidence
