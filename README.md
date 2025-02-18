# h3_honey_pot

# what's a honeypot ?

A honeypot is a cybersecurity mechanism designed to detect, deflect, or study cyber threats by mimicking a real system. 
It acts as a decoy to lure attackers, allowing security professionals to analyze their techniques, monitor malicious activities, and enhance overall security strategies.

To understand more watch those tutorials: 
https://www.youtube.com/watch?v=gI8LnMAhBv8
https://www.youtube.com/watch?v=o3thhfKN6iQ

# How does it work ?

Honeypots are typically set up to resemble legitimate IT systems, such as:

1. Web servers
2. Database servers
3. IoT devices
4. Network environments

Attackers, believing the honeypot to be a vulnerable target, attempt to exploit it. 
These interactions provide valuable data on attack patterns, tools, and methodologies used by cybercriminals.

# Types of Honeypot ?

1. Low-Interaction Honeypots : 

Simulate limited functionality of real systems.
Primarily used for gathering basic information on automated attacks.
Easier to maintain and secure

2. High-Interaction Honeypots :

Fully functional systems that replicate real environments.
Provide in-depth insights into attacker behavior.
Require more resources and careful monitoring to prevent misuse.

# Benefits of Using Honeypots ?

Threat Intelligence: Gather real-world attack data for analysis.
Early Threat Detection: Identify new attack vectors before they impact critical systems.
Deception and Defense: Misdirect attackers away from valuable resources.
Improved Security Policies: Strengthen cybersecurity strategies based on observed threats.

# Risks of using a Honeypots ?

Potential for Exploitation: If not properly isolated, attackers could leverage honeypots to attack other systems.
Resource Intensive: High-interaction honeypots require constant monitoring and maintenance.
Legal and Ethical Concerns: Operating honeypots should comply with legal frameworks to avoid entrapment issues.

# How to achieve a honeypot using an SSH server ?

# Method 1 : Fool the attacker using EndlessSSH 

# step 1 : understand how does work an endlessSSH 

a lightweight SSH honeypot that runs indefinitely and logs SSH brute-force attempts. 
It doesn’t allow actual access but can be used to collect attacker credentials and analyze attack patterns.

# step 2 : Prepare Your Environment

You'll need a Linux-based system , root access, and a way to monitor logs.

# step 3 : Install endlessSSH  

1. install dependencies 
```sudo apt update ```
```sudo apt install -y build-essential git```

2. clone the repository 
```git clone https://github.com/skeeto/endlessh.git```
```cd endlessh```

3. compile endlessSSH
```make```

4. install the binary 
```sudo make install```

5. configure endlessSSH
```sudo mkdir -p /etc/endlessh```
```sudo nano /etc/endlessh/config```
the content of the config file :
Port 2222
Delay 10000
MaxLineLength 32
LogLevel 1

6. Create a Systemd Service
```sudo nano /etc/systemd/system/endlessh.service```

the content of the file endlessh.service : 
[Unit]
Description=Endlessh SSH Honeypot
After=network.target
[Service]
ExecStart=/root/endlessh/endlessh -p 22
Restart=always
User=root
Group=root
[Install]
WantedBy=multi-user.target


7. Verify It’s Running
```sudo systemctl status endlessh```
```telnet localhost 2222```

8. Modify the port from 22 to 66 
```nano /etc/ssh/sshd_config ```
Uncomment the line  in this file sshd_config : 
#Port 22
and replace it with 
Port 66


# How to achieve a honeypot using an HTTP server ?
