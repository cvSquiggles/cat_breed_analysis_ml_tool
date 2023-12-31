import tensorflow as tf
import tensorflow_hub as tfh
import numpy as np
import streamlit as st

form = st.form(key="user_form")

data_categories = ['Abyssinian',
                   'American Bobtail',
                   'American Curl',
                   'American Shorthair',
                   'Bengal',
                   'Birman',
                   'Bombay',
                   'British Shorthair',
                   'Egyptian Mau',
                   'Exotic Shorthair',
                   'Maine Coon',
                   'Manx',
                   'Norwegian Forest',
                   'Persian',
                   'Ragdoll',
                   'Russian Blue',
                   'Scottish Fold',
                   'Siamese',
                   'Sphynx',
                   'Turkish Angora',
                   ]

model = tfh.load('tmp\\cat_breed_model_efficientnetv2-xl-21k')


def preprocess_image(image):
    image = tf.image.resize(image, [512, 512])
    image = tf.cast(image, tf.float32) / 255.0
    return image


imgPath = form.text_input('Enter target image name from root of project folder', 'abyssinian_1.jpg')

if form.form_submit_button('Classify'):
    image = tf.keras.preprocessing.image.load_img(imgPath)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = preprocess_image(image)
    image = tf.expand_dims(image, axis=0)

    predictions = model(image)

    predicted_class = tf.argmax(predictions, axis=-1)
    score = tf.nn.softmax(predictions)

    #print('Cat in image is {} with accuracy of {:0.2f}'.format(data_categories[np.argmax(score)], np.max(score) * 100))

    img_height = 512
    img_width = 512

    st.image(imgPath)
    st.write('The cat in the image appears to be:  ' + (data_categories[np.argmax(score)]))
    st.write('With a confidence of: ' + (str(round((np.max(score) * 100), 2))))

    st.write('__________________________________________________________________________________________________________')

    st.write('cat_breed_model_efficientnetv2-xl-21k loss:')
    st.write('(Blue = Training; Orange = Validation)')
    st.image("loss.png")

    st.write('cat_breed_model_efficientnetv2-xl-21k accuracy:')
    st.write('(Blue = Training; Orange = Validation)')
    st.image("accuracy.png")
