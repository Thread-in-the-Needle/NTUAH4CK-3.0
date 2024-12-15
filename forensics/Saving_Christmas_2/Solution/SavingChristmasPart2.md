# Saving Christmas Part 2

# Investigating Persistence Techniques

To identify potential persistence techniques employed by the attacker, we analyzed registry entries for suspicious activities. Below is a detailed description of the process:

---

## Step 1: Analyzing Scheduled Tasks

One of the common persistence techniques attackers use is creating malicious **Scheduled Tasks**. To investigate this, we analyzed the **`SOFTWARE`** registry hive file located at:
`system32\config\SOFTWARE`

Using **Registry Explorer**, we navigated to the following path:
`Microsoft\Windows NT\Current Version\Schedule\TaskCache\Tasks`


### Findings
Upon examining the entries in the **Tasks** registry path, we identified multiple scheduled tasks. Among these, a task named **`nhack_plan`** stood out. Analyzing this task's properties revealed that the **flag** was embedded in its description.

---

## Flag

**Flag**: `NHACK{Ch3k1nG_f0r_P3rs1sT4nC3_S33ms_4_G00d_0pt10N}`

