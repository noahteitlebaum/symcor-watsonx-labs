# 🛠️ Operations & Risk Team – Monitoring AI Use Case in Production

> ⚠️ **Note:** Log in with the **Operations & Risk Team** role before accessing monitoring and governance tools in Watsonx Governance.

---

# 🧑‍💻 Model Developer – AI Asset Deployment & Testing

> ⚠️ **Note:** Log in with the **Model Developer** role before accessing project assets, promoting prompts, and testing AI models.


### 🔹 Step 6: Monitor the Model in Production  

**Who:** Operations & Model Developer Team 

>[!Note]
> Now after **AIOps Engineer** will complete the deployment of asset in **Production Space** when get approval from **Buisness Unit Leader** he will involve Model developer in managing and monitoring **Agentic RAG Detached prompt** asset in Production.

-> AIOps Engineer - [Deployer_tasks](https://github.ibm.com/skol/ai-governance-client-bootcamp/edit/main/labs/risk-and-compliance/assets/tasks/Model_deployer_tasks.md)

->A fter completing [Deployer_tasks](https://github.ibm.com/skol/ai-governance-client-bootcamp/edit/main/labs/risk-and-compliance/assets/tasks/Model_deployer_tasks.md) AIOps engineer continue tracking deployed asset in AI Use case along with **Model Developer** in **Governance Console** by following below steps:
---

### Key Actions in Watsonx Governance

#### Track in AI Use Case

1. Now click on **Track in AI use case**  to associate asset to **AI Use case** click on **Go to AI Use cases** as project is not associated to **AI Use case** :


   
<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model51.png">



2. Select **AI Use case** created by **Use case owner** initially :



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model52.png">



3. Go to **Associated workspaces** section and Select **Operation** phase and click on **Associate Workspace**:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model53.png">



4. Here, Select  Deployment space created initially or if you have not created Click on **+New Space** and follow [Deployment Creation Steps](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/instructor/deploy-project.md) these steps for creating deployment space for **Production** Deployment stage. Click on Save:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model54.png">



5. Now **AI Use case** is associated to **project** and **deployment space**.In **Associated Workspaces** Section Click on Arrow beside **your project** under **Operation** phase:


    
<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model55.png">



#### Evaluate prompt template in **Production** Phase:

1. In project go to **Deployments** tab Click on **Agentic RAG Production** your deployment name:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model55.png">    



2. In Evaluation tab click on **Activate** to evaluate prompt template in **Production** phase:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model56.png">   



3. Choose the evaluation dimensions and select the test data:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model76.png">  


---

## Prerequisites

- IBM Cloud account with access to Watsonx.Governance
- Access to the pre-deployed Agentic RAG model
- Permissions to create and manage projects in Watsonx Studio
  
---

## Resources

- [IBM Cloud Platform](https://cloud.ibm.com/login)
- [Steps for creating Deployment Space](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/Instructions/deploy-project.md)

---


### ✅ Summary

- Monitoring in **Watsonx Governance** ensures AI models in production remain fair, high-quality, and reliable.  
- Alerts provide proactive oversight for risk and compliance.  
- Operations & Risk teams maintain transparency and governance of AI deployments.  
