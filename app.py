# app.py
import streamlit as st
import os
import pandas as pd

# Function to plot data from CSV
def plot_data(file_path, chart_title):
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return
    
    df = pd.read_csv(file_path)
    st.write(f"{chart_title} DataFrame")
    st.write(df.head())  # Display the first few rows of the DataFrame to check the column names
    df.columns = ["Time", "Weight"]
    st.line_chart(df.rename(columns={"Time": "index"}).set_index("index")["Weight"])

# Main app
def main():
    st.title("Pet Weight Management")
    pages = ["Instruction", "Pet Daily Diagrams", "Pet Weight Management", "Feeding Plan"]
    page = st.sidebar.selectbox("Select a page", pages)

    if page == "Instruction":
        st.header("Instruction")
        video_path = "MultiPetfeeder.mov"
        if not os.path.exists(video_path):
            st.error(f"Video file not found: {video_path}")
        else:
            st.video(video_path)

    elif page == "Pet Daily Diagrams":
        st.header("Pet Daily Diagrams")

        # Load and plot CSV files for various weights
        file_paths = {
            "Bowl A Weight": "Bowl A Weight1.csv",
            "Bowl B Weight": "Bowl B Weight1.csv",
            "Pet A Weight": "Pet A Weight1.csv",
            "Pet B Weight": "Pet B Weight1.csv",
        }

        for chart_title, file_path in file_paths.items():
            st.subheader(chart_title)
            plot_data(file_path, chart_title)

    elif page == "Pet Weight Management":
        st.header("Pet Weight Management")
        pet_type = st.selectbox("Select pet type", ["Dog", "Cat", "Others"])

        if pet_type == "Dog":
            dog_breeds = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Beagle",
                          "Poodle", "Rottweiler", "Boxer", "Siberian Husky", "Chihuahua"]
            pet_breed = st.selectbox("Select dog breed", dog_breeds)
        elif pet_type == "Cat":
            cat_breeds = ["Ragdoll", "Siamese", "Birman", "Persian", "Maine Coon",
                          "British Shorthair", "Sphynx", "Abyssinian", "Bengal", "Russian Blue"]
            pet_breed = st.selectbox("Select cat breed", cat_breeds)
        else:
            pet_breed = st.text_input("Enter pet breed")

        current_weight = st.number_input("Enter current weight (kg)")
        expected_weight = st.number_input("Enter expected weight (kg)")

        if st.button("Get Feeding Advice"):
            with st.spinner("Generating AI-powered feeding advice..."):
                advice = "Sample feeding advice based on the given parameters."  # Replace with actual API call
            st.success("Here is your AI-generated feeding advice:")
            st.write(advice)

    elif page == "Feeding Plan":
        st.header("Feeding Plan")
        pet_name = st.text_input("Enter pet name")
        num_meals = st.number_input("Number of meals per day", min_value=1, value=3, step=1)

        feeding_plan = {}
        for i in range(int(num_meals)):
            meal_name = f"Meal {i+1}"
            quantity = st.number_input(f"{meal_name} quantity (grams)", min_value=0, value=0, step=1)
            release_time = st.time_input(f"{meal_name} release time")
            feeding_plan[meal_name] = {"quantity": quantity, "release_time": str(release_time)}

        if st.button("Save Feeding Plan"):
            feeding_plan_data = {
                "pet_name": pet_name,
                "feeding_plan": feeding_plan
            }
            st.success("Feeding plan saved successfully!")

if __name__ == "__main__":
    main()
