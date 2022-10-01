import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/User1/Desktop/xgbmodel.sav', 'rb'))


def corrosion_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'Grade A corrosion detected'
    elif (prediction[0] == 2):
        return 'Grade B corrosion detected'
    elif (prediction[0] == 3):
        return 'Grade C corrosion detected'
    else:
      return 'Grade D corrosion detected'


def main():
    # giving a title
    st.title('Corrosion Severity Level Predictor')

    # getting the input data from the user

    WeightLoss = st.text_input('Weight Loss(g) ')
    WeightLossPercentage = st.text_input('Weight Loss(%) ')
    ThicknessLoss = st.text_input('Thickness Loss(mm) ')
    ThicknessPercentage = st.text_input('Thickness Loss(%) ')

    # code for Prediction
    detection = ''

    # creating a button for Prediction

    if st.button('Corrosion Severity Level'):
        detection = corrosion_prediction(
            [WeightLoss, WeightLossPercentage, ThicknessLoss, ThicknessPercentage])

    st.success(detection)


if __name__ == '__main__':
    main()












# input_data = (6.44,10.210258,0.42,6.903887)
#
# # changing the input_data to numpy array
# input_data_as_numpy_array = np.asarray(input_data)
#
# # reshape the array as we are predicting for one instance
# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
#
# prediction = loaded_model.predict(input_data_reshaped)
# print(prediction)
#
# if (prediction[0] == 1):
#   print('Grade A corrosion detected')
# elif (prediction[0] == 2):
#     print('Grade B corrosion detected')
# elif (prediction[0] == 3):
#     print('Grade C corrosion detected')
# else:
#   print('Grade D corrosion detected')