# Saving Christmas Part 1

# Investigating the Entry Point of the Attack

To identify the entry point of the attack, we analyzed relevant log files for suspicious activity. Below is the detailed breakdown of the investigation:

---

## Step 1: Analyzing Failed Login Attempts

To investigate failed login attempts, we analyzed the **`security.evtx`** file using **Event Viewer**. By filtering for **Event ID 4625**, we obtained **282 events**. Upon closer inspection, we found that **2 events were unrelated to the attack**, leaving the final count as **`280` failed login attempts**.

**Answer 1**: `280`

---

## Step 2: Finding the First Successful Login

To find the first successful login, we continued analyzing the **`security.evtx`** file, this time filtering for **Event ID 4624**. Based on our prior analysis, we searched for logins associated with the attacker's IP. The first reference to the attacker's IP occurred at:

**Timestamp**: `2024-11-14T23:06:23` (UTC)

**Answer 2**: `2024-11-14T23:06:23`

---

## Step 3: Identifying the First Disconnection

For the first disconnection, we filtered **Event ID 4634** in the **`security.evtx`** file, yielding **54 events**. Many were associated with the user `nhack`. Initially, we noted a logoff event 3 seconds after the successful login, but this did not match our analysis of the attacker’s activity.

To accurately identify when the attacker disconnected, we turned to the **`Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx`** log. Filtering for **Event ID 24** and cross-referencing with the attacker’s IP, we found the first session disconnect at:

**Timestamp**: `2024-11-14T23:08:53` (UTC)

**Answer 3**: `2024-11-14T23:08:53`

---

## Step 4: Identifying the Attacker's IP and Hostname

From our earlier analysis, we confirmed the following details about the attacker:
- **IP Address**: `192.168.38.129`
- **Victim's Hostname**: `DESKTOP-3AEH23H`

**Answer 4**: `192.168.38.129`  
**Answer 5**: `DESKTOP-3AEH23H`

---

## Summary of Answers
1. **Number of Failed Login Attempts**: `280`
2. **Timestamp of First Successful Login**: `2024-11-14T23:06:23`
3. **Timestamp of First Disconnection**: `2024-11-14T23:08:53`
4. **Attacker's IP**: `192.168.38.129`
5. **Victim's Hostname**: `DESKTOP-3AEH23H`
