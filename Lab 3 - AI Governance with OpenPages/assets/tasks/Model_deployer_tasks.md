# 🧑‍🔬 AIOps Engineer – Deploy and Track Model in Production

> ⚠️ **Note:** Log in with the **AIOps Engineer** or **AI Engineer** role before accessing deployment tools.

---

# 🔑 Accessing Project Deployment Tools

1. Log in to **IBM Cloud**.
   

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model02.png">

 
2. From the **Hamburger Menu (☰)**, navigate to **Projects**.


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model20.png">


3. Click **View All Projects**.
   

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model22.png">


4. Select **HR Process Automation Project**.  


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model23.png">


---

# 🎯 Deployment Responsibilities

As a **Model Deployer**, your primary responsibilities include:

- **Asset Management**  
  Promote and manage AI assets (prompts, models) to the correct deployment space.  

- **Deployment**  
  Configure and launch assets in production with proper naming and optional descriptions.  

- **Monitoring**  
  Track deployed AI in the **AI Use Case** view to ensure correct operation and performance.  

- **Documentation**  
  Review **AI Factsheets** to validate asset metadata, lineage, and compliance.  



---

# 🔍 Deployment Steps

## 1️⃣ Promote Asset to Deployment Space

1. Navigate to **Assets** → **Asset Types** → **Prompts** -> Locate **Agentic RAG Testing Detached Prompt**.

   
<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model24.png">


  
2. Click the **3-dot menu** on the asset → select **Promote to Space**.

   
<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model27.png">

     
3. Choose the **space you created initially** or you can create new space as **Production** deployment stage. - [Steps for creating Deployment Space](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/Instructions/deploy-project.md)
   

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model28.png">


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model29.png">

   
4. Click **Promote**.

   
<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model30.png">

    
5. Confirm the asset is now **promoted to the deployment space**.
   

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model31.png">  


---

## 2️⃣ Deploy Asset

1. In the deployment space, click the **3-dot menu** on the promoted asset → select **Deploy**.


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model32.png">  


2. Enter a **name** for the deployment, optionally, add a **description**.


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model32.png">  

  
 
3. Click **Deploy**.


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model33.png">  

 
4. Click on Create.Your **Agentic RAG asset** is now **running in production**.


<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model34.png">  
  



---

## 3️⃣ Track and Monitor Deployment

1. Click the **AI Factsheet** next to the **Deployment** tab.
   

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model35.png">  


2. Review **asset metadata**, **performance**, and **compliance information**.
    

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model36.png"> 


3. Click **Track in AI Use Case** to monitor the deployed AI in context.
     

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model37.png"> 




---

# ✅ Summary

Following these steps ensures:

- AI assets are correctly promoted to the proper deployment space.  
- Deployed models are operational and accessible in production.  
- Asset metadata and performance are transparent through **AI Factsheets**.  
- You can monitor and track AI effectively in the **AI Use Case** view.  

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

# 🎉 Congratulations!

By deploying and tracking your **Agentic RAG prompt**, you ensure **reliable, compliant, and production-ready AI services** for HR process automation!  

