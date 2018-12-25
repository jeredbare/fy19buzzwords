import random

wordlist = ['bug bounty', 'go', 'development', 'blockchain', 'devsecops', 'nextgen', 'secure', 'encryption', 'aes', 'dashboards', 'firewall', 'fast', 'secure', 'cloud', 'fullstack', 'security', 'infosec', 'information', 'patching', 'linux', 'windows', 'server', 'automation', 'metrics', 'management', 'api', 'authorization', 'bucket', 'fargate', 'logging', 'kubernetes', 'devops', 'ci', 'cd', 'pipeline']

buzzwords = random.sample(wordlist, 3)

print("\nYour 2019 Information Security Slogan is...\n")
print("*" * 50)
for i in buzzwords:
	print(i.capitalize(), end=" ")
print("\n" + "*" * 50 + "\n")

print("\n" + "=" * 10 + "What to do with your new slogan" + "=" * 10)
print("Step 1. Sell a product or software based off the slogan without actually building it.\n" + "Step 2. Generate a bunch of media around such slogan.\n" + "Step 3. ????\n" +  "Step 4. Profit\n")
