
def classify(recognizer, image):

    label_id, confidence = recognizer.predict(image)

    label = recognizer.getLabelInfo(label_id)

    return label, confidence
