# h3_honey_pot

## What is a Honeypot?
A honeypot is a cybersecurity mechanism designed to detect, deflect, or study cyber threats by mimicking a real system. It acts as a decoy to lure attackers, allowing security professionals to analyze their techniques, monitor malicious activities, and enhance overall security strategies.

To understand more, watch these tutorials:
- [Honeypot Explained (Video 1)](https://www.youtube.com/watch?v=gI8LnMAhBv8)
- [Honeypot Explained (Video 2)](https://www.youtube.com/watch?v=o3thhfKN6iQ)

## How Does It Work?
Honeypots are typically set up to resemble legitimate IT systems, such as:
1. Web servers
2. Database servers
3. IoT devices
4. Network environments

Attackers, believing the honeypot to be a vulnerable target, attempt to exploit it. These interactions provide valuable data on attack patterns, tools, and methodologies used by cybercriminals.

## Types of Honeypots
### 1. Low-Interaction Honeypots
- Simulate limited functionality of real systems.
- Primarily used for gathering basic information on automated attacks.
- Easier to maintain and secure.

### 2. High-Interaction Honeypots
- Fully functional systems that replicate real environments.
- Provide in-depth insights into attacker behavior.
- Require more resources and careful monitoring to prevent misuse.

## Benefits of Using Honeypots
- **Threat Intelligence**: Gather real-world attack data for analysis.
- **Early Threat Detection**: Identify new attack vectors before they impact critical systems.
- **Deception and Defense**: Misdirect attackers away from valuable resources.
- **Improved Security Policies**: Strengthen cybersecurity strategies based on observed threats.

## Risks of Using Honeypots
- **Potential for Exploitation**: If not properly isolated, attackers could leverage honeypots to attack other systems.
- **Resource Intensive**: High-interaction honeypots require constant monitoring and maintenance.
- **Legal and Ethical Concerns**: Operating honeypots should comply with legal frameworks to avoid entrapment issues.

## Setting Up a Honeypot with an SSH Server
### Method 1: Fool the Attacker Using EndlessSSH

### Step 1: Understand How EndlessSSH Works
EndlessSSH is a lightweight SSH honeypot that runs indefinitely and logs SSH brute-force attempts. It doesn’t allow actual access but can be used to collect attacker credentials and analyze attack patterns.

### Step 2: Prepare Your Environment
You'll need:
- A Linux-based system
- Root access
- A way to monitor logs

### Step 3: Install EndlessSSH
#### 1. Install Dependencies
```bash
sudo apt update
sudo apt install -y build-essential git
```

#### 2. Clone the Repository
```bash
git clone https://github.com/skeeto/endlessh.git
cd endlessh
```

#### 3. Compile EndlessSSH
```bash
make
```

#### 4. Install the Binary
```bash
sudo make install
```

#### 5. Configure EndlessSSH
```bash
sudo mkdir -p /etc/endlessh
sudo nano /etc/endlessh/config
```
Add the following content to `config`:
```
Port 2222
Delay 10000
MaxLineLength 32
LogLevel 1
```

#### 6. Create a Systemd Service
```bash
sudo nano /etc/systemd/system/endlessh.service
```
Add the following content:
```
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
```

#### 7. Verify It’s Running
```bash
sudo systemctl status endlessh
telnet localhost 2222
```

#### 8. Modify the SSH Port (Optional)
Change the SSH server port from 22 to 66:
```bash
sudo nano /etc/ssh/sshd_config
```
Uncomment and modify this line:
```
#Port 22
```
Replace it with:
```
Port 66
```
### Method 2: HoneyPot Forms 

A Honeypot Form is a security technique used to detect and block automated bots from submitting forms on websites. 
The core idea is to add an extra, hidden input field that is visible to bots but invisible to human users. 
Since bots typically fill in all input fields they detect, a filled honeypot field can be a strong indication of bot activity.

### How Honeypot Forms Work
Adding a Hidden Input Field:

A form includes a hidden input field that real users do not see.
The field is either visually hidden using CSS (display: none; or visibility: hidden;) or positioned off-screen.
User vs. Bot Behavior:

A real user will not fill out the hidden field because they never see it.
A bot, which scans and fills all input fields, will likely enter data into the honeypot field.
Form Submission Validation:

If the honeypot field contains any data, the form submission is flagged as spam and either ignored or logged for further analysis.
If the honeypot field is empty, the submission is considered legitimate.

### Advantages :

- Invisible to real users (no CAPTCHA frustration).
- Easy to implement with minimal impact on UX.
- No JavaScript dependency, making it accessible.

### Limitations :

- Advanced bots can detect hidden fields using CSS analysis.
- Some screen readers may still detect the field, potentially affecting accessibility.


## Setting Up a Honeypot with an HTTP Server
(Coming soon...)

---
### Contributors
#### OUAFI Omar
#### EREKYSY Anass
#### NAOUI Nassera



