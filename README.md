# Pet Weight Management System

**A smart, interactive system to manage and monitor the weight and feeding schedules of your pets efficiently.**

## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- Azure IoT Central

## Problems You Are Trying to Solve
Pet owners often struggle with maintaining the optimal weight and health of their pets. This project aims to solve:
- Continuous monitoring of pet weight and food intake.
- Providing feeding advice based on pet breed and current weight.
- Creating and saving feeding plans for pets.
- Visualizing pet weight data over time.

## How to Run
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up the virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root directory.
   - Add the following environment variables to the `.env` file:
     ```plaintext
     AZURE_IOT_CONNECTION_STRING=<your_azure_iot_connection_string>
     GOOGLE_API_KEY=<your_google_api_key>
     ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. **Upload your CSV files:**
   Ensure that the CSV files for pet weight and feeding schedules are in the correct directory paths as specified in the `app.py`.

## Reflections
This project was an excellent opportunity to integrate multiple technologies and create a comprehensive solution for pet weight management. It brought together IoT, data visualization, cloud services, and AI to address a common problem faced by pet owners.

## What You Learned
- How to integrate Streamlit for creating interactive web applications.
- Data visualization techniques using Pandas and Plotly.
- Integrating with cloud services like Azure IoT Central and AWS.
- Handling CSV file uploads and processing them for data visualization.
- Using environment variables for managing sensitive information.

## What Questions/Problems Did You Face?
- **File Accessibility**: Ensuring that the files were accessible in different environments, especially after deploying to Streamlit Sharing.
- **Data Handling**: Correctly handling and plotting the data from the CSV files, ensuring that the data types and column names were consistent.
- **API Integrations**: Integrating with multiple APIs and services, managing authentication, and handling responses effectively.
