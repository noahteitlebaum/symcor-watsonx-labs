# Model Developer's Lab for AI Governance

## Overview

This repository contains the Model Developer's lab for AI Governance, focusing on automating HR policy question/answering processes using IBM watsonx **AutoRAG** capabilities.

## 1. Use Case

**Business Goal:** Automate question/answering process from HR policies using IBM watsonx **AutoRAG**, enabling faster, bias-free hiring while maintaining compliance in OpenPages.

### 🧠 Agentic RAG Capabilities for HR Policy Q&A:

1. Ingest and index HR policy documents (PDFs, DOCX, web pages, internal knowledge bases)
2. Allow users to ask natural language questions about HR policies (e.g., leave, benefits, conduct, compliance)
3. Retrieve relevant policies using semantic search
4. Generate clear, accurate answers grounded in official HR documentation
5. Highlight source references to support transparency and traceability
6. Support multilingual queries and inclusive language understanding

> **Note:** The Agentic RAG model for this use case is **already created and deployed** in the pre-production environment.

---

## 2. Persona

**Model Developer:** Responsible for accessing the deployed Agentic RAG model, running evaluations, and integrating outputs into OpenPages.

---

## 3. Step-by-Step OpenPages Flow

### **Step 1 – Access the Deployed Agentic RAG Model**

The Agentic RAG model is already developed and deployed. To access it:

1. Log in to the **[IBM Cloud](https://cloud.ibm.com/login)** platform.

<img width="800" alt="IBM Cloud Login" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model1.png">

2. Open **hamburger menu → Resource List → watsonx.governance**
   
<img width="800" alt="Watsonx Governance Navigation" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model2.png">

3. Click the **Launch in watsonx.governance** button — this navigates to:
   [https://dataplatform.cloud.ibm.com/wx/home?context=wx](https://dataplatform.cloud.ibm.com/wx/home?context=wx)
   
<img width="800" alt="Launch watsonx.governance" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model3.png">

4. On the **watsonx Studio** homepage:
   
* Create a new project as explained in the steps linked here: [Steps for creating project](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/instructor/create-project.md)
  
* After creating the project, go to the **Assets** tab and click on **New Asset**:
  
<img width="800" alt="New Asset Creation" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model13.png">

* Select **Working with data or models in Python or R notebooks** from the **All** option on the sidebar:
  
<img width="800" alt="Notebook Selection" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model14.png">

* Go to the **local file** tab and click **browse** to upload the notebook linked here as a local file: [Notebook](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/assets/agentic-rag.ipynb)
  
<img width="800" alt="File Upload" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model15.png">

* Select the [Notebook](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/assets/agentic-rag.ipynb), download it locally, and upload it to the watsonx.ai runtime.
  
<img width="800" alt="Notebook Upload" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model16.png">

* After uploading, provide a name to the notebook and click the **Create** button:
  
<img width="800" alt="Notebook Creation" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model17.png">

* The notebook will now be ready to run and **create a Detached Prompt Template for Agentic RAG** in the OpenScale dashboard UI

-> In this notebook:

- Use **watsonx_api_key** created initially [Create API key](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/instructor/create-api-key.md)
- Access **project_id** by navigating: hamburger menu → projects → view all projects → your project-> Manage tab -> copy project id.


<img width="800" alt="Notebook Ready" src="/labs/risk-and-compliance/assets/hands_on_lab_images/project-id.png">
   
  
<img width="800" alt="Notebook Ready" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model18.png">

---

> **Note:** The Model Developer can use this Notebook for evaluation and integration.

---

### **Step 2 – Run Notebook in watsonx.governance**

Run the above notebook and then visualize the results in **IBM watsonx Openscale** Dashboard:


#### Using the UI:


Navigate to the **Detached Prompt Template** asset within the project on **[Openscale](https://aiopenscale.cloud.ibm.com/aiopenscale/insights?nocache=true&bss_account=4b9fae855573451bb6e3bb27d9153c4a)** Dashboard:


<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model8 .png">


### **Step 3 – AI Factsheet View of Detached Prompt Template **


1. Go to dataplatform.cloud.ibm.com watsonx studio


<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model20.png">


2. Navigate: hamburger menu → projects → view all projects → HR Process Automation (select this project)

   

<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model23.png">



3. Inside this project, you will find **Detached prompt template** named **Agentic RAG** - select that

   

<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model25.png">  



4. After selecting, you will be onboarded to **AI Factsheet**



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model26.png">



5. Now click on **Track in AI use case**  to associate asset to **AI Use case** click on **Go to AI Use cases** as project is not associated to **AI Use case** :


   
<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model51.png">



6. Select **AI Use case** created by **Use case owner** initially :



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model52.png">



7. Go to **Associated workspaces** section and Select **Validation** phase and click on **Associate Workspace**:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model53.png">



9. Here, Select **Project** created initially and Deployment space created  or if you have not created Click on **+New Space** and follow [Deployment Creation Steps](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/instructor/deploy-project.md) these steps for creating deployment space for **Testing** Deployment stage. Click on Save:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model54.png">



10. Now **AI Use case** is associated to **project** and **deployment space**.In **Associated Workspaces** Section Click on Arrow beside **your project** under **Validation** phase:


    
<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model55.png">



11. In project go to **Assets** tab select **Agentic RAG testing** asset and click on three dot then select **Go to AI factsheet**



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model63.png">    



12. Now **AI Use case** is getting tracked in **Validation** phase so Click on **Track in AI Use case**:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model57.png">



13. Select Approach set as **Default Approach** or click on **+New Approach** for defining one path for solving the goal of the use case. Click on **Next**:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model58.png">



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model59.png">



14. Associate the **asset** with an existing model record or create a new model record in OpenPages. This will sync the tracked model facts between Model inventory and OpenPages.Click on **Next**.



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model60.png">



15. Choose the starting point for this approach(Experimental,Stable,Custom) any one of them for **version** tracking. Click on **Next**:



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model61.png">



16. Review to make sure that your detached prompt template is stable before you track it in an **AI use case**. Click on **Track Asset**:



 <img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model62.png">   



Finally **Agentic RAG** getting tracked in **AI Use case**. Click on **Agentic RAG Testing** under asset record to view it in **Governance Console**



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model63.png"> 



<img width="800" alt="Detached Prompt Template UI" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Model64.png"> 

17.Now Go to [Model Lifecycle part to start process for validation](http://github.ibm.com/skol/ai-governance-client-bootcamp/edit/main/labs/risk-and-compliance/assets/tasks/Model%20lifecycle)

> [!Note]
> Model Developer has developed **Agentic RAG Detached prompt template** and Also onboarded it to **AI Use case**

---

## Prerequisites

- IBM Cloud account with access to watsonx.governance
- Access to the pre-deployed Agentic RAG model
- Permissions to create and manage projects in Watsonx Studio

## Resources

- [IBM Cloud Platform](https://cloud.ibm.com/login)
- [Project Creation Steps](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/instructor/create-project.md)
- [Create API key](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/instructor/create-api-key.md)
- [Agentic RAG Notebook](https://github.ibm.com/skol/ai-governance-client-bootcamp/blob/main/labs/risk-and-compliance/assets/agentic-rag.ipynb)

