> ⚠️ **Login Note:** Before starting, ensure you are logged into **IBM OpenPages** using the **Use case owner** role.
> This access is required to create and manage **Business Entities**, **Model Use Cases**, and perform associated governance tasks.

---

# 📊 Business Entity Creation in watsonx.governance

## 📌 Overview

This guide walks you through creating a **Primary Business Entity** and a **Child Business Entity** in watsonx.governance for the **AskHR Project**, under the **Techcorp** organization.

---

## 🏢 Business Entity Creation

In **IBM OpenPages**, a **Business Entity**:

* Represents a logical division or unit within an organization.
* Serves as a container for managing risks, controls, issues, and processes.
* Supports parent/child hierarchy to enable structured governance.

---

## 🎯 Structure to Be Created

| Entity Level   | Entity Name   | Description                                                        |
| -------------- | ------------- | ------------------------------------------------------------------ |
| Primary Entity | Techcorp      | Main entity representing the organization.                         |
| Child Entity   | AskHR - GenAI | GenAI use case entity under the AskHR project, linked to Techcorp. |

---

## 🛠️ Step-by-Step Creation Process

### 1️⃣ Step 1: Create Primary Business Entity — Techcorp

1. **Log in as:**
   `Use case owner`

2. **Navigate to the Business Entity Section:**

   * Click the **Hamburger Menu (☰)**.
   * Go to **Organization**.
   * Select **Business Entity**.

   <img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Business_entity.png">

3. **Create a New Entity:**

   * Click **Create New**.
   * Fill in the following fields:

   | Field             | Value                                |
   | ----------------- | ------------------------------------ |
   | **Entity Name**   | `Techcorp`                           |
   | **Description**   | Parent entity representing Techcorp. |
   | **Owner**         | Use case owner     |
   | **Business Unit** | As applicable                        |

4. **Click Save.**

   <img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/primary_entity.png">

---

### 2️⃣ Step 2: Create Child Business Entity — AskHR - GenAI

1. After **Techcorp** is created, click **Create New** again to add the child entity.

2. Fill in the following fields:

   | Field                       | Value                                                    |
   | --------------------------- | -------------------------------------------------------- |
   | **Entity Name**             | `AskHR - GenAI`                                          |
   | **Description**             | Child entity for the GenAI use case under AskHR project. |
   | **Owner**                   | Use case owner / Governance Lead                            |
   | **Business Unit**           | As applicable                                            |
   | **Primary Business Entity** | Select `Techcorp` from the dropdown or lookup list.      |

   <img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Screenshot 2025-07-17 at 5.32.40 PM.png">

3. ✅ **Ensure `Techcorp` is selected** as the **Primary Business Entity**.

4. **Click Save.**

---

## ✅ Example Child Entity Summary

* **Entity Name:** `AskHR - GenAI`
* **Description:** Child entity for the GenAI use case in the AskHR project.
* **Primary Business Entity:** `Techcorp`
* **Owner:** Use case owner

---

## 📊 Summary

By setting up:

* **Techcorp** as the **Primary Business Entity**, and
* **AskHR - GenAI** as a **Child Entity** linked to it,

You enable:

* Clear governance hierarchy
* Focused compliance tracking
* Organized risk and issue management within your AI initiatives

<img width="800" alt="image" src="/labs/risk-and-compliance/assets/hands_on_lab_images/Screenshot 2025-07-17 at 5.35.09 PM.png">

---

👏 **Well Done!**
Creating structured Business Entities in OpenPages sets a strong foundation for scalable, transparent, and well-governed AI initiatives.
