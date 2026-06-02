# 📊 Creating Use Cases in watsonx.governance

> ⚠️ **Login Note:** Before starting, ensure you are logged into **IBM Governance Console** with the **Use Case Owner** role.
> This is required to create and manage Model Use Cases and associated risk/compliance workflows.

---

## 📌 What is a  Use Case?

A **Use Case** in IBM Governance Console is used to document and govern one or more models developed to fulfill a specific business objective. It acts as a centralized record for model development, compliance, risk tracking, and approval workflows.

> ✅ **A Use Case should be created whenever there's a business requirement that needs one or more AI/ML assets (e.g., models, prompts, or agents).**

---

## 🎯 Why Create a Use Case?

Creating a Use Case helps:

* Centralize governance of related models.
* Manage risks, compliance requirements, and ownership in one place.
* Track model performance and approvals across the model lifecycle.
* Link models to Business Entities for traceability and audit readiness.

---

## 🛠️ Step-by-Step Guide to Create a Use Case

### 1️⃣ Navigate to the Use Case Section

* Log in to IBM OpenPages as **Model Owner**.
* Click on the **Hamburger Menu (☰)**.
* Go to **Inventory**.
* Select **Use Case**.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase16.png">

---

### 2️⃣ Click **“Create New”**

* Click the **Create New** button at the top of the Use Case list view.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase2.png">

---

### 3️⃣ Fill in the Required Fields

Fill in the form using the following example:

| Field                       | Example Entry                                   |
| --------------------------- | ----------------------------------------------- |
| **Name**                    | AskHR Automation using Agentic AI               |
| **Owner**                   | Use Case Owner                                     |
| **Purpose**                 | Automate HR processes using Generative AI.      |
| **Description**             | This use case tracks GenAI-based HR automation. |
| **Primary Business Entity** | Techcorp                                        |

> ⚠️ All required fields must be completed before you can save.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase5.png">

---

### 4️⃣ Save the Use Case

* Click **Save** to create and register the Use Case record.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase17.png">

---

### 5️⃣ Set the Risk Level

After saving:

* Open the newly created Use Case.
* Scroll down to the **Risk** section.
* Select an appropriate **Risk Level** (Low, Medium, or High).
* Click **Save** again.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase4.png">

---

## ✅ Example Use Case Summary

| Field               | Value                                    |
| ------------------- | ---------------------------------------- |
| **Name**            | AskHR Automation using Agentic AI        |
| **Owner**           | Use Case Owner                              |
| **Purpose**         | Automate HR tasks using Generative AI    |
| **Description**     | Tracks GenAI model for internal HR tasks |
| **Business Entity** | Techcorp                                 |
| **Risk Level**      | Medium (adjust as needed)                |

After setting the risk level Go on action tab and click on **Submit for initial approval**

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase6.png">

### 6️⃣ Navigate to the Questionnaire Assesment section

* Click on the **Hamburger Menu (☰)**.
* Go to **Assesment**.
* Select **Questionnaire Assessment**.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase7.png">  


### 7️⃣ Complete Risk Assessment

In the Questionnaire Assessment page,

* Click on the Risk Assessment associated with the Use Case.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase8.png">  

* Fill out all required questions in the Risk Assessment Questionnaire, such as:

  a.What type of data is being used?

  b.Is the Use Case customer-facing?

  c.What is the impact of a model failure?

  d.What mitigations are in place?

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase9.png">   

* Use dropdowns, radio buttons, and text fields as applicable.

* Click **Submit and close** on Actions tab once all questions are answered.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase10.png"> 

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase11.png">  

### 8️⃣ Complete Compliance Assessment

In the Questionnaire Assessment page,

* Click on the Compliance Assessment associated with the Use Case.(EU AI ACT)

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase12.png">  

* Fill out all required questions in the Risk Assessment Questionnaire, such as:

  a.Is the Use Case subject to regulations (e.g., GDPR, HIPAA)?

  b.Has a Data Protection Impact Assessment (DPIA) been completed?

  c.Is cross-border data transfer involved?

  d.Are legal and data retention policies in place?

**Note**: 

👉 For most questions, select “Yes” if the risk or control is applicable. This ensures the risks get assigned and mapped properly in the assessment.
👉 Use “No” only when the risk or control clearly does not apply.
👉 If unsure, check the guidance notes or consult your risk team before leaving a field blank.
👉 Always review the final list of risks assigned after submission to confirm they reflect your business process.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase13.png">  

* Use dropdowns, radio buttons, and text fields as applicable.

* Click **Submit and close** on Actions tab once all questions are answered.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase14.png">  

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase15.png">  


✅ Once both assessments are submitted, the risks will be assigned for the use case.

- After the assesments Go back to your use case there you can See Risks associated in **Risk** List Section:

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model50.png"> 

- In the use case In **regulatory information** section Go to **mandates** tab and click on **Add**

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase51.png"> 

- Select appropriate **Mandates or Risk & Compliance Act** and associate to the use case.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase52.png"> 

-Now you can see in **mandates** section **Mandates or Risk & Compliance Act** are added.

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/usecase53.png"> 


Now you can proceed to the Risk assesment process by clicking on below link:

* [Review and Assess Risk](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/assets/tasks/risk_review_rco.md)


---

## 🎉 Well Done!

You have successfully created a **Model Use Case** and filled assesments in Watsonx.governance.

This enables:

* Structured governance
* Risk and compliance tracking
* Streamlined collaboration across stakeholders

Use Cases provide visibility, traceability, and control across the lifecycle of AI models.

---
