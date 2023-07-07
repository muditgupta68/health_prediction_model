import streamlit as st
import joblib


def main():
    html_temp = """"
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:#232323;text-align:center">Health Insurance Cost Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('health_model_gbr')

    age = st.slider('Enter your age', 18, 100)
    st.write(age, 'years old')

    gender = st.selectbox(
        'Enter your Age',
        ('Male', 'Female'))
    
    genderSwitcher = {
        "Male": 0,
        "Female":1
    }    
    gender = genderSwitcher.get(gender)
    # st.write(gender)
    
    bmi = st.number_input('Enter your BMI')
    
    children = st.slider('Enter Number of children',0,4)
    
    smoke = st.selectbox(
        'Are you smoker',
        ('Yes', 'No'))
    
    smokeSwitcher = {
        'Yes':1,
        'No' :0
    }
    
    smoke = smokeSwitcher.get(smoke)
    # st.write(smoke)
    
    region = st.selectbox(
        'Region',
        ('North-East', 'North-West','South-East','South-West'))
    
    selectedRegion = [0.0,0.0,0.0]
    
    if region == 'North-East':
        selectedRegion = [0.0,0.0,0.0]
    elif region == 'North-West':
        selectedRegion = [1.0,0.0,0.0]
    elif region == 'South-East':
        selectedRegion = [0.0,1.0,0.0]
    else:
        selectedRegion = [0.0,0.0,1.0]
    
    # st.write(selectedRegion[0],selectedRegion[1],selectedRegion[2])
    
    if st.button('Predict Now'):
        prediction = model.predict([[age,gender,bmi,children,smoke,selectedRegion[0],selectedRegion[1],selectedRegion[2]]])
        print(prediction[0])
        
        st.success(f'Your Insurance Cost is Rs.{round(prediction[0],2)}')


if __name__ == '__main__':
    main()
