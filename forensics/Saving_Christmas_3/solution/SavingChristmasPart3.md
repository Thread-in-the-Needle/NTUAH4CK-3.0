# Saving Christmas Part 3

# Decrypting Files Encrypted by `nhack_trip.exe`

To decrypt the files, we identified the encryption method used by the attacker and retrieved the necessary key and IV. Below is the process we followed:

---

## Step 1: Analyze the Executable

We began by analyzing the file **`nhack_trip.exe`**, uploading it to **VirusTotal**. VirusTotal confirmed that this executable was used to encrypt the files. Examining its details, we discovered it was a **.NET application**, making it suitable for further inspection using **dnSpy**.

---

## Step 2: Analyze with dnSpy

We loaded **`nhack_trip.exe`** into **dnSpy** and found the following details:
- **Encryption Algorithm**: AES-CBC
- **Key**: 32 bytes (randomly generated)
- **IV**: 16 bytes (randomly generated)

### Observations
1. The **IV** is written to the **last 16 bytes** of each encrypted file.
2. The **key** is saved in the **user's temporary folder**, with the filename being the **Base64-encoded value of the name of the file being encrypted**.

---

## Step 3: Verifying the Key and IV

To validate the process, we worked with an example file named **`Santa_Wishlist.nhack`**:
1. **Extract the IV**: The **last 16 bytes** of the file are:
`f0 07 c3 a9 1a df 15 b3 d2 45 55 f4 98 49 77 e9`

2. **Locate the Key**:
- Convert the file name **`Santa_Wishlist`** to **Base64**, resulting in:
  ```
  U2FudGFfV2lzaGxpc3Q=
  ```
- Navigate to the path **`Users\nhack\AppData\Local\Temp`** and locate the file named **`U2FudGFfV2lzaGxpc3Q=`**.
- This file contains the **32-byte key** required for decryption.

---

## Step 4: Decrypt the File

With the **key** and **IV**, we decrypted the file using the **AES-CBC** algorithm in **NoPadding** mode. The process successfully recovered the original content, including the flag.


## Flag

**Flag**: `NHACK{d3cRypT1nG_a1nt_4lwAyS_Th1s_3aSy}`
