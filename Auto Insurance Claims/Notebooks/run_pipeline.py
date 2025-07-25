import os
import subprocess
from datetime import datetime

# Step 0: Install required packages
requirements_file = "./requirements.txt"

if os.path.exists(requirements_file):
    print("📦 Installing required packages...")
    subprocess.run(["pip", "install", "-r", requirements_file])
else:
    print("⚠️ No requirements.txt found, skipping installation step.")

# Step 1: Define the pipeline
# List of notebooks to run in order

import papermill as pm
notebooks = [
    "01_Data_Preprocessing.ipynb",
    "02_Feature_Engineering_SD.ipynb",
    "03_NLP_Modeling.ipynb",
    "04_XGBoost_SD.ipynb",
    "05_Meta_Model.ipynb",
    "06_Evaluation.ipynb",
    "07_Deployment.ipynb",
    "08_SHAP.ipynb"
]

input_dir = "C:\\Users\\abdou\\Documents\\Data_Science_Projects\\AbdoulT_DSPortfolio\\Auto Insurance Claims\\Notebooks\\"
output_dir = os.path.join(input_dir, "outputs")
log_file = os.path.join(input_dir, "pipeline_error_log.txt")
os.makedirs(output_dir, exist_ok=True)

# Clear or create log file
with open(log_file, "w") as log:
    log.write(f"Pipeline Execution Log - {datetime.now()}\n\n")

# Run each notebook and log errors
for nb in notebooks:
    input_path = os.path.join(input_dir, nb)
    output_path = os.path.join(output_dir, f"OUT_{nb}")
    
    try:
        print(f"▶️ Running: {nb}")
        pm.execute_notebook(
            input_path=input_path,
            output_path=output_path
        )
        print(f"✅ Completed: {nb}")
    except Exception as e:
        error_message = f"❌ Failed: {nb}\n⚠️ Error: {str(e)}\n\n"
        print(error_message)
        with open(log_file, "a") as log:
            log.write(error_message)    
        continue  # go to the next notebook regardless of failure