Video KYC with Llama2, YOLOv8, and EasyOCR
This project creates an innovative Video KYC (Know Your Customer) solution powered by advanced AI techniques. The core components are:

Llama2 70B (Finetuned): A conversational AI model finetuned on KYC dialogues for natural interaction with users.
YOLOv8: A state-of-the-art object detection model for identifying and extracting relevant areas from identity documents.
EasyOCR: A powerful optical character recognition (OCR) engine for converting images of IDs into machine-readable text.
Key Features
Enhanced User Experience: Conversational guidance powered by Llama2 streamlines the KYC process.
Accurate Document Analysis: YOLOv8 effectively locates important sections on ID cards, and EasyOCR reliably extracts the text.
Secure Verification: Extracted details are displayed on a front-end interface where the user confirms their accuracy before final KYC approval.
Project Structure
models/: Contains the finetuned Llama2 model, YOLOv8 configuration, and pre-trained EasyOCR weights.
scripts/: Includes scripts for data processing, model training/finetuning, and inference.
frontend/: Contains the UI for displaying extracted details and user confirmation.
backend/: Handles API calls, data storage, and generation of confirmation IDs.
Installation
Clone the Repository:
Bash
git clone https://github.com/your-username/video-kyc.git
Use code with caution.
Install Dependencies:
Bash
cd video-kyc
pip install -r requirements.txt 
Use code with caution.
Usage
Data Preparation: Collect KYC video recordings and corresponding ID documents. Preprocess if necessary.
Model Finetuning (Optional): If necessary, finetune the Llama2 model on your KYC conversational dataset.
Run Inference: Use the provided scripts to run the model pipeline:
Conversation: Llama2 interacts with the user.
Detection: YOLOv8 identifies ID areas in video frames.
OCR: EasyOCR extracts text.
Front-end Display: Present the extracted information for user confirmation.
Verification and Confirmation: Upon user approval, submit the data to the backend for KYC verification and generate a confirmation ID.
Contributing
We welcome contributions! To get started:

Fork the repository.
Create a feature branch.
Make your changes and submit a pull request.
License
This project is licensed under the MIT License: https://opensource.org/licenses/MIT (or another license of your choice).

Disclaimer: Please ensure that your use of these AI models complies with all applicable laws and regulations, particularly those concerning data privacy and customer identification.
