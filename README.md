# CV module: face-classifier

This module for OpenCV uses a simple classifier function of the given recognizer object to classify an image.

## Usage

```python
classify(recognizer, image)
```

- `recognizer`: The given [OpenCV recognizer](https://docs.opencv.org/master/d4/d48/namespacecv_1_1face.html).
- `image`: The image of **a face** that has to be classified. 

## Return

```python
return label, confidence
```

- `label`: The label info as string.
- `confidence`: The confidence percentage of the recognition.
