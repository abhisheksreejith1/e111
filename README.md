model = load_model("deepfake_model.h5")

img = preprocess_image("input.jpg")
prediction = model.predict(img)

if prediction > 0.5:
    print("Fake Image Detected")
else:
    print("Real Image")
    
