# ICMP_Party
### Description
Recently our network engineers noticed a weird icmp traffic. Can you find out what happened?

### Writeup

Ξεκινώντας έχουμε ενα αρχείο pcap. Οπότε το ανοίγουμε με wireshark για ανάλυση. Σύμφωνα με την περιγραφή θα επικεντρωθούμε στο πρωτόκολλο icmp. Βάζοντας ως φίλτρο `icmp` έχουμε 78 πακέτα μόνο. Με λίγη προσεκτική παρατήρηση βλέπουμε πως τα πακέτα προς την IP 192.168.1.233 έχουν πάντα ttl με τιμή 64 ενώ τα υπόλοιπα αλλάζουν τιμή. Αποθηκεύοντας όλες τις τιμές ttl και κάνοντας Decode με χρήση FromDecimal ```(https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false))``` παίρνουμε το flag.

