# Browser Password
### Description
I forgot an important password that i use in a secret environment i must access. I remembered that i had save that password to my friend's chrome browser. When i informed them about that they told me that they couldn't retrieve the plaintext password but they read the other day an article saying that there is a way to get the plaintext of stored passwords in a browser. Sadly they didn't have time to do that for me so they sent me some files that will help me achieve that.


Ξεκινώντας έχουμε 3 αρχεία. Θα πρέπει αρχικά να δούμε πως λειτουργεί το encryption σε chrome browser προκειμένου να γίνουν recover απο τα αρχεία οι αποθηκευμένοι κωδικοί. Υπάρχουν αρκετά άρθρα που εξηγούν πως αποθηκεύονται οι κωδικοί στο browser db. Πολύ απλά χρεάζεται να βρούμε το secret key μέσω του mkey.json. Προκειμένου να γίνει αυτό θα χρησιμοποιήσουμε το παρακάτω python script:
`https://github.com/tijldeneut/dpapilab-ng/blob/main/browserdec.py`

Χρησιμοποιώντας το script με arguments ως εξής:
```python3 key.py --masterkey "3088e97ca870bfb3bdf4677e7dea1d6d449b4b8fb35a97ee9595aee43b77b5846aec27666eea26e702c54d3721ac609d11e802c6c518330e4e925e7833c78607"```

Παίρνουμε αποτέλεσμα το κλειδί: `c20b3d4cf8163aa7cba6acc2c3ada7c45f085f9127b10ba2b36f930da9493d52`

Στην συνέχεια με χρήση του dcp.py: `https://github.com/palmenas/dcp/blob/main/dcp.py`  μπορεί να γίνει πολύ εύκολα recover ο αποθηκευμένος κωδικός.
`python3 yolo.py -S "c20b3d4cf8163aa7cba6acc2c3ada7c45f085f9127b10ba2b36f930da9493d52" -P Login\ Data`


