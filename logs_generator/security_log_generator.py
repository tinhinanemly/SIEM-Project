import json
import random
import time
from datetime import datetime
import ipaddress
import logging
import os

class SecurityLogGenerator:
    def __init__(self):
        # Common attack patterns and indicators
        self.malicious_ips = [
            "192.168.100.50", "10.0.0.100", "172.16.0.50",
            "203.0.113.42", "198.51.100.77", "192.0.2.123"
        ]
        
        self.legitimate_ips = [
            "192.168.1.10", "192.168.1.20", "192.168.1.30",
            "10.0.1.5", "172.16.1.10"
        ]
        
        self.attack_types = [
            "brute_force", "sql_injection", "xss", "dos",
            "port_scan", "malware", "privilege_escalation"
        ]
        
        self.services = ["ssh", "http", "https", "ftp", "dns", "smtp"]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "curl/7.68.0", "wget/1.20.3", "sqlmap/1.4.7",
            "Nmap Scripting Engine", "ZAP/2.10.0"
        ]

    def generate_failed_login(self):
        """Generate failed login attempt logs"""
        return {
            "@timestamp": datetime.now().isoformat(),
            "log": {
                "level": "WARNING"
            },
            "event": {
                "action": "authentication_failure",
                "severity": random.choice([3, 4, 5])
            },
            "source": {
                "ip": random.choice(self.malicious_ips)
            },
            "destination": {
                "ip": random.choice(self.legitimate_ips),
                "port": 22
            },
            "service": {
                "name": "ssh"
            },
            "user": {
                "name": random.choice(["admin", "root", "user", "test", "guest"])
            },
            "message": "Failed password for invalid user",
            "rule": {
                "category": "brute_force"
            }
        }

    def generate_web_attack(self):
        """Generate web application attack logs"""
        payloads = [
            "' OR '1'='1", "<script>alert('xss')</script>",
            "../../etc/passwd", "UNION SELECT * FROM users",
            "../../../windows/system32/config/sam"
        ]
        
        return {
            "@timestamp": datetime.now().isoformat(),
            "log": {
                "level": "CRITICAL"
            },
            "event": {
                "action": "web_attack",
                "severity": random.choice([7, 8, 9])
            },
            "source": {
                "ip": random.choice(self.malicious_ips)
            },
            "destination": {
                "ip": random.choice(self.legitimate_ips),
                "port": random.choice([80, 443, 8080])
            },
            "service": {
                "name": "http"
            },
            "http": {
                "request": {
                    "method": random.choice(["GET", "POST", "PUT"]),
                    "referrer": f"/login.php?id={random.choice(payloads)}"
                },
                "response": {
                    "status_code": random.choice([200, 403, 500])
                }
            },
            "user_agent": {
                "original": random.choice(self.user_agents)
            },
            "rule": {
                "category": random.choice(["sql_injection", "xss", "directory_traversal"])
            }
        }

    def generate_port_scan(self):
        """Generate port scanning logs"""
        return {
            "@timestamp": datetime.now().isoformat(),
            "log": {
                "level": "WARNING"
            },
            "event": {
                "action": "port_scan",
                "severity": 5
            },
            "source": {
                "ip": random.choice(self.malicious_ips)
            },
            "destination": {
                "ip": random.choice(self.legitimate_ips)
            },
            "network": {
                "ports": random.sample(range(1, 65535), random.randint(10, 100))
            },
            "rule": {
                "category": "reconnaissance"
            }
        }

    def generate_dos_attack(self):
        """Generate DoS attack logs"""
        return {
            "@timestamp": datetime.now().isoformat(),
            "log": {
                "level": "CRITICAL"
            },
            "event": {
                "action": "dos_attack",
                "severity": 8
            },
            "source": {
                "ip": random.choice(self.malicious_ips)
            },
            "destination": {
                "ip": random.choice(self.legitimate_ips),
                "port": random.choice([80, 443, 22, 21, 25])
            },
            "service": {
                "name": random.choice(self.services)
            },
            "network": {
                "requests": random.randint(1000, 10000),
                "duration": "1 minute"
            },
            "rule": {
                "category": "dos"
            }
        }

    def generate_malware_detection(self):
        """Generate malware detection logs"""
        malware_names = [
            "Trojan.Win32.Generic", "Backdoor.Linux.Mirai", 
            "Worm.Win32.Conficker", "Ransomware.CryptoLocker"
        ]
        
        return {
            "@timestamp": datetime.now().isoformat(),
            "log": {
                "level": "CRITICAL"
            },
            "event": {
                "action": "malware_detection",
                "severity": 9,
                "outcome": random.choice(["quarantined", "deleted", "blocked"])
            },
            "source": {
                "ip": random.choice(self.malicious_ips)
            },
            "destination": {
                "ip": random.choice(self.legitimate_ips)
            },
            "file": {
                "name": random.choice(malware_names),
                "path": f"/tmp/{random.randint(1000,9999)}.exe"
            },
            "rule": {
                "category": "malware"
            }
        }

    def generate_normal_traffic(self):
        """Generate legitimate traffic logs"""
        return {
            "@timestamp": datetime.now().isoformat(),
            "log": {
                "level": "INFO"
            },
            "event": {
                "action": "normal_access",
                "severity": 1,
                "outcome": "success"
            },
            "source": {
                "ip": random.choice(self.legitimate_ips)
            },
            "destination": {
                "ip": random.choice(self.legitimate_ips),
                "port": random.choice([80, 443, 22])
            },
            "service": {
                "name": random.choice(["http", "https", "ssh"])
            }
        }

    def generate_log_entry(self):
        """Generate a random log entry"""
        # Weight the probability of different log types
        log_types = [
            (self.generate_failed_login, 0.3),
            (self.generate_web_attack, 0.2),
            (self.generate_port_scan, 0.1),
            (self.generate_dos_attack, 0.05),
            (self.generate_malware_detection, 0.05),
            (self.generate_normal_traffic, 0.3)
        ]
        
        # Choose log type based on weights
        rand = random.random()
        cumulative = 0
        for func, weight in log_types:
            cumulative += weight
            if rand <= cumulative:
                return func()
        
        return self.generate_normal_traffic()

    def run_continuous_logging(self, log_file="security_logs.json", interval=2):
        """Continuously generate and write logs"""
        print(f"Starting continuous log generation to {log_file}")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                log_entry = self.generate_log_entry()
                
                # Write to JSON file (for Filebeat)
                with open(log_file, "a") as f:
                    f.write(json.dumps(log_entry) + "\n")
                
                print(f"Generated: {log_entry['event']['action']} from {log_entry.get('source', {}).get('ip', 'N/A')}")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nLog generation stopped")

    def generate_batch_logs(self, count=1000, filename="batch_security_logs.json"):
        """Generate a batch of logs for testing"""
        print(f"Generating {count} log entries...")
        
        with open(filename, "w") as f:
            for i in range(count):
                log_entry = self.generate_log_entry()
                f.write(json.dumps(log_entry) + "\n")
                
                if (i + 1) % 100 == 0:
                    print(f"Generated {i + 1} logs...")
        
        print(f"Batch generation complete: {filename}")

if __name__ == "__main__":
    generator = SecurityLogGenerator()
    
    print("Security Log Generator")
    print("1. Run continuous logging")
    print("2. Generate batch logs")
    
    choice = input("Choose option (1 or 2): ")
    
    if choice == "1":
        interval = int(input("Enter logging interval in seconds (default 2): ") or "2")
        generator.run_continuous_logging(interval=interval)
    elif choice == "2":
        count = int(input("Enter number of logs to generate (default 1000): ") or "1000")
        generator.generate_batch_logs(count=count)
    else:
        print("Invalid choice")
