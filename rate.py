from ultralytics import YOLO
import sys

# Load your trained model
model = YOLO("best.pt")   # change path if needed

def rate_image(img_path):
    results = model.predict(img_path, verbose=False)[0]

    # predicted class name (example: "rating_4")
    cls_name = results.names[results.probs.top1]

    # Extract rating number from class name
    rating_number = int(cls_name.split("_")[-1])

    # confidence score
    confidence = float(results.probs.top1conf)

    return rating_number, confidence

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rate.py image_2.jpg")
        exit()

    img_path = sys.argv[1]

    rating, conf = rate_image(img_path)

    print(f"Predicted Rating: {rating} / 5")
    print(f"Confidence: {conf:.2f}")
