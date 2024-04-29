import cv2
import numpy as np
from keras.models import load_model
from skimage.transform import resize, pyramid_reduce
from PIL import Image
import Time

model = load_model('CNNmodel.h5')

def prediction(pred):
    return(chr(pred+ 65))

def keras_predict(model,image):
    data = np.asarray(image, dtype="int32")

    pred_probab = model.predict(data)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class

def keras_process_image(img):
    image_x = 28
    image_y = 28
    img = cv2.resize(img, (1,28,28), interpolation = cv2.INTER_AREA)

    return img

def crop_image(image, x, y, width, height):
    return image[y:y + height, x:X + width]

def main():
    l=[]

    while True:

        cam_capture = cv2.VideoCapture(0)

        _, image_frame = cam_capture.read()

        im2 = crop_image(image_frame, 300, 300, 300, 300)
        image_grascale = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

        image_grascale_blurred = cv2.GaussianBlur(image_grayscale, (15,15), 0)
        im3 = cv2.resize(image_grascale_blurred, (28,28), interpolation = cv2.INTER_AREA)

        im4 = np.resize(im3, (28, 28, 1))
        im5 = np.expand_dims(im4, axis=0)

        pred_probab, pred_class = keras_predict(model, im5)
        print(pred_class, pred_probab)
        curr = chr(pred_class+ 65)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_frame, curr, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)


        cv2.rectangle(image_frame, (300, 300), (600, 600), (255, 255, 00), 3)
        cv2.imshow('video, image_frame')

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()