# Model Lifecycle Process

<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model97.png">


---

## 1. Model Developer Stage

### Step 1: Assign Users
- In the governance console, assign relevant users to the model:
  - **Assignee:** Model Developer
  - **Role:** Responsible for developing and updating the model
- Ensure all access permissions are correctly set.


<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model92.png">

---

### Step 2: Start Model Lifecycle
- Navigate to your **Detached Prompt Asset** in the governance console.
- Click on **Actions** → **Start Model Lifecycle**.


<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model93.png">

---


### Step 3: Submit for Validation
- After verification, click **Actions** → **Submit for Validation**.
- The model is now ready for validation by the assigned validation team.


<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model94.png">
---

## 2. Validation Stage

### Step 1: Assign Users
- Assign the **Validation Team** as assignees in the governance console.
- Their role is to review the model and ensure it meets required standards.


<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model95.png">

---

### Step 2: Perform Validation
- The validation team checks:
  - Accuracy
  - Compliance
  - Performance
- Once completed, mark the model as **Submit for final approval**.


<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Valid10.png">

---

## 3. Production Stage

### Step 1: Assign Users
- Assign **Business Unit Leader** as assignees in the console.
- Their role is to deploy the validated model and monitor production performance.


<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model91.png">

---

### Step 2: Deploy Model
- Once validation is complete, the production team deploys the model.
- Monitor performance and log issues as necessary.

 
[Production Step 2 Screenshot](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/assets/hands_on_lab_images/.png)

---

### Notes
- Always ensure the correct assignees are added at each stage.
- Screenshots should capture each action step clearly for reference.
- This lifecycle ensures traceability from development to production.

